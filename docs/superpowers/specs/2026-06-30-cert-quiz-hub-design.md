# 설계: Salesforce Slack 자격증 퀴즈 허브

작성일: 2026-06-30

## 목적

Salesforce Slack 자격증 학습 가이드(developer·admin·consultant) 3종의 예시문제를
누구나 링크로 풀어볼 수 있는 **단일 인터랙티브 퀴즈 허브**로 공개한다. 기존
developer 전용 퀴즈(`salesforce-slack-developer-quiz`)를 3종 통합 허브로 일반화한다.

- 단일 출처: 각 가이드의 `content/*.md`(연습문제 + 종합 모의고사)
- 한국어 전용, 객관식(단일/복수 선택), 정답·해설 제공
- 기존 공부모드/시험모드 UX 재사용 + 자격증 선택 랜딩 추가

비목표(범위 제외):
- **discovery(인터뷰 키트)**: 객관식 정답이 있는 문항이 없어 제외
- 기존 developer 퀴즈 레포 리다이렉트/배너(후속 과제로 분리)
- 로그인·점수 저장·서버(정적 사이트 유지)

## 배포 구조

- 신규 public 레포 `salesforce-slack-cert-quiz`, GitHub Pages.
  URL: `https://soonyeon-kim.github.io/salesforce-slack-cert-quiz/`
- 빌드 의존성 없는 정적 단일 페이지(`index.html` = HTML+CSS+JS).
- 모노레포 워킹트리에서 `slack_admin/`·`slack_consultant/`·`slack_developer/` 와
  형제 디렉터리로 위치 → 빌더가 `../slack_*/content` 를 상대경로로 읽음(기존
  developer 퀴즈와 동일 모델). 산출 `questions.json` 은 레포에 커밋되어 런타임에는
  가이드가 필요 없음.

## 컴포넌트

### 1. `build_questions.py` (문항 추출기)

기존 developer 추출기를 일반화한다.

- 입력: `CERTS` 매핑으로 3개 가이드의 `content` 디렉터리.
- 챕터 파싱(`parse_chapter`)·모의고사 파싱(`parse_mock`) 로직은 그대로 재사용
  (3종 가이드가 동일 마크다운 포맷 사용 확인됨).
- 변경점:
  - cert별 루프 → 각 문항에 `cert` 필드(`developer`/`admin`/`consultant`) 추가.
  - `id` 는 전체 통합 일련번호(1..N).
  - 모의고사 해설 요약 매핑 시 `·` 구분에 더해 **범위 표기(`8~12`)도 전개**
    (현재는 `·` 만 처리해 일부 mock 해설 누락 → 개선). 챕터 해설은 영향 없음.
- 출력: 단일 `questions.json`(배열). 스키마:
  ```json
  {
    "id": 1,
    "cert": "developer",
    "domain_id": 1,
    "domain": "1. 슬랙 플랫폼의 앱",
    "question": "...",
    "options": [{"id": "A", "text": "..."}],
    "correct_answer": ["C"],
    "explanation": "..."
  }
  ```

### 2. `questions.json` (데이터)

- 단일 파일, 각 문항에 `cert` 필드. 총 ~130문항(소용량 → 1회 로드 후 cert로 필터).

### 3. `index.html` (앱)

기존 developer 퀴즈 UI를 토대로 화면 흐름을 한 단계 확장한다.

1. **랜딩(자격증 선택)**: developer/admin/consultant 카드 3장.
   각 카드에 문항수·합격선 표기. 선택 시 해당 cert로 진입.
2. **모드 선택 / 공부모드 / 시험모드**: 기존 로직 재사용.
   - 공부모드: 도메인(=챕터) 선택 + 문제 수 지정, 즉시 정오답·해설.
   - 시험모드: 해당 cert 전체 문항 랜덤, 제한시간, 합격선.
3. **자격증 변경**: 랜딩으로 복귀.

### 4. cert 메타데이터(앱 내 상수)

| cert | 표시명 | 문항 | 합격선 | 권장 시간 |
|---|---|---|---|---|
| developer | Salesforce Certified Slack Developer | 47 | 67% | 75분 |
| admin | Salesforce Certified Slack Administrator | 41 | 65% | 65분 |
| consultant | Salesforce Certified Slack Consultant | 42 | 67% | 67분 |

- 권장 시간 ≈ 1.6분/문항 반올림. 시험모드는 해당 cert 공식 합격선 사용.
- 도메인 라벨 = 가이드 챕터(1..N). admin 가이드는 7챕터 구조 유지(시험 6도메인
  매핑은 가이드 본문이 설명) → 퀴즈 도메인 필터는 챕터 기준.

## 데이터 흐름

```
slack_{developer,admin,consultant}/content/*.md
        │  python build_questions.py
        ▼
   questions.json  (cert 필드 포함, 레포에 커밋)
        │  fetch (정적)
        ▼
   index.html  → 랜딩(cert 선택) → 공부/시험 모드
```

가이드 갱신 시 `python build_questions.py` 재실행으로 `questions.json` 재생성.

## 에러 처리·엣지케이스

- 빌더: H1 도메인 라벨 미발견, 문제-정답 매핑 누락 시 명시적 예외(기존 동작 유지).
- 검증(`validate`): cert별 기대 문항수(dev 47 / admin 41 / consultant 42) +
  구조 검증(보기≥2, 정답이 보기 내, 질문/정답 비어있지 않음, 챕터 문항 해설 존재).
  모의고사 문항 해설은 선택(누락 허용).
- 앱: `questions.json` 로드 실패 시 안내 메시지. 복수 정답 문항은 부분점수 없이
  완전일치만 정답(기존 동작 유지).

## 면책

"학습 점검용 자체 제작 예상문제이며 공식 기출이 아니다. 공개된 학습 가이드 기반."
README·앱 내 표기 유지. 플랜·정책 사실은 가이드 최신 정정 반영(단일 출처).

## 테스트·배포

- 빌드 검증: `python build_questions.py` 가 cert별 기대 문항수로 통과.
- 수동 검증: 로컬에서 `index.html` 열어 3개 cert 각각 공부/시험 모드 동작,
  복수정답·해설 표시, 자격증 변경 확인.
- 배포: 신규 레포 push → GitHub Pages 활성화 → 라이브 URL 확인.

## 파일 구성(예정)

```
salesforce-slack-cert-quiz/
  index.html
  questions.json
  build_questions.py
  README.md
  docs/superpowers/specs/2026-06-30-cert-quiz-hub-design.md
```
