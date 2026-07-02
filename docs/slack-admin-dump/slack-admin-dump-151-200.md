# Salesforce Certified Slack Administrator — 덤프 검증·해설 (NO.151~200)

> 문서 목적·면책·표기 규칙은 [README](./README.md) 참고. 문제·보기는 영어 원문, 해설은 한국어. `✅` 일치 / `⚠️` 불일치·논란.
> **이 파일의 ⚠️ 문항: NO.163, NO.192.**

---

### NO.151 — Share a sensitive report (usually public channel)
> **Q.** A VP requested a sensitive internal report; communication usually happens in a public project channel. What should the user do?
> - A. Group DM to the VP and anyone whose info is in the report.
> - B. Create a private project channel to share the report with the VP and those included.
> - C. DM the report to the VP of HR.
> - D. Post the report in the project's public channel.

**핵심 개념:** 민감 정보는 **접근이 제한된 비공개 채널**에서 공유.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 관련 인원만 있는 private 채널이 기밀을 보호하면서 필요한 stakeholder를 포함.
**오답 해설:** A 그룹 DM은 확장·관리 어려움. C 단일 DM은 관련자 누락. D 공개 채널은 기밀 노출.
**출처:** Slack Help Center — *Sharing sensitive information / private channels*.

---

### NO.152 — Two actions to promote channels over DMs
> **Q.** Most communication happens in DMs. Two actions to promote channel usage? (Select TWO.)
> - A. Turn off channel creation so users collaborate only in existing channels.
> - B. Publish a Slack Etiquette guide that defaults to using channels.
> - C. Send a company-wide email asking members to use channels.
> - D. Ask Slack Champions to model the behavior.
> - E. Create default channels for more collaboration options.

**핵심 개념:** 문화 변화 = **에티켓 가이드(채널 우선) + Champion의 모범**.
**덤프 정답:** B, D → ✅ 재판정 일치
**정답 근거:** B 채널 우선 규범 명문화. D Champion이 행동을 모델링.
**오답 해설:** A 채널 생성 차단은 협업을 위축. C 이메일은 수동·저효과. E 기본 채널은 온보딩용(행동 변화와 별개).
**출처:** Slack 자료 — *Change management best practices*.

---

### NO.153 — App governance with audit + rationale (Business+, native)
> **Q.** Security wants app-install governance with audit tracking and rationale, using native functionality. Best approach?
> - A. Pre-approve common tools and give security the list; restrict unapproved apps.
> - B. Turn on app approval in Manage Apps, require a comment per request, add your team as App Managers, and send requests to a #plz-apps channel.
> - C. Turn on app approval; limit approval to Workspace Owners via Slackbot; notify #team-security.
> - D. Create #triage-apps and use a Workflow Builder form for name + rationale; App Managers approve from the App Directory.

**핵심 개념:** 네이티브 **앱 승인(Manage Apps)** 은 요청 기록·사유 수집·매니저 라우팅을 모두 제공.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** 앱 승인 기능으로 요청이 로깅되고 사유를 요구하며 App Manager가 중앙에서 추적·승인.
**오답 해설:** D Workflow Builder는 네이티브 승인이 있는데 불필요. A/C 감사·사유 요건 일부 누락.
**출처:** Slack Help Center — *Manage app approval / app governance*.

---

### NO.154 — Two steps to let support team build a ticket-posting workflow
> **Q.** Support team wants a workflow that posts new/urgent tickets. Which TWO steps allow them to create it?
> - A. Add support team as App Managers.
> - B. Enable a policy allowing any user role to use steps from installed apps in Workflow Builder.
> - C. Enable channel email addresses.
> - D. Enable Workflow Builder and webhooks in Workflow Builder.
> - E. Add a workflow-creation policy allowing "Everyone, except Guests" to create workflows.

**핵심 개념:** 외부 도구를 워크플로우에 통합하려면 **앱 스텝 사용 허용(B)** 과 **웹훅 활성화(D)** 가 핵심.
**덤프 정답:** B, D → ✅ 재판정 일치 *(E도 관련 — 확신도: 중)*
**정답 근거:** B 설치된 앱의 스텝 사용 허용. D Workflow Builder + 웹훅 트리거 활성화.
**오답 해설:** A App Manager는 앱 승인 권한(워크플로우 생성엔 불필요). C 채널 이메일은 무관. E 워크플로우 생성 정책도 관련되나, 이 문항의 핵심은 앱·웹훅 통합(B·D).
**출처:** Slack Help Center — *Workflow Builder with app steps & webhooks*.

---

### NO.155 — Archive all Slack data outside Slack
> **Q.** Brian needs all Slack data archived and stored outside Slack. What must he do?
> - A. Turn on Corporate exports to retrieve private data and store it elsewhere.
> - B. Contact Slack to set org-level retention to "Keep all messages."
> - C. Enable DLP and quarantine all messages/files to archive.
> - D. Use a third-party eDiscovery app to retrieve and store data in a data warehouse.

**핵심 개념:** 외부로의 지속 아카이빙은 **서드파티 eDiscovery/아카이빙 앱**으로 데이터를 끌어와 별도 저장.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** eDiscovery/아카이빙 앱이 Slack 데이터를 외부 저장소로 지속 수집.
**오답 해설:** A 수동·비연속. B 리텐션은 데이터를 Slack 내부에 보관. C DLP는 위험 관리이지 장기 외부 아카이빙 아님.
**출처:** Slack Help Center — *eDiscovery / data governance*.

