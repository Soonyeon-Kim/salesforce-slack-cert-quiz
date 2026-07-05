# Salesforce Certified Slack Administrator — 덤프 검증·해설 (NO.201~212)

> 문서 목적·면책·표기 규칙은 [README](./README.md) 참고. 문제·보기는 영어 원문, 해설은 한국어. `✅` 일치 / `⚠️` 불일치·논란.
> **이 파일의 ⚠️ 문항: 없음(전부 재판정 일치).**

---

### NO.201 — Slack Connect DMs disabled: can users DM the partner?
> **Q.** Your company, Alpha Corp, highly prioritizes information security. The company has just set up Slack Connect channels to work with Beta Corp. Slack Connect direct messages (DMs) are disabled at this time. Given this, your Chief Information Officer (CIO) wants to know whether your organization's users can communicate with external users from Beta Corp using Slack Connect DMs. What should you tell the CIO? (Select the best answer.)
> - A. Alpha users can DM any Beta users in the same Connect channels.
> - B. Alpha users can DM any Beta users now that the orgs are connected.
> - C. Alpha users cannot DM anyone from Beta since Slack Connect DMs are disabled.
> - D. Workspace Admins can give specific Alpha users access to DM with Beta.

**핵심 개념:** **Slack Connect DM이 비활성화**되면, 공유 채널을 함께 쓰더라도 외부 조직과 DM을 시작/수신할 수 없다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** Connect DM이 꺼져 있으면 외부 DM 자체가 불가.
**오답 해설:** A/B 공유 채널·연결만으로 DM이 되지 않음. D 개별 허용도 설정이 꺼진 상태에선 성립하지 않음.
**출처:** Slack Help Center — *Manage Slack Connect DMs*.

---

### NO.202 — Grid design approach with many suggestions
> **Q.** You're in charge of a Slack Enterprise Grid workspace design for your company. Your teammates provide dozens of suggestions about how the workspaces should be created to provide the best user experience. Which approach should you choose? (Select the best answer.)
> - A. Keep the design loosely defined so it can change over time.
> - B. Define org policies to prevent workspaces from differing from standards.
> - C. Create the minimum number of workspaces to meet users' needs, limiting context switching.
> - D. Create new workspaces instead of multi-workspace channels to reduce noise.

**핵심 개념:** **필요한 최소 수의 워크스페이스**로 설계 — 컨텍스트 전환↓, 거버넌스 단순화, 발견성↑.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 워크스페이스가 적을수록 전환·관리 부담이 줄고 정보 발견이 쉬워진다.
**오답 해설:** A 느슨한 설계는 혼란. B 정책은 중요하나 sprawl을 직접 해결 못함. D 워크스페이스 남발은 파편화 악화.
**출처:** Slack 자료 — *Workspace design principles*.

---

### NO.203 — Hard-to-find public channels & sprawl (keep quick creation)
> **Q.** You're a Slack Org Owner at Acme Inc. Several employees report that public channels are difficult to search and find. This results in channel sprawl or duplicative channels being created by employees. The Slack experience is now noisy and confusing. You need a solution to address this while still enabling members to create channels quickly. What should you do? (Select the best answer.)
> - A. Pin the Slack Etiquette Guide to a tips channel.
> - B. Post a list of org-wide public channels in announcement channels.
> - C. Create a process to request public channel creation through admins.
> - D. Create and communicate a channel naming and creation policy (structure + convention).

**핵심 개념:** 발견성·중복 문제는 **네이밍·생성 정책의 수립·공지**로 해결하되 생성 속도는 유지.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 문서화·공지된 네이밍 규칙은 admin 개입 없이도 중복을 줄이고 발견성을 높인다.
**오답 해설:** A/B 인지 제고에 그침. C admin 필수 요청은 지나치게 제한적.
**출처:** Slack Help Center — *Channel management and naming conventions*.

---

### NO.204 — Two true statements about workflows
> **Q.** Which TWO statements are true about workflows? (Choose two.)
> - A. It's impossible to create a custom workflow in fewer than five clicks.
> - B. Workspace Owners/Admins can view all published workflows created by members of their workspaces.
> - C. To see all workflows in a workspace, you must be an Owner or Admin.
> - D. Org Owners/Admins can view all workflows created in an Enterprise Grid org.

