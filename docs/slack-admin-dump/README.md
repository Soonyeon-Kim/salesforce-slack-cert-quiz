# Salesforce Certified Slack Administrator — 덤프 검증·해설 (212문항)

서드파티로 유통되는 **Salesforce Certified Slack Administrator 덤프**(`V12.65`, 212문항)를
학습용으로 검증하고, 문항별 **핵심 개념·정답(독립 재판정)·정답 근거·보기별 오답 해설·공식 출처**를 정리한 문서입니다.

## ⚠️ 면책

- 이 문서의 문제·보기는 **비공식 서드파티 덤프**에서 가져온 것이며, **개인 학습·개념 점검용**입니다. 공식 기출이 아니고 Salesforce/Slack과 무관합니다.
- **덤프의 정답은 오류·모호함이 흔합니다.** 그래서 각 문항은 덤프 정답을 그대로 믿지 않고 **독립적으로 재판정**했습니다.
- 정답 재판정·해설은 **best-effort 검증**이며 **공식 시험 정답을 보장하지 않습니다.** 실제 시험 대비 시 반드시 공식 학습 가이드로 교차 확인하세요.

## 표기 규칙

- `✅ 재판정 일치` — 내 판단이 덤프 정답과 같음
- `⚠️ 재판정 불일치/논란` — 덤프 정답이 틀렸거나 논란의 여지가 있음(내 판단과 근거 병기)
- `(확신도: 중/낮음)` — 확신이 낮아 재확인을 권하는 항목
- **문제·보기는 영어 원문 유지**, 해설·개념·근거는 한국어. 출처는 가능한 경우 공식 Slack Help Center/문서를 인용.

## 파일 인덱스

| 파일 | 범위 | ⚠️ 문항 |
|---|---|---|
| [slack-admin-dump-001-050.md](./slack-admin-dump-001-050.md) | NO.1~50 | NO.25, NO.30 |
| [slack-admin-dump-051-100.md](./slack-admin-dump-051-100.md) | NO.51~100 | NO.51, NO.71, NO.99, NO.100 |
| [slack-admin-dump-101-150.md](./slack-admin-dump-101-150.md) | NO.101~150 | NO.105 |
| [slack-admin-dump-151-200.md](./slack-admin-dump-151-200.md) | NO.151~200 | NO.163, NO.192 |
| [slack-admin-dump-201-212.md](./slack-admin-dump-201-212.md) | NO.201~212 | 없음 |

## 재판정 불일치·논란(⚠️) 요약표 — 9문항

덤프 정답을 **그대로 외우면 틀릴 수 있는** 문항들입니다. 특히 확신도 '높음'은 공식 문서로 확인했습니다.

| NO | 주제 | 덤프 정답 | 재판정(내 판단) | 사유 | 확신도 |
|---|---|---|---|---|---|
| 25 | External People 대시보드에서 가능한 2가지 | B, E | **A, E** (논란) | 다채널 일괄 제거는 "can only post" 멤버 대상(A 지지). E만 확실 | 낮음 |
| 30 | 리텐션: 중요 보관 + 일부만 1개월 | A | **B** | 시나리오상 기본=전체 보관 + 소수만 예외(1개월). 덤프 A는 반대 | 중 |
| 51 | 잘못된 Connect 초대 대응 | D | **C** (논란) | 멤버가 Connect 권한이 없어 "직접 취소 안내(D)"보다 "대신 취소 제안(C)" | 중 |
| 71 | EMM 로그아웃 시점 안내 | A | **C = 72시간** | "즉시/유예 없음"은 NO.3 및 공식 문서(72시간 설정 기한)와 모순 | **높음** |
| 99 | 커스텀 이모지(CIO가 업로드 꺼림) | A | **B** | 덤프 A(전원 업로드 허용)는 CIO 우려와 배치. 사전 큐레이션 세트(B)가 부합 | 중 |
| 100 | Pro 플랜 SSO "필수" provider | A | A (전제 부정확) | 보기 중 A(Google)가 최선이나 "required" 프레이밍이 부정확(지원일 뿐) | 중 |
| 105 | Grid 네이티브 모바일 통제 2가지 | A, B | **A, E** | 탈옥/루팅 감지(E)가 네이티브. "도메인 허용목록(B)"은 EMM/관리기기 기능 | 중-높음 |
| 163 | conversations.list/info 스코프 | B | **D = channels:read** | 해당 메서드는 channels:read 요구. admin.conversations:read는 admin.* 전용 | **높음** |
| 192 | 워크스페이스 관리 '최소' 역할 | A | **C = Workspace Admin** (논란) | 멤버·설정 관리 최소 역할은 Admin. NO.181(정답 Admin)과도 모순 | 중 |

> 나머지 203문항은 재판정 결과 덤프 정답과 일치(`✅`)하며, 일부는 `(확신도: 중)` 주석과 대안 해석을 병기했습니다.

## 복수정답(Choose N) 문항 — 29문항

아래 문항은 정답이 2개 이상입니다. **완전 일치**로만 정답 처리하세요(부분점수 없음).

`2(A B C)` · `10(A D)` · `19(B E)` · `25(B E)` · `34(A B)` · `37(A B C)` · `48(C D)` · `70(A B)` · `79(B C)` · `94(A B)` · `96(C E)` · `101(A D)` · `102(A E)` · `104(D E)` · `105(A B)` · `111(A E)` · `123(A D F)` · `127(A D)` · `138(B C D)` · `145(B E)` · `152(B D)` · `154(B D)` · `162(D E)` · `169(A B)` · `173(A D)` · `184(A C)` · `185(A C)` · `195(B C D)` · `204(B D)`

> 괄호 안은 **덤프가 제시한 정답**입니다. 이 중 `25`, `105`는 ⚠️ 재판정에서 정답이 달라질 수 있습니다(위 표 참고).

## 검증에 사용한 주요 공식 출처

- [Customize data retention in Slack](https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack)
- [Data residency for Slack](https://slack.com/help/articles/360035633934-Data-residency-for-Slack)
- [Enable Enterprise Mobility Management](https://slack.com/help/articles/115002579426-Enable-Enterprise-Mobility-Management-for-your-organization)
- [Block jailbroken or rooted devices on Enterprise Grid](https://slack.com/help/articles/360042097113-Block-jailbroken-or-rooted-mobile-devices-from-accessing-Slack)
- [Understand Channel Managers in Slack](https://slack.com/help/articles/8328303095443-Understand-Channel-Managers-in-Slack)
- [Deactivate a member's account](https://slack.com/help/articles/204475027-Deactivate-a-members-account)
- [Use the Slack Connect external people dashboard](https://slack.com/help/articles/5682545991443-Use-the-Slack-Connect-external-people-dashboard)
- [conversations.list method (Slack API)](https://docs.slack.dev/reference/methods/conversations.list)

---

*생성: 2026-07-02. 원본 덤프: `Salesforce-Slack-Administrator V12.65` (212문항).*
