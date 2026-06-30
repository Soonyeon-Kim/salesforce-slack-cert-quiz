#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Salesforce Slack 자격증 학습 가이드 3종(developer·admin·consultant)의 예시문제를
퀴즈 허브용 단일 questions.json 으로 추출한다.

소스(단일 출처): 각 가이드의 content 디렉터리 (모노레포 형제 디렉터리)
  - 챕터 연습문제: content/01..0N-*.md 의 `## 연습문제` 섹션
  - 종합 모의고사: content/C-mock-exam.md (정답 키 + 장별 요약 해설)

출력 스키마(한국어 전용):
  {
    "id": 1,                        # 전체 통합 일련번호(1..N)
    "cert": "developer",            # developer | admin | consultant
    "domain_id": 1,                 # 챕터 번호, 모의고사는 "mock"
    "domain": "1. 슬랙 플랫폼의 앱",
    "question": "...",
    "options": [{"id": "A", "text": "..."}, ...],
    "correct_answer": ["C"],
    "explanation": "..."
  }

Windows: PYTHONUTF8=1 환경에서 실행 권장.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # 모노레포 루트(slack_* 와 형제)
OUT_PATH = Path(__file__).resolve().parent / "questions.json"

# cert 키 → (가이드 디렉터리명, 기대 문항수)
CERTS = [
    ("developer", "slack_developer", 47),
    ("admin", "slack_admin", 41),
    ("consultant", "slack_consultant", 42),
]


def clean(text: str) -> str:
    """플레인 텍스트 렌더링용으로 마크다운 강조 마커 제거."""
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def section(lines, header):
    """`## {header}` 다음부터 다음 `## ` 헤더 전까지의 줄을 반환."""
    out, capturing = [], False
    for ln in lines:
        if ln.strip() == f"## {header}":
            capturing = True
            continue
        if capturing and ln.startswith("## "):
            break
        if capturing:
            out.append(ln)
    return out


# ── 챕터 파싱 ────────────────────────────────────────────────────────────
H1_RE = re.compile(r"^#\s*(\d+)\.\s*.*?\(([^)]+)\)")
Q_RE = re.compile(r"^\*\*문제\s*(\d+)\.\*\*\s*(.+)$")
OPT_RE = re.compile(r"^-\s*([A-D])\)\s*(.+)$")
# > **1) C.** 해설   또는   > **3) A, C, D.** 해설
ANS_RE = re.compile(r"^>\s*\*\*(\d+)\)\s*([A-D](?:\s*,\s*[A-D])*)\.\*\*\s*(.*)$")


def domain_label(path: Path) -> tuple[int, str]:
    first = path.read_text(encoding="utf-8").splitlines()[0]
    m = H1_RE.match(first)
    if not m:
        raise ValueError(f"H1에서 도메인 라벨을 못 찾음: {path.name} → {first!r}")
    n, ko = int(m.group(1)), m.group(2).strip()
    return n, f"{n}. {ko}"