**핵심 개념:** Workspace Owner/Admin은 자기 워크스페이스의 **모든 게시된 워크플로우를 조회**하고, Grid에서는 Org Owner/Admin이 **전 워크스페이스의 워크플로우를 조회**할 수 있다.
**덤프 정답:** B, D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:** B 워크스페이스 게시 워크플로우 관리 가시성, D Grid 전역 가시성.
**오답 해설:** A 워크플로우 생성은 빠름(거짓). C 일반 멤버도 접근 가능한 워크플로우를 볼 수 있어 부정확.
**출처:** Slack Help Center — *Workflow Builder / admin controls*.

---

### NO.205 — Clean up ~1,000 channels efficiently
> **Q.** As an Org Admin of a large Enterprise, you perform an annual channel cleanup exercise that includes archiving, deleting, and moving channels to an alternative workspace based on set criteria. On average, there are around 1,000 channels that meet the criteria during this cleanup. What is the most effective way to do this?
> - A. Use Slack's channel management tools.
> - B. Utilize bulk channel lifecycle management APIs.
> - C. Take action from each channel's settings.
> - D. Request each channel owner take action.

**핵심 개념:** 1,000개 규모의 혼합 작업(아카이브·삭제·이동)은 **API 자동화**가 가장 효과적.
**덤프 정답:** B → ✅ 재판정 일치 *(A(관리자 채널 관리 도구)도 대량 아카이브/삭제엔 유효 — 확신도: 중)*
**정답 근거(B):** `conversations.archive`·`conversations.rename` 등 API로 대량 정리를 자동화.
**오답 해설:** C/D 수동·소유자 요청은 1,000개엔 비현실적. A 관리 대시보드 도구는 효율적이나 이 볼륨·혼합 작업엔 API 자동화가 더 적합.
**출처:** Slack API — *conversations.* methods / bulk channel management*.

---

### NO.206 — Surprise party planning with cross-functional friends
> **Q.** You're planning a surprise milestone birthday party for your Team Leader virtually. Currently, the planning committee consists of two direct team members, with plans to invite cross-functional friends. What should you do to facilitate the conversation? (Select the best answer.)
> - A. New public channel; add committee + friends.
> - B. Group DM with the two team members.
> - C. Thread in the existing team channel, @mention committee.
> - D. New private channel; add committee + friends.

**핵심 개념:** 기밀·서프라이즈 계획은 **비공개 채널**로 특정 인원에 한정.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** private 채널이 서프라이즈를 보호하며 인원 추가도 유연.
**오답 해설:** A 공개는 노출. B 그룹 DM은 인원 제한·비공식. C 공개 스레드는 서프라이즈에 위험.
**출처:** Slack Help Center — *Private channels for sensitive conversations*.

---

### NO.207 — Most relevant issue in a multi-workspace proposal
> **Q.** Your organization is in the process of determining its Slack Enterprise Grid design. The latest draft proposal is a multi-workspace design that includes: * Focused workspaces for each major business function, * Global and Social workspaces where all organization members will be added, * Separate workspaces for each major external partner. You need to evaluate the current proposal and communicate potential issues to the team leading the Enterprise Grid design and launch. What is the most relevant issue to communicate to the team about the challenges of the current proposal?
> - A. High risk of notification/message noise vs a single workspace.
> - B. Slack Connect security issues.
> - C. Admin control and user management challenges.
> - D. Context switching and scalability challenges.

**핵심 개념:** 워크스페이스가 지나치게 많으면 **컨텍스트 전환·확장성** 문제가 가장 두드러진다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 다중 워크스페이스는 사용자가 정보를 찾으려 잦은 전환을 하게 해 효율을 떨어뜨리고 확장성에도 부담.
**오답 해설:** C 관리·사용자 관리 복잡성도 존재하나 D가 이 설계의 핵심 이슈. (참고: '파트너별 별도 워크스페이스'는 Slack Connect로 대체하는 게 바람직하다는 점도 지적 가치.)
**출처:** Slack 자료 — *Enterprise Grid design best practices*.

---

### NO.208 — Promote communication outside DMs (retention + creation)
> **Q.** Teara is a Workspace Owner. She has discovered that projects and key decisions are being discussed via direct messages because public channel message retention settings are set to delete messages after 20 days. The decision regarding this setting was made 2 years ago, and now the setting is no longer required. Team members are experiencing difficulty creating channels. Teara is wondering if there are other settings she should review that might be contributing to the direct message conversations. Which settings and permissions should Teara change to promote increased communication outside of direct messages?
> - A. Set retention to "Keep Everything" for all channels and DMs, and allow everyone to create channels.
> - B. Announce in #general to move conversations to channels and DM Teara for channel creation.
> - C. Public retention "Keep Everything"; DM retention delete after 1 day; restrict channel creation to Owners.
> - D. Public retention "Keep Everything"; DM retention delete after 1 day; allow everyone to create channels.