---

### NO.156 — Automated app/integration approval process
> **Q.** Best approach for an automated approval process for app/integration requests?
> - A. Create conditional rules; notify requesters; create rules at both Grid and workspace level.
> - B. Create a list of trusted members; notify approvers; rules at Grid + workspace level.
> - C. Create rules based on licensing cost; notify requesters; rules at workspace level.

**핵심 개념:** 자동 승인은 **조건부 규칙 + 요청자 상태 알림 + Grid·워크스페이스 양 수준 규칙**.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(A):** 조건부 규칙으로 자동 승인/제한하고 요청자에게 상태를 알리며, 두 수준에서 규칙을 두어 유연성 확보.
**오답 해설:** B 신뢰 멤버 목록은 자동화가 아님. C 라이선스 비용 기준은 협소·위험.
**출처:** Slack Help Center — *Automate app approvals*.

---

### NO.157 — First step before creating a new workspace
> **Q.** A teammate requests a new workspace. Which action first?
> - A. Confirm channel naming conventions.
> - B. Identify progress-tracking tools.
> - C. Ensure you have an available resource to serve as a Workspace Admin.
> - D. Determine if they'll use Slack workflows.

**핵심 개념:** 새 워크스페이스 생성 전에는 **관리할 Workspace Admin을 확보**해야 한다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** 책임 Workspace Admin 없이 만든 워크스페이스는 방치·혼란 우려.
**오답 해설:** A/B/D는 이후 세부 계획 요소.
**출처:** Slack Help Center — *Workspace creation best practices*.

---

### NO.158 — Audit all guest accounts efficiently (2 workspaces)
> **Q.** Most efficient way to audit all guest accounts across two workspaces?
> - A. Gather data from each workspace's Manage Members section.
> - B. Open a ticket with Slack's Customer Experience team.
> - C. Export the data from the Members section of the org analytics dashboard.
> - D. Export via the Export Data tab in the org administration dashboard.

**핵심 개념:** 조직 전체 게스트/멤버 정보는 **Org 분석 대시보드 Members 섹션에서 수출**하는 것이 효율적.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** Org 분석에서 게스트 유형·상태·소속 워크스페이스를 포함해 수출 가능.
**오답 해설:** A 워크스페이스별 수집은 비효율. B 티켓 불필요. D Export Data는 메시지/파일 수출.
**출처:** Slack Help Center — *Org analytics / member exports*.

---

