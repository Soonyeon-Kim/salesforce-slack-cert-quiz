# Salesforce Slack 자격증 예시문제 퀴즈 허브

Salesforce Slack 자격증 학습 가이드 3종의 **예시문제 130문항**을 누구나 링크로
풀어볼 수 있는 인터랙티브 퀴즈입니다. 자격증을 골라 도메인별 연습문제와 종합
모의고사를 공부모드·시험모드로 풀 수 있습니다.

👉 **퀴즈 풀기:** https://soonyeon-kim.github.io/salesforce-slack-cert-quiz/

## 수록 자격증

| 자격증 | 문항 | 합격선 | 제한시간 |
|---|---|---|---|
| Salesforce Certified Slack Developer | 47 | 67% | 75분 |
| Salesforce Certified Slack Administrator | 41 | 65% | 65분 |
| Salesforce Certified Slack Consultant | 42 | 67% | 67분 |

각 자격증은 **도메인별 연습문제 + 종합 모의고사 20문항**으로 구성됩니다.

## 구성

- 한국어 전용 · 객관식(단일/복수 선택) · 정답 및 해설 제공
- **공부모드**: 도메인 선택 + 문제 수 지정, 풀면서 즉시 정오답·해설 확인
- **시험모드**: 해당 자격증 전체 문항 랜덤 출제, 제한시간·합격선 적용
- 복수 정답 문항은 부분점수 없이 완전일치만 정답 처리

## 면책

학습 점검용 **자체 제작 예상문제**이며 공식 기출이 아닙니다. 이미 공개된 학습 가이드
자료를 기반으로 합니다. 플랜·정책 등 사실 관계는 학습 가이드의 최신 정정을 단일
출처로 반영합니다.

## 구조

```
index.html          정적 단일 페이지 (HTML+CSS+JS)
questions.json      문항 데이터 (build_questions.py로 생성)
build_questions.py  학습 가이드 content/*.md → questions.json 추출기
```

문항 데이터는 학습 가이드 3종(`slack_developer`·`slack_admin`·`slack_consultant`의
`content/*.md`)이 단일 출처입니다. 가이드가 갱신되면 모노레포 워킹트리에서
`python build_questions.py`를 재실행해 `questions.json`을 재생성합니다.