**핵심 개념:** 공개 소통 촉진 = **공개 채널 보존 극대화 + DM 보존 최소화 + 채널 생성 개방**.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** 공개 채널은 "Keep Everything"으로 투명성을 살리고, DM 보존을 1일로 줄여 사일로를 억제하며, 채널 생성을 개방해 병목을 없앤다.
**오답 해설:** C 채널 생성을 Owner로 제한하면 "생성 어려움" 문제를 악화시켜 DM 의존을 강화. A 모든 대화(DM 포함) Keep Everything은 사일로 억제 취지와 어긋남. B 공지는 구조적 해결이 아님.
**출처:** Slack Help Center — *Messaging and retention policies / channel creation permissions*.

---

### NO.209 — Good candidate for EKM
> **Q.** Which of the following would most make your company a good candidate to use Slack's Enterprise Key Management (EKM)?
> - A. Employees primarily use unsecured mobile devices.
> - B. Your company frequently shares PII.
> - C. You use Azure for all key management.
> - D. Your company is in the public sector.

**핵심 개념:** **EKM은 PII/PHI/금융 등 민감 데이터를 자주 다루는** 조직에 적합(자체 키로 접근 통제·폐기).
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 민감 데이터(PII)를 다루면 자체 암호화 키 통제/폐기 능력이 가치 있음.
**오답 해설:** A 모바일 이슈(MDM). C Azure 사용만으로는 자격 아님. D 공공부문은 보안 요구를 시사할 뿐 EKM 자격과 직접 연결은 아님.
**출처:** Slack Help Center — *Enterprise Key Management (EKM)*.

---

### NO.210 — Most effective way to increase productivity (little training)
> **Q.** A company has recently implemented Slack, and many teams have started to use it instead of email. Admins want to help members be more productive in Slack without overwhelming them with too much training. Which of the below would be the most effective way to increase members' productivity in Slack?
> - A. Show how to request new apps.
> - B. Train everyone on creating integrations.
> - C. Allow social apps like Giphy.
> - D. Connect tools they already use (Google Calendar, Box) to Slack.

**핵심 개념:** 이미 쓰는 도구를 Slack에 연결하면 추가 학습 없이 즉시 가치를 체감한다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 친숙한 도구 연동이 워크플로우와 생산성을 즉시 향상시킨다.
**오답 해설:** A 앱 요청 방법은 부차적. B 통합 개발 교육은 부담. C 소셜 앱은 생산성 핵심이 아님.
**출처:** Slack Help Center — *Accelerate productivity with integrations*.

---

### NO.211 — Integration limit on the Standard (paid) plan
> **Q.** How many integrations can be installed on a workspace on the Standard plan?
> - A. 25 · B. 10 · C. Unlimited · D. 5

**핵심 개념:** 유료 플랜(Standard=Pro 이상)은 **무제한 앱 통합**. (무료 플랜만 10개 제한.)
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** Standard 이상에서는 App Directory·커스텀 앱을 제한 없이 설치 가능.
**오답 해설:** A/B/D 특정 수치는 오답 — 무료 플랜의 10개 제한과 혼동한 것.
**출처:** Slack Help Center — *Slack plans and features (app limits)*.

---

### NO.212 — Prevent sharing credit card numbers in channels
> **Q.** You're a Workspace Owner. You notice employees are breaking corporate policy by sharing business-issued credit card numbers in channel when booking their travel for an upcoming customer meeting. Your information security team identifies this as a risk. What recommendation should you make to prevent this from happening in the future? (Select the best answer.)
> - A. Integrate with a Discovery solution using Slack's Discovery API.
> - B. Use Admin APIs to create a custom script to flag credit card numbers.
> - C. Integrate with a DLP solution using Slack's Discovery API.
> - D. Use Workflow Builder to let people report policy violations.

**핵심 개념:** 민감 데이터의 채널 공유를 **선제적으로 탐지·차단**하려면 **DLP 통합**(Discovery API 기반).
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** DLP는 메시지·파일에서 카드번호 등 패턴을 탐지해 차단·경고 등 자동 조치.
**오답 해설:** A Discovery(eDiscovery) 솔루션은 보존/조사용이지 선제적 DLP 집행이 아님. B 커스텀 스크립트는 비표준·비확장. D Workflow Builder는 민감 데이터 모니터링 용도가 아님.
**출처:** Slack Help Center — *DLP integration (Discovery API)*.

---

> **파일 완료: NO.201~212. 전체 212문항 검증 완료.** 전체 요약·불일치 목록은 [README](./README.md) 참고.