### NO.159 — Facilitate regional (LA) community conversation
> **Q.** Enable LA employees (and visitors) to discuss events/meetups/volunteering. Best way?
> - A. Group DM with the 10 LA employees.
> - B. Slack Connect channel with the 10 LA people.
> - C. Individual DMs with each of the 10.
> - D. Public channel (e.g. #social-LA) with the 10 people.

**핵심 개념:** 지역 커뮤니티는 **공개 채널**로 발견성과 참여를 높인다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 공개 채널은 관심 있는 다른 멤버(방문자 포함)도 쉽게 발견·참여.
**오답 해설:** A/C DM은 확장·발견성 없음. B Connect는 외부 협업용.
**출처:** Slack Help Center — *Community channel best practices*.

---

### NO.160 — Strongest benefit of a vision statement for end users
> **Q.** Upgrading Pro→Business+; drafting a vision. Strongest benefit of a vision statement for end users?
> - A. Understand the purpose of using Slack for their work in a new shared way.
> - B. Learn several channels they should join.
> - C. Describe their permissions vs admin permissions.
> - D. Know about newly released features.

**핵심 개념:** 비전 문구는 **왜 Slack을 쓰는지(목적)** 를 정렬시켜 전략적 이해를 준다.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 조직 워크플로우에서 Slack의 목적을 이해하게 함.
**오답 해설:** B 채널, C 권한, D 기능은 전술적 요소.
**출처:** Slack 자료 — *Change management / vision*.

---

### NO.161 — Most secure onboarding for 4,000 users (company email only)
> **Q.** Most secure option to onboard 4,000 users, restricting access to company emails?
> - A. Integrate a SAML IdP + SCIM API connector to pre-provision members.
> - B. Enable email signup for approved company emails.
> - C. Turn on JIT provisioning and distribute an invite link.
> - D. Enable admins to invite their departments.

**핵심 개념:** 대규모·보안 온보딩은 **SAML IdP + SCIM 프로비저닝**(자동 생성/비활성화, 통제).
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(A):** IdP+SCIM로 계정을 사전 프로비저닝하면 보안·통제가 가장 강하다.
**오답 해설:** B/C 이메일 가입·JIT는 통제·보안이 약함. D 수동 초대는 4,000명 규모엔 비현실적.
**출처:** Slack Help Center — *Secure provisioning (SAML + SCIM)*.

---

### NO.162 — Two questions to ask requestors during app approval
> **Q.** Two questions to ask requestors during the app approval process? (Choose 2.)
> - A. Does the app support DLP?
> - B. Are competitors using the app?
> - C. Does the app support EKM?
> - D. Does the app require a license?
> - E. What is the urgency level for the request?

**핵심 개념:** 요청자에게는 **라이선스 필요 여부(D)** 와 **긴급도(E)** 를 물어 우선순위·계획을 세운다.
**덤프 정답:** D, E → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:** D 라이선스 요구 파악, E 긴급도로 우선순위 설정.
**오답 해설:** A DLP·C EKM은 IT/보안이 평가할 기술 사항(요청자 몫 아님). B 경쟁사 사용 여부는 무관.
**출처:** Slack Help Center — *Manage app approvals*.

---

### NO.163 — Scope for conversations.list / conversations.info (public channels)
> **Q.** Which scope allows retrieving a list of all public channels and info about a public channel via conversations.list and conversations.info?
> - A. files:read · B. admin.conversations:read · C. conversations.connect:read · D. channels:read

**핵심 개념:** **`conversations.list`·`conversations.info`는 `channels:read`** 스코프를 요구한다. `admin.conversations:read`는 `admin.conversations.*` 네임스페이스 전용이다.
**덤프 정답:** B → ⚠️ 재판정 불일치 (내 판단: **D = channels:read**) *(공식 API 문서로 확인, 확신도: 높음)*
**정답 근거(D):** Slack API 문서상 `conversations.list`의 필수 스코프는 `channels:read`(및 groups/im/mpim:read). 공개 채널 목록·정보 조회에 해당하는 스코프는 D.
**왜 덤프 B가 틀렸나:** `admin.conversations:read`는 문서상 `conversations.list`의 스코프로 나열되지 않으며, `admin.conversations.*` 메서드 전용이다. 문항이 명시한 메서드(`conversations.list`/`.info`)에는 적용되지 않는다.
**오답 해설:** A files:read는 파일용. C conversations.connect:read는 Slack Connect 관련. B admin.conversations:read는 admin.conversations.* 전용.
**출처:** Slack API — [conversations.list](https://docs.slack.dev/reference/methods/conversations.list) (Bot/User scope: `channels:read`).

---

### NO.164 — Self-paced onboarding strategy
> **Q.** Onboarding that lets members self-start and learn at their own pace. Which strategy?
> - A. Workflow Builder onboarding workflow with webinars and Help Center articles.
> - B. Host a hackathon on building Slack apps.
> - C. Custom bot to pair onboarding buddies.
> - D. Host a Slack 101 live training.

**핵심 개념:** 자기주도 학습에는 **Workflow Builder로 자료(웨비나·Help Center 링크)를 담은 온보딩 워크플로우**.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 자동 온보딩 워크플로우로 자료 링크를 제공해 각자 속도로 학습.
**오답 해설:** B/D 예약 세션(자기주도 아님). C 커스텀 봇은 과한 오버헤드.
**출처:** Slack Help Center — *Onboarding with Workflow Builder*.

---

### NO.165 — Roll out Slack, keep apps updated
> **Q.** Security wants all apps kept updated. How should IT roll out Slack?
> - A. Browser-only so employees only update the browser.
> - B. Install the Slack Desktop App with automatic updates disabled.
> - C. Install the Slack Desktop App with automatic updates allowed.
> - D. Announce steps for downloading/updating the app.

**핵심 개념:** 항상 최신·보안 버전 유지는 **데스크톱 앱 배포 + 자동 업데이트 허용**.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 자동 업데이트로 최신 보안 버전을 보장.
**오답 해설:** A 브라우저만으론 부족. B 업데이트 비활성화는 위험. D 사용자 준수 의존.
**출처:** Slack Help Center — *Deployment best practices*.

---

### NO.166 — Channel visible to IT + Internal but not Contractors
> **Q.** A channel for everyone in IT and Internal workspaces but not Contractors. Best way?
> - A. Org-wide channel, exclude the Contractors workspace.
> - B. Slack Connect channel between IT and Internal.
> - C. Channel in IT workspace, invite Internal members as guests.
> - D. Multi-workspace channel between IT and Internal.

**핵심 개념:** 선택된 워크스페이스만 공유하려면 **멀티워크스페이스 채널**(IT·Internal 한정).
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 멀티워크스페이스 채널은 지정 워크스페이스 간만 공유하고 나머지는 제외.
**오답 해설:** A org-wide는 전원 포함. B Connect는 외부용. C 게스트 초대는 비효율.
**출처:** Slack Help Center — *Multi-workspace channels*.

---

### NO.167 — Grid structure minimizing disruption
> **Q.** Moving Plus→Grid without disrupting how teams communicate. Best structure?
> - A. Workspaces for each department and sub-department.
> - B. Workspaces for each product line, each as the employee's "primary."
> - C. Workspaces based on how info is shared, each employee having one "primary" (80% of time).
> - D. One workspace, each product line as a channel.

**핵심 개념:** **정보 공유 방식**으로 워크스페이스를 나누고 각자 **주 워크스페이스(80%)** 를 두면 기존 협업을 유지.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 사람들이 정보를 공유하는 방식대로 그룹핑하면 disruption 최소·협업 유지.
**오답 해설:** A 과세분. B 제품군별은 팀 협업 구조와 어긋날 수 있음. D 단일 워크스페이스는 500명·다팀엔 부적합.
**출처:** Slack 자료 — *Enterprise Grid design strategies*.

---

### NO.168 — Which requirement makes EMM the right option
> **Q.** Which requirement makes EMM the right option for mobile security?
> - A. Require a minimum app version.
> - B. Restrict access to workspaces to approved (managed) mobile devices only.
> - C. Block file downloads and message copying.
> - D. Require secondary authentication.

**핵심 개념:** **관리(승인)된 기기에서만 접근 허용**은 EMM 고유 기능.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(B):** EMM은 승인된 관리 기기로만 Slack 접근을 제한한다.
**오답 해설:** A 최소 앱 버전, C 다운로드/복사 차단, D 2차 인증은 네이티브/세션 설정으로도 가능(EMM 고유 아님).
**출처:** Slack Help Center — *Enterprise Mobility Management (EMM)*.

---

### NO.169 — Two best ways to access Slack learning materials (beginners)
> **Q.** Two best ways to help coworkers access relevant Slack learning materials? (Choose 2.)
> - A. Review the 'Slack tutorials' section of the Help Center.
> - B. Guide members to the Slack resources library on slack.com.
> - C. Complete the Slack Certified Admin program.
> - D. Watch the on-demand "How to launch Slack" webinar.
> - E. Use /feedback to submit a support request.

**핵심 개념:** 초보자에게는 **Help Center 튜토리얼**과 **Slack 리소스 라이브러리** 같은 셀프서비스 자료.
**덤프 정답:** A, B → ✅ 재판정 일치
**정답 근거:** A/B 자기주도 학습 자료.
**오답 해설:** C Certified Admin은 고급(초보용 아님). D 웨비나는 관리자용. E 피드백은 학습 자료 아님.
**출처:** Slack Help Center — *Slack tutorials / resources library*.

---

### NO.170 — Sync standardized user attributes from IdP
> **Q.** Add standardized user attributes to profiles using IdP data. Best method?
> - A. Use the Analytics API to sync to the analytics dashboard.
> - B. Use the SCIM API to sync attributes to member profiles.
> - C. Use the Custom Profile API to sync to the analytics dashboard.
> - D. Create custom profile fields for members to add manually.

**핵심 개념:** IdP의 표준 속성(부서·직함·위치)은 **SCIM API로 멤버 프로필에 동기화**.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** SCIM 프로비저닝이 IdP 속성을 Slack 프로필로 동기화.
**오답 해설:** A/C는 분석/리포팅 대상, 프로필 동기화 아님. D 수동은 자동화 아님.
**출처:** Slack Help Center — *SCIM attribute syncing*.

---

### NO.171 — Group DM needs changing membership
> **Q.** Chandler uses a group DM for a private cert program; members will rotate. What next?
> - A. Public channel + keep using group DMs for private content.
> - B. Continue the group DM and invite new members.
> - C. Start a new group DM with only new members.
> - D. Convert the group DM to a private channel, then invite new members.

**핵심 개념:** 그룹 DM은 **멤버 추가/교체가 불가** — 멤버십을 관리하려면 **private 채널로 전환**.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** private 채널로 전환하면 기밀 유지 + 멤버십 변경 관리 + 논의 중앙화가 가능.
**오답 해설:** A/B/C 그룹 DM은 멤버 추가/교체 불가.
**출처:** Slack Help Center — *Private channels vs group DMs*.

---

### NO.172 — When to claim domains
> **Q.** When should you claim your relevant domains for Enterprise Grid?
> - A. Any time; earlier workspaces are shut down automatically.
> - B. Never; Slack claims them automatically on purchase.
> - C. As soon as possible; not retroactive — workspaces created before claiming remain standalone.
> - D. Before purchasing Grid, while on the free plan.

**핵심 개념:** 도메인 클레임은 **가능한 한 빨리** — 소급 적용되지 않아, 클레임 전에 만들어진 워크스페이스는 독립적으로 남는다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** 조기 클레임으로 미관리 워크스페이스 난립을 방지.
**오답 해설:** A 자동 종료되지 않음. B 자동 클레임 안 함. D 구매 전 무료 플랜에서 하는 것이 아님.
**출처:** Slack Help Center — *Claim domains (Enterprise Grid)*.

---

### NO.173 — Two benefits of user groups
> **Q.** Two benefits of creating user groups? (Select TWO.)
> - A. Notify a group of members at once (e.g. @managers).
> - B. Set channel management permissions at the workspace level.
> - C. Set who can view workspace analytics.
> - D. Assign default channels to users when they start.
> - E. Assign default Slack app integrations to users.

**핵심 개념:** 사용자 그룹은 **@멘션 일괄 알림(A)** 과 **가입 시 기본 채널 자동 배정(D)** 을 제공.
**덤프 정답:** A, D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:** A 그룹 일괄 알림. D 그룹 지정 시 기본 채널 자동 참여로 온보딩 간소화.
**오답 해설:** B 채널 관리 권한, C 분석 권한, E 앱 통합 할당은 사용자 그룹 기능이 아님.
**출처:** Slack Help Center — *Manage user groups*.

---

### NO.174 — Make new channels' project association clear
> **Q.** Ensure it's clear which of three projects a new channel belongs to. Best way?
> - A. Install an app that auto-updates channel topics.
> - B. Ask members to include the project name in the channel description.
> - C. Create a spreadsheet mapping channels to projects, pinned in #general.
> - D. Create a naming convention per project and add them as default channel naming prefixes.

**핵심 개념:** **네이밍 규칙(접두사)** 으로 채널 목적을 한눈에 식별.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 접두사 규칙을 강제하면 생성 시점부터 프로젝트 소속이 명확.
**오답 해설:** A 앱은 불필요. B 설명 의존은 불안정. C 스프레드시트는 번거롭고 생성 시점에 안 보임.
**출처:** Slack Help Center — *Channel naming best practices*.

---

### NO.175 — Feature to archive communications for regulation
> **Q.** A bank must archive all communications for years. Which feature?
> - A. DLP · B. MDM · C. EKM · D. eDiscovery

**핵심 개념:** 규제 아카이빙·수출은 **eDiscovery** 통합.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** eDiscovery로 메시지·파일을 수집·아카이브·수출해 규제 요건 충족.
**오답 해설:** A DLP 유출 방지, B MDM 모바일, C EKM 암호화 키 — 아카이빙 자체가 아님.
**출처:** Slack Help Center — *eDiscovery integration*.

---

### NO.176 — File retention: keep deleted files discoverable (Business+)
> **Q.** All historical files (incl. deleted) must remain discoverable. Which file retention setting?
> - A. Keep all files, including deleted files.
> - B. Keep all files.
> - C. Keep all files, including deleted files, for a set number of days.
> - D. Keep all files, including all file versions.
> - E. Keep all files, only for a set number of days.

**핵심 개념:** 삭제 파일까지 발견 가능하려면 **"Keep all files including deleted files"**(Slack 실제 라벨엔 쉼표 없음; 보기는 쉼표 표기).
**덤프 정답:** A → ✅ 재판정 일치 *(공식 문서로 확인, 확신도: 높음)*
**정답 근거(A):** 문서: 이 옵션은 워크스페이스 수명 내 모든 파일을 보존하며, **수동 삭제된 파일도 exports·Discovery API로 접근** 가능. 감사·컴플라이언스 요건을 충족한다.
**오답 해설:** B 삭제 파일 보존 보장 못함. C/E "N일" 후 손실 위험. D 버전 이력(삭제 복구 아님).
**출처:** Slack Help Center — *File retention settings*.

---

### NO.177 — When Clips are most useful (async)
> **Q.** In which scenario is Clips most useful for asynchronous work?
> - A. Troubleshooting a time-sensitive issue with tier support.
> - B. A PM showing their work and asking for feedback before end of week.
> - C. A manager scheduling time to thoroughly review a product release.
> - D. A manager actively brainstorming with leadership.

**핵심 개념:** Clips는 **비동기**로 영상·화면·음성을 녹화·공유해 각자 시간에 소비.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** PM이 업데이트를 녹화해 마감 전 비동기로 피드백을 받는 상황이 적격.
**오답 해설:** A/D 실시간(Huddle 적합). C 예약 검토는 라이브 회의.
**출처:** Slack Help Center — *Create and share clips*.

---

### NO.178 — Benefit of integrating Slack with ServiceNow
> **Q.** Benefit of integrating Slack with an app like ServiceNow?
> - A. Lets third parties access your Slack data to recommend apps.
> - B. A unified view of what's happening in the app natively, without leaving Slack.
> - C. You never have to log in to the app natively.
> - D. Lets you bypass security settings.

**핵심 개념:** 앱 통합의 이점은 **Slack을 떠나지 않고 외부 앱과 상호작용·업데이트 수신**.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** ServiceNow 같은 앱을 Slack 안에서 다루고 업데이트를 받는다.
**오답 해설:** A 부정확. C 항상 로그인 불필요는 아님. D 보안은 여전히 적용.
**출처:** Slack Help Center — *App integration benefits*.

---

### NO.179 — Who can grant multi-workspace channel permissions
> **Q.** Who can give Clint multi-workspace channel permissions?
> - A. Org Owners and Org Admins decide who can manage multi-workspace channels.
> - B. Only Org Owners.
> - C. The Sales Workspace Primary Owner.
> - D. A Workspace Owner who already has the permission.

**핵심 개념:** 멀티워크스페이스 채널 관리 권한은 **Org Owner/Org Admin**이 배정한다.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(A):** Org 수준 관리자가 멀티워크스페이스 채널 생성·관리 권한을 부여.
**오답 해설:** B "Org Owner만"은 너무 좁음(Org Admin도). C/D Workspace 수준은 독립적으로 부여 불가.
**출처:** Slack Help Center — *Manage multi-workspace channels*.

---

### NO.180 — Prevent wrong posting + manage large new-hire groups
> **Q.** New hires post in announcement channels on day one; hiring is ramping. What should Nicole do?
> - A. Post a "How to use Slack" guide in all team channels.
> - B. Custom Slackbot response when "new hire" is used.
> - C. Email the guide before they start.
> - D. Use Workflow Builder to welcome teammates to channels with onboarding messages + guide links.

**핵심 개념:** 대규모 온보딩 자동화는 **Workflow Builder** — 채널 참여 시 자동 안내로 잘못된 게시를 예방.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 참여 시점에 가이드·규범을 자동 전달해 수동 모니터링 없이 확장.
**오답 해설:** A/C 인지 도움이나 자동화 아님. B Slackbot 응답은 온보딩 관리로 부적합.
**출처:** Slack Help Center — *Onboarding with Workflow Builder*.

---

### NO.181 — Fewest-privilege role to manage users and channels (Business+)
> **Q.** Fewest-privilege role for the Head of IT to manage users and channels (Business+)?
> - A. Org Admin · B. Workspace Admin · C. Workspace Owner · D. Member

**핵심 개념:** 멤버·채널·설정 관리의 최소 권한 역할은 **Workspace Admin**.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(B):** Workspace Admin은 Owner의 광범위 권한 없이 멤버·채널·설정을 관리.
**오답 해설:** A Org Admin은 Grid 역할이며 과함. C Workspace Owner는 권한이 더 큼. D Member는 관리 불가. *(참고: NO.192와 비교 — 동일 취지에서 최소 역할은 Workspace Admin.)*
**출처:** Slack Help Center — *Roles and permissions*.

---

### NO.182 — Enable Google Calendar for all members
> **Q.** Best way to enable the Google Calendar app for all members?
> - A. Post instructions in #announcements linking to the app's directory page.
> - B. Connect Google Calendar to your email domain and enable domain-wide authentication to auto-install for all users.
> - C. Pre-approve the Google Calendar integration so users can easily enable it themselves.
> - D. Use the Admin API to automate approvals.

**핵심 개념:** 전원에게 앱을 매끄럽게 제공하려면 **도메인 전체 인증(domain-wide authentication)** 으로 자동 설치·인가.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중 — 실제로는 사용자별 Google 계정 연결이 필요할 수 있음)*
**정답 근거(B):** 도메인 전체 인증을 켜면 개별 수동 설치 없이 앱이 전원에게 설치·인가된다.
**오답 해설:** A 수동·불일치. C 사전 승인은 여전히 사용자가 개별 설치. D Admin API는 요청 관리이지 매끄러운 접근 보장 아님.
**출처:** Slack Help Center — *Manage apps / domain-wide authentication*.

---

### NO.183 — Best Workspace Admin candidate
> **Q.** Which prior experience makes the best Workspace Admin candidate?
> - A. Encourages etiquette, answers Slack questions, gives feedback on settings/policies.
> - B. Creates custom integrations for onboarding.
> - C. Set up Slack Connect channels and designed the approval process.
> - D. Relies on Slack daily and frequently asks IT questions.

**핵심 개념:** Workspace Admin은 **베스트 프랙티스 이해 + 도입 지원 + 에티켓 강화 + 정책 피드백** 역량이 이상적.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 이미 Slack 사용 리더십·정책 이해·동료 지원을 보이는 후보.
**오답 해설:** B 개발자 성향. C Slack Connect 특화(일반 admin 준비는 아님). D 지원을 받는 쪽.
**출처:** Slack Help Center — *Choosing Workspace Admins*.

---

### NO.184 — Actions from scopes channels:write and chat:write:user
> **Q.** With scopes channels:write and chat:write:user, which TWO actions can the app perform? (Choose two.)
> - A. Modify public channels · B. Upload files · C. Send messages as a member · D. Access group direct messages

**핵심 개념:** `channels:write`=공개 채널 생성/아카이브/수정, `chat:write:user`=사용자로서 메시지 전송.
**덤프 정답:** A, C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거:** A 공개 채널 관리, C 사용자 명의 메시지 전송.
**오답 해설:** B 파일 업로드는 files:write 필요. D 그룹 DM 접근은 groups:read/history 등 필요.
**출처:** Slack API — *OAuth scopes (channels:write, chat:write:user)*.

---

### NO.185 — Two best practices when restricting channel creation to admins
> **Q.** After restricting channel creation to Workspace Admins, two best practices? (Choose two.)
> - A. Keep up to date on channel naming conventions to process requests accurately.
> - B. Prepare for a decrease in workload.
> - C. Create a process for channel requests.
> - D. Appoint other members to help with the workload.

**핵심 개념:** 생성 권한을 제한하면 **네이밍 규칙 숙지(A)** 와 **채널 요청 프로세스 마련(C)** 이 필요.
**덤프 정답:** A, C → ✅ 재판정 일치
**정답 근거:** A 일관된 요청 처리, C 명확한 요청 절차.
**오답 해설:** B 오히려 업무량 증가. D 생성 권한은 Admin에 한정돼야 하므로 부합하지 않음.
**출처:** Slack Help Center — *Channel management governance*.

---

### NO.186 — Consider first when deciding on a new workspace
> **Q.** New business unit has stricter security/compliance but needs to collaborate extensively. What to consider first?
> - A. Number of multi-workspace channels needed.
> - B. The unit's preference for DMs/private channels.
> - C. The data retention needs of the new business unit.
> - D. The unit's app approval requirements.

**핵심 개념:** 새 워크스페이스 판단은 **데이터 리텐션·보안·컴플라이언스 요건이 기존과 다른지**를 먼저 평가.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** 리텐션/컴플라이언스 요건이 다르면 별도 설정을 위해 워크스페이스 분리가 필요할 수 있다.
**오답 해설:** A/B/D는 부차적 고려.
**출처:** Slack 자료 — *Enterprise Grid workspace planning*.

---

### NO.187 — Action for Org Owner but not Workspace Owner
> **Q.** Which action can an Org Owner perform but not a Workspace Owner?
> - A. Set message retention policies.
> - B. Reset all members' passwords.
> - C. Manage SSO settings.
> - D. Turn on approved apps.

**핵심 개념:** **SSO 설정은 조직 전체 보안 사안으로 Org Owner의 영역**.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** 조직 전체 SSO 구성/관리는 Org Owner가 담당하고 Workspace Owner는 불가.
**오답 해설:** A 리텐션, D 앱 승인은 워크스페이스 수준 가능. B 개별 비번 리셋은 IdP로 관리(둘 다 직접 불가).
**출처:** Slack Help Center — *Roles and permissions (Enterprise Grid)*.

---

### NO.188 — Inactive channel with important content, one member
> **Q.** A channel inactive nine months with important content and one member. What to do?
> - A. Notify the member, then delete.
> - B. Notify the member, then archive.
> - C. Notify the member, keep active but limit posting to admins.
> - D. Notify the member, rename with #archived prefix.

**핵심 개념:** 중요한 콘텐츠가 있는 비활성 채널은 **아카이브**(검색 가능, 새 게시 차단).
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 아카이브로 히스토리를 보존하며 새 게시를 막는다.
**오답 해설:** A 삭제는 영구 제거. C/D 표준 정리 절차 아님.
**출처:** Slack Help Center — *Archive or delete a channel*.

---

### NO.189 — Recover data past retention (Pro, 1-year policy, 18 months ago)
> **Q.** Can you recover channel history from 18 months ago if retention was set to one year (Pro)?
> - A. Yes — Slack disaster recovery backups accessible to Org Admins.
> - B. Yes — Slack can access history upon Org Admin request due to MFA on admin access.
> - C. No — GDPR territory; Slack legally can't provide it after the retention date.
> - D. No — data is removed on retention expiration; Slack deletes it from production systems.

**핵심 개념:** 리텐션 만료 시 Slack은 **프로덕션 시스템에서 영구 삭제**하므로 복구 불가.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** 만료된 메시지는 영구 삭제되어 복구할 수 없다.
**오답 해설:** A/B 백업·MFA는 복구와 무관. C GDPR는 리텐션 요건에 영향은 있으나 복구 불가의 핵심 이유는 삭제 동작(D).
**출처:** Slack Help Center — *Message retention and deletion*.

---

### NO.190 — Main benefit of per-BU workspace design
> **Q.** Workspaces per line of business + one social; members assigned to two, can join others. Main benefit?
> - A. Workspace admin efforts distributed to representatives who know each BU's needs.
> - B. Less context switching from accessing several workspaces.
> - C. No added benefit.
> - D. Centralized admin with less policy-breach opportunity.

**핵심 개념:** BU별 워크스페이스의 이점은 **관리 책임을 각 BU 대표에게 위임**해 효율·적합성을 높이는 것.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** BU를 잘 아는 리더에게 관리를 분산하면 관리가 효율적·유관하다.
**오답 해설:** B 여러 워크스페이스는 오히려 전환 증가. C 이점 없다는 것은 오답. D "중앙집중"은 이 설계(분산)와 반대.
**출처:** Slack 자료 — *Enterprise Grid workspace architecture*.

---

### NO.191 — Update an outdated workflow
> **Q.** A published onboarding workflow is now outdated. How do you fix it?
> - A. Unpublish, modify the steps, and republish.
> - B. Download the workflow file, edit JSON, re-import.
> - C. Add a new step describing what changed.
> - D. Delete the workflow and create a new one.

**핵심 개념:** 워크플로우 수정은 **언퍼블리시 → 수정 → 재퍼블리시**.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(A):** 기존 워크플로우를 직접 편집·재게시하는 것이 표준.
**오답 해설:** B JSON 편집 불필요. C 단계 추가는 임시방편. D 삭제·재생성은 비효율.
**출처:** Slack Help Center — *Manage/edit workflows*.

---

### NO.192 — Minimum role for workspace-level actions
> **Q.** Minimum role to accomplish workspace-level actions (changing settings, managing members)?
> - A. Workspace Owner · B. Org Admin · C. Workspace Admin · D. Roles Admin

**핵심 개념:** 멤버 관리·대다수 워크스페이스 설정은 **Workspace Admin**이 수행할 수 있어, "최소 역할"은 Workspace Admin이다.
**덤프 정답:** A → ⚠️ 재판정 불일치/논란 (내 판단: **C = Workspace Admin**) *(확신도: 중)*
**정답 근거(C):** 문항 예시(설정 변경·멤버 관리)는 Workspace Admin 권한 범위다. "최소 역할"을 물었으므로 Owner보다 낮은 Admin이 정답. **NO.181**(같은 취지, 정답 Workspace Admin)과도 일관된다.
**왜 덤프 A가 어긋나나:** Workspace Owner는 필요 이상의 상위 권한. 다만 일부 소유자 전용(Owner-only) 설정까지 포함해 "설정 변경"을 해석하면 Owner가 필요하다는 논리도 가능해 '논란'으로 분류.
**오답 해설:** B Org Admin은 조직 수준. D Roles Admin은 역할 배정 전용.
**출처:** Slack Help Center — *Roles and permissions overview* (Workspace Admin: 멤버·채널·설정 관리).

---

### NO.193 — Terminated user active because IdP (Okta) is down
> **Q.** A terminated user is still active because Okta is down. Immediate steps?
> - A. Change email to a dummy and force logout.
> - B. Make #general read-only, delete offensive messages, contact the manager.
> - C. Deactivate the account in Slack settings; ask HR to notify you of updates until Okta is back.
> - D. Ask IT and the Primary Org Owner to contact Okta and Slack support.

**핵심 개념:** SCIM/IdP가 다운이면 **Slack 설정에서 수동 비활성화**해 즉시 접근을 차단.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** IdP 불가 시 수동 비활성화가 즉시 접근을 막는 정석.
**오답 해설:** A 이메일 변경은 지저분·비권장. B read-only는 접근 자체를 막지 못함. D 지원 문의는 즉각성 부족.
**출처:** Slack Help Center — *Deactivate a member's account (manual)*.

---

### NO.194 — What must be true for automatic deactivation
> **Q.** Which must be true for members to be automatically deactivated when they leave (Plus, IdP)?
> - A. Each member's access must expire after 90 days.
> - B. The member must not be a Workspace Admin or Owner.
> - C. The member must have left all channels.
> - D. The IdP must support deprovisioning via SCIM.

**핵심 개념:** 자동 비활성화는 **IdP의 SCIM 디프로비저닝 지원**이 전제.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** SCIM 디프로비저닝이 켜져 있어야 IdP의 비활성화가 Slack에 자동 반영된다.
**오답 해설:** A/B/C는 자동 비활성화 요건이 아님.
**출처:** Slack Help Center — *SCIM provisioning / deprovisioning*.

---

### NO.195 — Set the Customer Support team up for success (choose all)
> **Q.** What should you do to set the Customer Support team up for success? (Choose all that apply.)
> - A. Allow everyone on the team to approve and install apps.
> - B. Approve and install apps to integrate their support tools.
> - C. Streamline an incident management workflow.
> - D. Organize and name channels so info/procedures/policies are easy to find.

**핵심 개념:** **핵심 앱 승인·설치(B)**, **인시던트 워크플로우 정비(C)**, **채널 조직·네이밍(D)** 으로 성공을 지원.
**덤프 정답:** B, C, D → ✅ 재판정 일치
**정답 근거:** B 도구 통합, C 워크플로우 자동화, D 발견성 있는 채널 구성.
**오답 해설:** A 전원에게 앱 승인 허용은 보안 위험.
**출처:** Slack Help Center — *Set teams up for success with integrations*.

---

### NO.196 — SMEs continuously manage a custom app's settings
> **Q.** How to let developer SMEs continuously manage settings for a custom app?
> - A. A channel to submit suggested changes for Org Admin review.
> - B. Promote SMEs to Org Admin to manage the app (and all others).
> - C. Use Workflow Builder instead of a custom app.
> - D. Add the SMEs as internal app collaborators to manage the app's settings directly.

**핵심 개념:** 커스텀 앱 설정은 **내부 앱 협업자(internal app collaborators)** 로 추가해 Org Admin 권한 없이 직접 관리하게 한다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 내부 앱 협업자는 OAuth·스코프 등 앱 구성을 관리 가능(과도한 권한 부여 불필요).
**오답 해설:** A 간접적. B Org Admin 승격은 과도. C 커스텀 앱 관리를 대체 못함.
**출처:** Slack Help Center — *Manage internal apps / app collaborators*.

---

### NO.197 — True about security in Slack
> **Q.** Which is true about security in Slack?
> - A. Workspace Admins can see all DM content anytime via the Admin console.
> - B. Slack data is stored on your company's servers.
> - C. Slack data is encrypted at rest and in transit.
> - D. Members can only access Slack on the corporate network.

**핵심 개념:** Slack 데이터는 **전송 중·저장 시 모두 암호화**된다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 높음)*
**정답 근거(C):** 업계 표준 암호화로 at rest/in transit 보호.
**오답 해설:** A 관리자는 승인된 수출/eDiscovery 없이는 DM을 볼 수 없음. B 데이터는 Slack(AWS) 인프라에 저장. D 기본적으로 회사 네트워크로 제한되지 않음.
**출처:** Slack — *Security and compliance overview*.