def parse_chapter(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    dom_id, dom_label = domain_label(path)
    body = section(lines, "연습문제")

    # 문제별 블록 수집
    questions, answers = {}, {}
    cur_num, cur_stem, cur_opts = None, None, []

    def flush():
        if cur_num is not None:
            questions[cur_num] = {"stem": cur_stem, "options": cur_opts}

    for ln in body:
        qm = Q_RE.match(ln.strip())
        if qm:
            flush()
            cur_num = int(qm.group(1))
            cur_stem = qm.group(2).strip()
            cur_opts = []
            continue
        om = OPT_RE.match(ln.strip())
        if om and cur_num is not None:
            cur_opts.append({"id": om.group(1), "text": clean(om.group(2))})
            continue
        am = ANS_RE.match(ln)
        if am:
            num = int(am.group(1))
            letters = [x.strip() for x in am.group(2).split(",")]
            answers[num] = {"correct": letters, "explanation": clean(am.group(3))}
    flush()

    out = []
    for num in sorted(questions):
        if num not in answers:
            raise ValueError(f"{path.name} 문제 {num}: 정답·해설 누락")
        q = questions[num]
        out.append({
            "domain_id": dom_id,
            "domain": dom_label,
            "question": clean(q["stem"]),
            "options": q["options"],
            "correct_answer": answers[num]["correct"],
            "explanation": answers[num]["explanation"],
        })
    return out


# ── 모의고사 파싱 ────────────────────────────────────────────────────────
MOCK_Q_RE = re.compile(r"^\*\*(\d+)\.\*\*\s*(.+)$")
INLINE_OPT_RE = re.compile(r"([A-D])\)\s*(.+?)(?=\s{2,}[A-D]\)|$)")
KEY_RE = re.compile(r"(\d+)\)\s*([A-D](?:\s*,\s*[A-D])*)")
# 장별 요약 해설: - **1·2·3·4** ...  또는  - **8~12** ... (범위 표기)
SUMMARY_RE = re.compile(r"^-\s*\*\*([\d·~–\-\s]+)\*\*\s*(.+)$")
RANGE_RE = re.compile(r"^(\d+)\s*[~–-]\s*(\d+)$")


def expand_nums(spec: str) -> list[int]:
    """'1·2·3' 또는 '8~12'(범위) 같은 번호 명세를 문항 번호 리스트로 전개."""
    nums = []
    for part in spec.split("·"):
        part = part.strip()
        rng = RANGE_RE.match(part)
        if rng:
            nums.extend(range(int(rng.group(1)), int(rng.group(2)) + 1))
        elif part.isdigit():
            nums.append(int(part))
    return nums


def parse_mock(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1) 문제 + 인라인 보기
    qs = {}
    cur = None
    for ln in lines:
        qm = MOCK_Q_RE.match(ln.strip())
        if qm:
            cur = int(qm.group(1))
            qs[cur] = {"stem": qm.group(2).strip(), "options": []}
            continue
        if cur is not None and re.match(r"^[A-D]\)", ln.strip()):
            for oid, otext in INLINE_OPT_RE.findall(ln.strip()):
                qs[cur]["options"].append({"id": oid, "text": clean(otext)})
            cur = None  # 보기 한 줄 처리 후 종료

    # 2) 정답 키 (> ✅ **정답 키** 블록의 > 로 시작하는 줄들)
    key = {}
    in_key = False
    for ln in lines:
        if "정답 키" in ln:
            in_key = True
            continue
        if in_key:
            if ln.startswith(">"):
                for num, letters in KEY_RE.findall(ln):
                    key[int(num)] = [x.strip() for x in letters.split(",")]
            elif ln.strip() == "":
                continue
            else:
                break

    # 3) 장별 요약 해설 → 문항별 매핑 (· 구분 + 범위 표기 전개)
    expl = {}
    for ln in lines:
        sm = SUMMARY_RE.match(ln.strip())
        if sm:
            etext = clean(sm.group(2))
            for n in expand_nums(sm.group(1)):
                expl[n] = etext

    out = []
    for num in sorted(qs):
        if num not in key:
            raise ValueError(f"{path.name} 모의고사 문제 {num}: 정답 키 누락")
        out.append({
            "domain_id": "mock",
            "domain": "종합 모의고사",
            "question": clean(qs[num]["stem"]),
            "options": qs[num]["options"],
            "correct_answer": key[num],
            "explanation": expl.get(num, ""),
        })
    return out


# ── 검증 ────────────────────────────────────────────────────────────────
def validate(questions):
    counts = {}
    for q in questions:
        counts[q["cert"]] = counts.get(q["cert"], 0) + 1
    for cert, _, expected in CERTS:
        actual = counts.get(cert, 0)
        assert actual == expected, f"{cert}: 문항 수 {expected} 기대, 실제 {actual}"

    for q in questions:
        opt_ids = {o["id"] for o in q["options"]}
        assert len(q["options"]) >= 2, f"id={q['id']}: 보기 부족"
        assert q["question"], f"id={q['id']}: 질문 비어있음"
        assert q["correct_answer"], f"id={q['id']}: 정답 비어있음"
        for c in q["correct_answer"]:
            assert c in opt_ids, f"id={q['id']}: 정답 {c}가 보기에 없음 ({opt_ids})"
        if q["domain_id"] != "mock":
            assert q["explanation"], f"id={q['id']}: 챕터 문항 해설 누락"


def main():
    raw = []
    for cert, dirname, _ in CERTS:
        content = ROOT / dirname / "content"
        cert_qs = []
        for path in sorted(content.glob("0[1-9]-*.md")):
            cert_qs.extend(parse_chapter(path))
        cert_qs.extend(parse_mock(content / "C-mock-exam.md"))
        for q in cert_qs:
            q["cert"] = cert
        raw.extend(cert_qs)

    # 전체 통합 일련번호 + 스키마 키 순서 정렬
    questions = []
    for idx, q in enumerate(raw, 1):
        questions.append({
            "id": idx,
            "cert": q["cert"],
            "domain_id": q["domain_id"],
            "domain": q["domain"],
            "question": q["question"],
            "options": q["options"],
            "correct_answer": q["correct_answer"],
            "explanation": q["explanation"],
        })

    validate(questions)

    OUT_PATH.write_text(
        json.dumps(questions, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"OK: {len(questions)}문항 작성 → {OUT_PATH.name}")
    for cert, _, _ in CERTS:
        cert_qs = [q for q in questions if q["cert"] == cert]
        chapters = sum(1 for q in cert_qs if q["domain_id"] != "mock")
        mock = sum(1 for q in cert_qs if q["domain_id"] == "mock")
        multi = sum(1 for q in cert_qs if len(q["correct_answer"]) > 1)
        no_expl = sum(1 for q in cert_qs if not q["explanation"])
        print(f"  {cert:11s}: {len(cert_qs):3d}문항 "
              f"(챕터 {chapters} / 모의고사 {mock} / 복수정답 {multi} / 해설없음 {no_expl})")


if __name__ == "__main__":
    sys.exit(main())