---

### NO.198 — Mobile security for unmanaged devices
> **Q.** Which mobile security feature is available for unmanaged devices?
> - A. Block Workspace access · B. Restrict access based on IP · C. Block message copying and downloads · D. Make VPN mandatory

**핵심 개념:** 비관리 기기에는 **메시지 복사·파일 다운로드 차단**으로 콘텐츠를 보호. (cf. NO.105)
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** 비관리 기기에서 복사/다운로드를 막아 민감 데이터를 보호.
**오답 해설:** B IP 제한, D VPN 강제는 네트워크 전략(모바일 기기 보안 기능 아님). A 접근 완전 차단은 목적이 아님.
**출처:** Slack Help Center — *Mobile security features*.

---

### NO.199 — Get reports from a tool into Slack; first step
> **Q.** You need reports from an inventory tool into Slack. First thing to do?
> - A. Set up email forwarding outside Slack.
> - B. Gather a team to develop a custom Slack app.
> - C. Create a workflow using an incoming webhook.
> - D. Search the Slack App Directory for an existing app that supports the tool.

**핵심 개념:** 통합의 첫 단계는 **App Directory에서 기존 통합 앱 검색**.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 공식 앱이 이미 있으면 개발 없이 빠르고 안정적으로 배포.
**오답 해설:** A 이메일 우회는 임시방편. B 커스텀 개발은 마지막 수단. C 웹훅 워크플로우도 기존 앱 확인 후.
**출처:** Slack Help Center — *Manage app integrations*.

---

### NO.200 — CPO async product demo to the entire company
> **Q.** Most efficient async way for the CPO to share/demo a major product release to the whole company?
> - A. Record a Slack Clip in an org-wide announcements channel.
> - B. Record a demo outside Slack and import into a multi-workspace channel.
> - C. Start a Huddle in an org-wide announcements channel.
> - D. Create a public channel in the Product & Engineering workspace to share the announcement.

**핵심 개념:** 전사 비동기 공유는 **org-wide 채널의 Slack Clip**(녹화 영상, 각자 시청).
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** Clip은 비동기 녹화, org-wide 채널은 전사 도달.
**오답 해설:** C Huddle은 동기. B 외부 녹화 임포트는 비효율. D 특정 워크스페이스 공개 채널은 수동 참여 필요.
**출처:** Slack Help Center — *Clips for asynchronous communication*.

---

> **파일 완료: NO.151~200.** 다음 파일 `slack-admin-dump-201-212.md` 로 이어집니다.
