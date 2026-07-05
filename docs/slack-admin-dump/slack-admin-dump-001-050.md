# Salesforce Certified Slack Administrator — 덤프 검증·해설 (NO.1~50)

> **범위**: NO.1~50 (완료). 이 파일의 ⚠️ 불일치·논란 문항: **NO.3(근거 수치 정정: 72h→12h), NO.16(정답 재판정: C→B), NO.25, NO.30**.

## 면책 / 사용법

- 이 문서의 문제·보기는 **비공식 서드파티 덤프**(`Salesforce-Slack-Administrator V12.65`)에서 가져온 것이며, **개인 학습·개념 점검용**입니다. 공식 기출이 아니고 Salesforce/Slack과 무관합니다.
- **덤프 정답은 오류·모호함이 흔합니다.** 그래서 각 문항은 덤프 정답을 그대로 믿지 않고 **독립적으로 재판정**했습니다.
  - `✅ 재판정 일치` — 내 판단이 덤프 정답과 같음
  - `⚠️ 재판정 불일치/논란` — 덤프 정답이 틀렸거나 논란의 여지가 있음(내 판단과 근거를 함께 표기)
- 정답 재판정·해설은 **best-effort 검증**이며 공식 시험 정답을 보장하지 않습니다. 확신이 낮은 항목은 `(확신도: 중/낮음)`으로 표시했습니다.
- **문제·보기는 영어 원문 유지**, 해설·개념·근거는 한국어입니다. 출처는 가능한 경우 공식 Slack Help Center 문서를 인용했습니다.

---

### NO.1 — Acceptable reason to convert a public channel to private
> **Q.** You're working with other Workspace Admins to define the criteria to approve requests to convert public channels to private. What is one example of an acceptable reason to convert a public channel to private?
> - A. Members of the workspace do not wish to be notified of new content in the channel.
> - B. Channel membership is low; in the single digits.
> - C. Several members in the channel are also communicating by direct message (DM).
> - D. Channel members need to share sensitive files which should not be accessible by the wider workspace.

**핵심 개념:** 공개→비공개 전환의 정당한 사유는 오직 **기밀성/민감 정보 보호**다. 멤버 수·중복 대화·알림 취향은 전환 사유가 아니다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 민감한 파일이 더 넓은 워크스페이스에 노출되면 안 될 때, 비공개 전환으로 접근을 통제하는 것이 정당한 사유다.
**오답 해설:**
- A. 알림 수신 여부는 개인 알림 설정으로 해결할 문제이며 기밀성과 무관.
- B. 멤버 수가 적은 것은 (필요하면) 아카이브 대상일 뿐 비공개 전환 사유가 아님.
- C. 일부가 DM을 병행한다는 사실은 채널 공개범위와 무관.

**출처:** Slack Help Center — *Convert a channel to private* / *Guidelines for converting channels* (기밀 콘텐츠 통제 목적으로만 전환 권장).

---

### NO.2 — Main benefits of Workflow Builder (multiple)
> **Q.** What are the main benefits of Workflow Builder? (Choose all that apply.)
> - A. It supports integration with various third-party apps for easy data transfer between services.
> - B. Non-developers can easily automate business processes.
> - C. Templates are available for download.
> - D. Developers and engineers can easily automate efficiencies in their development.

**핵심 개념:** Workflow Builder는 **코드 없이 비개발자가 업무를 자동화**하는 노코드 도구. 앱/서비스 연동 스텝과 사전 제작 템플릿 제공이 핵심 이점.
**덤프 정답:** A B C → ✅ 재판정 일치 *(다만 '주요 이점'을 묻는 다소 주관적인 문항 — 확신도: 중)*
**정답 근거:**
- A. 앱/서비스 연동 스텝으로 서비스 간 데이터 이동을 지원.
- B. 비개발자가 코드 없이 반복 업무를 자동화 — WFB의 핵심 가치.
- C. 갤러리에서 바로 쓸 수 있는 사전 제작 템플릿 제공.

**오답 해설:**
- D. 함정 보기. 개발자도 WFB를 쓸 수 있지만, WFB는 **비개발자용**으로 포지셔닝되며 개발자는 보통 커스텀 앱/Slack API를 선호. '주요 이점'으로 꼽히지 않음.

**출처:** Slack Help Center — *Guide to Workflow Builder* / *Create a workflow in Slack*.

---

### NO.3 — Users signed out after EMM activation
> **Q.** You're an Org Admin at a company that recently rolled out Enterprise Mobility Management (EMM) to its employees. You start receiving reports that users are being signed out of Slack unexpectedly after EMM activation. What is the most likely cause of the sign out?
> - A. The users need to update their device operating systems.
> - B. The members did not set up EMM within the 72-hour window.
> - C. EMM requires users to sign in every 72 hours to ensure compliance.
> - D. When activating EMM, you did not enable "Keep users signed in."

**핵심 개념:** EMM 활성화 후 멤버는 **정해진 기한 내에 기기에서 EMM 설정을 완료**해야 하며, 완료하지 못하면 모바일 Slack에서 **자동 로그아웃**된다. ⚠️ 공식 문서상 기한은 **12시간**이며, 보기 B·C의 "72-hour"는 덤프의 오기다(실제 Slack 문서에 "72시간"이라는 수치는 없음).
**덤프 정답:** B → ✅ 재판정 일치(정답 문자는 B) *(단, 보기의 '72시간'은 부정확 — 실제는 12시간. 확신도: 높음)*
**정답 근거(B):** Slack 공식 문서: "Members will have **12 hours** to set up EMM for Slack on their device. If a member does not complete the EMM setup, they will be signed out of Slack on their mobile devices." 로그아웃 원인은 '기한 내 EMM 설정 미완료'이며, 보기 B는 이 개념(설정 미완료 → 로그아웃)을 담고 있어 4개 중 최선이다. 다만 B가 명시한 '72시간'은 덤프의 오기이고 실제 기한은 **12시간**이다.
**오답 해설:**
- A. OS 업데이트는 EMM 설정/로그인 필수 조건이 아님.
- C. EMM은 일정 주기(72시간)마다 재로그인을 '강제'하는 방식이 아니다. 실제 메커니즘은 **최초 설정 완료 기한(12시간) 내 미완료 시 로그아웃**이며, '주기적 재인증 강제'라는 프레이밍 자체가 틀림.
- D. "Keep users signed in"은 세션 유지 관련 별개 설정으로, EMM 설정 미완료로 인한 로그아웃의 원인이 아님.

**출처:** Slack Help Center — [Enable Enterprise Mobility Management for your organization](https://slack.com/help/articles/115002579426-Enable-Enterprise-Mobility-Management-for-your-organization) (현재 문서: "EMM을 켜면 정규 Slack 앱에서 **within 12 hours** 내 로그아웃"). "12 hours to set up EMM … signed out" 문구는 [Install Enterprise Mobility Management](https://slack.com/help/articles/115002247686-Install-Enterprise-Mobility-Management) 구버전에 있었음(현재는 Intune 중심으로 개편). **어느 공식 페이지에서도 '72시간' 수치는 확인되지 않음.**

---

### NO.4 — Deactivate a departing Workspace Admin (SCIM)
> **Q.** You're an Org Admin for your company's Slack Enterprise Grid org. Your organization uses an identity provider (IdP) with SCIM provisioning. Today is the last day of employment for a manager at your company who is a Workspace Admin. What is the best strategy to ensure the account is no longer active after this Workspace Admin's departure? (Select the best answer.)
> - A. Deactivate the departing Workspace Admin from all Enterprise Grid workspaces from each workspace's Manage Members page.
> - B. Deactivate the Workspace Admin's account in the IdP, and automatically sync deactivated members from your organization's IdP.
> - C. Manually delete the departing Workspace Admin from your organization's IdP.
> - D. Request an Org Owner deactivate the departing Workspace Admin from the Org Admin dashboard.

**핵심 개념:** SCIM 프로비저닝이 있으면 **IdP가 단일 진실 공급원(source of truth)**. IdP에서 비활성화하면 SCIM 동기화로 Slack 계정도 자동 비활성화된다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** IdP에서 사용자를 비활성화하면 SCIM 동기화로 Slack 전 워크스페이스에서 즉시·일관되게 비활성화된다. Slack 내 수동 작업이 불필요.
**오답 해설:**
- A. 워크스페이스별 수동 비활성화 — SCIM이 있는데 비효율적이고 누락 위험.
- C. IdP에서 '삭제'는 감사·복구 관점에서 부적절하며, 권장 동작은 '비활성화(deactivate)'.
- D. Org Owner 수동 작업에 의존 — 자동 동기화가 있는데 불필요한 수작업.

**출처:** Slack Help Center — *Manage members with SCIM provisioning* / SCIM lifecycle management.

---

### NO.5 — Org-wide channel vs multi-workspace channel
> **Q.** Takeshi is an Org Admin on Enterprise Grid. A business leader asks him to create an org-wide channel for a cross-functional company project, but he replies that he needs to create a cross-workspace channel instead. Which of the following best describes why a multi-workspace channel is more appropriate than an org-wide channel in this scenario?
> - A. There is a limit of ten org-wide channels, and this project would not necessitate creating one.
> - B. Org-wide channels are created by default when Slack is first implemented and cannot be reconfigured afterwards.
> - C. Org-wide channels are discoverable by all workspaces in the same Grid org and should only be used for information that applies to all employees.
> - D. Multi-workspace channels can be archived at the end of the project, but org-wide channels cannot.

**핵심 개념:** **Org-wide 채널**은 조직 전체(모든 워크스페이스)에 공유·노출되어 전사 공지용. 특정 참여자만 필요한 프로젝트에는 **멀티워크스페이스 채널**이 적합.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** Org-wide 채널은 그리드 조직의 모든 워크스페이스에 자동 공유되어 전 직원 대상 정보에만 써야 한다. 부서 간 프로젝트는 특정 참여자만 필요하므로 멀티워크스페이스 채널이 더 유연·적절.
**오답 해설:**
- A. "org-wide 채널 10개 제한" 같은 규칙은 없음(허구).
- B. org-wide 채널이 최초 구현 시 기본 생성되고 재구성 불가하다는 것은 사실이 아님.
- D. 두 유형 모두 아카이브 가능 — 아카이브 가능 여부가 선택 근거가 아님.

**출처:** Slack Help Center — *Create an org-wide channel* / *Understand channels in Enterprise Grid*.

---

### NO.6 — Legal export of a Slack Connect channel
> **Q.** You're an Org Owner on a Slack Enterprise Grid plan. Due to a legal issue, you need to export all messages and files from a Slack Connect channel. What is the best way to do this? (Select the best answer.)
> - A. Use the Discovery API to export all messages and files from the channel.
> - B. Use the Audit Logs API to monitor and report on all messages and files from the channel.
> - C. Use Slack's Import/Export Data tool to export all messages from the channel, and then manually download the files.
> - D. Use the Discovery API to export messages and files from the channel that were sent by your company. Then ask the partners in the Slack Connect channel to do the same.

**핵심 개념:** Slack Connect에서는 **각 조직이 자기 데이터만 소유·수출**한다. Discovery API로는 **내 조직이 보낸 메시지/파일만** 내보낼 수 있고, 상대 조직 데이터는 해당 조직에 요청해야 한다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** Slack Connect는 다중 조직 채널이라 데이터 소유권이 분산. Discovery API는 내 조직 데이터만 수출 가능하므로, 상대 파트너에게 동일하게 자기 데이터 수출을 요청해야 전체가 확보된다.
**오답 해설:**
- A. Discovery API로 '전부(파트너 포함)' 수출은 불가 — 소유권 경계 때문.
- B. Audit Logs API는 관리 이벤트 로그용이며 메시지/파일 콘텐츠 수출 도구가 아님.
- C. Import/Export 도구는 표준 워크스페이스 데이터용이며 Slack Connect 크로스 조직 콘텐츠에 부적합.

**출처:** Slack Help Center — *How data management features apply to Slack Connect* / Discovery API 문서.

---

### NO.7 — Most efficient way to manage apps org-wide
> **Q.** As an admin, managing apps across every workspace in an Enterprise Grid org can be time- consuming. What is the most efficient way to manage apps at your organization?
> - A. Identify and restrict all apps that pose the most security risks, while automatically approving users to download any apps that don't fall within the restricted list.
> - B. Identify commonly used apps once per year, and set those to be automatically approved at the org level via whitelisting.
> - C. Require end users to rate the complexity of their apps as high, medium, or low risk before submitting an app approval request.
> - D. Create rules based on a chain of comparisons for each app request to be checked against and then approved or restricted based on the specified criteria.

**핵심 개념:** 앱 거버넌스는 **고위험 앱은 선제적으로 차단(restrict)하고 나머지는 자동 허용**해 관리자 개입을 최소화하는 것이 효율적.
**덤프 정답:** A → ✅ 재판정 일치 *(운영 '베스트 프랙티스'형 문항 — 확신도: 중)*
**정답 근거(A):** 위험 앱만 차단하고 안전한 앱은 자동 승인하면, 매 요청마다 수동 검토하지 않아도 되어 관리 부담이 가장 적다.
**오답 해설:**
- B. 연 1회 화이트리스트는 갱신 주기가 너무 느려 금세 최신성을 잃음.
- C. 사용자 자가 위험 평가는 신뢰도가 낮음.
- D. 복잡한 규칙 체인은 유지보수가 어려움.

**출처:** Slack Help Center — *Manage app approval for your workspace/org* (앱 승인·제한 정책).

---

### NO.8 — Introducing yourself to a new 12-member team
> **Q.** You will be managing a new product launch and have just been assigned a new team of 12 members. You need to introduce yourself and the project scope. What should you do? (Select the best answer.)
> - A. Create a new private channel for the project, invite the team members, and introduce yourself and the project scope.
> - B. Start a group direct message (group DM) with the members introducing yourself and the project scope.
> - C. Start a direct message (DM) with each member individually.
> - D. Create a new public channel for the project, invite the team members, and introduce yourself and the project scope.

**핵심 개념:** Slack은 **DM보다 채널, 비공개보다 공개**를 기본 권장(투명성·검색성·온보딩 용이). 민감/기밀 프로젝트가 아니면 공개 채널이 기본.
**덤프 정답:** D → ✅ 재판정 일치 *(A도 방어 가능 — 확신도: 중)*
**정답 근거(D):** 공개 프로젝트 채널은 투명성을 높이고, 이후 합류자가 맥락을 따라잡기 쉬우며, 지식이 축적된다.
**오답 해설:**
- A. 비공개 채널은 기밀 프로젝트에 적합 — 문항에 기밀 요건이 없으므로 기본은 공개. *(프로젝트가 대외비라면 A가 정답이 될 수 있음.)*
- B. 그룹 DM은 규모·기능 제약이 있어 프로젝트 협업에 부적합.
- C. 개별 DM은 온보딩에 비효율적이고 정보가 흩어짐.

**출처:** Slack Help Center — *Best practices for channels* (public-by-default, channels over DMs).

---

### NO.9 — Role for managing one workspace + inviting guests
> **Q.** Andrew is the Primary Org Owner for his company's Enterprise Grid org, which consists of three workspaces. Frank, a new member of the IT department, will be responsible for inviting guests and managing one of the three workspaces' settings. Which role should Andrew give Frank in Slack?
> - A. Member
> - B. Workspace Admin
> - C. Multi-channel Guest
> - D. Primary Org Owner

**핵심 개념:** 특정 워크스페이스의 설정 관리 + 게스트 초대는 **Workspace Admin** 역할의 범위. 조직 전체 권한(Org Admin/Owner)은 불필요.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** Workspace Admin은 지정된 워크스페이스의 설정 관리·게스트 초대/관리 등 워크스페이스 수준 관리 업무를 수행하며, 조직 전체 통제 권한은 갖지 않아 최소 권한 원칙에 부합.
**오답 해설:**
- A. Member는 관리 권한이 없음.
- C. Multi-channel Guest는 외부 게스트로 관리 권한이 없음.
- D. Primary Org Owner는 조직 전체 최상위 권한 — 과도(1명만 가능하며 위임 대상이 아님).

**출처:** Slack Help Center — *Types of roles in Enterprise Grid* / *Manage Workspace Admins*.

---

### NO.10 — Two features to streamline onboarding tool-access requests
> **Q.** You're a Workspace Admin at a real estate technology company. Your HR team asks you to simplify how new hires request access to the tools they need. This onboarding step is currently done manually through emails. Employees are then required to follow up via email to IT support, causing delays. Given all new hires have access to Slack pre-onboarding, which two Slack features would you recommend to improve these processes? (Select the TWO best answers.)
> - A. Use Workflow Builder to automatically send instructions on how to request access to new tools when new employees join the default #general channel.
> - B. Invite each new employee as a Single-Channel Guest before they join, to give them more advance time to submit tool access requests.
> - C. Use Workflow Builder to automatically post instructions on how to request access to new tools in the default #general channel once per week.
> - D. Use Workflow Builder to create a form for tool access requests, to simplify data collection and reduce wasted time going back and forth in email.

**핵심 개념:** 온보딩 자동화의 핵심은 **채널 참여 트리거로 안내를 자동 발송**하고, **폼(Workflow form)으로 요청 데이터를 일관되게 수집**해 이메일 왕복을 없애는 것.
**덤프 정답:** A D → ✅ 재판정 일치
**정답 근거:**
- A. #general 참여 시점에 트리거되어 개인별·적시에 안내 — 이벤트 기반 자동화.
- D. 요청 폼으로 필요한 정보를 구조화해 수집, 이메일 왕복 제거.

**오답 해설:**
- B. 신입은 온보딩 전 이미 정식 접근 권한이 있으므로 Single-Channel Guest 초대는 무관.
- C. "주 1회 게시"는 신입 합류 시점과 어긋나 적시성이 떨어짐(트리거 기반 A보다 열등).

**출처:** Slack Help Center — *Guide to Workflow Builder* / *Create a form with Workflow Builder*.

---

### NO.11 — Centralize alerting identification and response
> **Q.** The Operations team at Fire Extinguishers Ltd has recently launched Slack and wants to better collaborate when internal alerting systems notify them of a failure. In the past, it was difficult to identify where the alert was coming from and who was responding. Sometimes, the team even missed the alerts. The Operations team and the Security team both have alerting set up with popular software tools, and the alerts get sent to multiple, unrelated teams. What should Fire Extinguishers Ltd do to centralize their alerting identification and response?
> - A. Build custom apps for all the popular tools that send the alerts to one channel.
> - B. Install apps from the Slack App Directory for the tools they use, and have the apps post alerts in a #alerts-all channel for the relevant teams to monitor.
> - C. Set up Slackbot custom responses to trigger when the word "alert" or "failure" is used in Slack.
> - D. Send an announcement to the company reminding them to be more responsive when receiving alerts.

**핵심 개념:** 검증된 **App Directory의 공식 통합 앱**을 설치해 알림을 **중앙 채널(#alerts-all)** 로 모으면 식별·대응이 일원화된다. 이미 통합이 있으면 커스텀 개발은 불필요.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 공식 앱으로 구조화된 알림을 중앙 채널에 모으면 관련 팀이 한곳에서 모니터링·대응 가능. 신뢰성·일관성·중앙집중이라는 요건을 모두 충족.
**오답 해설:**
- A. 기존 통합이 있는데 커스텀 앱을 새로 만드는 것은 불필요한 비용.
- C. Slackbot 키워드 응답은 근본적 알림 라우팅/식별 문제를 해결하지 못함.
- D. 공지 리마인더는 시스템적 문제를 해결하지 못함.

**출처:** Slack Help Center — *Add apps to Slack* / 통합 관리 베스트 프랙티스.

---

### NO.12 — Business+ launch: integrate productivity apps day one
> **Q.** You're a Workspace Owner for a Slack Business+ workspace, working with your security team to launch Slack globally. You want members to integrate Slack with their daily productivity apps from day one. What should you do?
> - A. Pre-approve daily productivity apps, and restrict apps that security has already deemed too risky.
> - B. Use an Admin API to manage and approve apps automatically.
> - C. Turn on app approvals, and have users individually request to install each app.
> - D. Pre-approve daily productivity apps, and restrict apps that are not commonly used.

**핵심 개념:** 빠른 도입과 보안의 균형 = **핵심 앱은 사전 승인, 고위험 앱은 차단**. '위험' 기준으로 제한해야지 '사용 빈도' 기준은 부적절.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 생산성 앱을 사전 승인하면 도입 속도가 빠르고, 보안이 지정한 고위험 앱을 차단해 컴플라이언스도 유지된다.
**오답 해설:**
- B. Admin API 자동화는 런칭 시점에 과도하게 기술적이고 불필요.
- C. 앱마다 개별 요청은 마찰을 유발해 "day one 도입" 목표와 배치.
- D. '흔히 쓰지 않는 앱' 차단은 위험도 기준이 아니라서 부적절 — 안전하지만 덜 쓰는 앱까지 막게 됨.

**출처:** Slack Help Center — *Manage app approval* (사전 승인/제한 정책).

---

### NO.13 — Feature + plan for login security and automated provisioning (cost-mindful)
> **Q.** You are Workspace Admin of a small but fast-growing organization on Slack's Free plan. You need to improve the security of logins and automate provisioning of Slack users to save time and expedite onboarding, while being mindful of costs. Which Slack feature and plan will suit this need?
> - A. Google Workspace single sign-on (SSO) and user groups on the Slack Pro plan
> - B. Mandatory two-factor authentication (2FA) on the Slack Free plan
> - C. Mandatory SAML single sign-on (SSO) and identity provider (IdP) groups on Slack Enterprise Grid
> - D. SAML single sign-on (SSO) and identity provider (IdP) groups on the Slack Business+ plan

**핵심 개념:** **자동 프로비저닝(SCIM) + SAML SSO**를 모두 지원하는 가장 저렴한 플랜은 **Business+**. Pro는 SAML/SCIM 미지원, Enterprise Grid는 소규모엔 과도·고비용.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** Business+에서 SAML SSO(로그인 보안)와 IdP 그룹 기반 SCIM 프로비저닝(사용자 관리 자동화)을 모두 제공하며, 비용도 Enterprise Grid보다 합리적.
**오답 해설:**
- A. Pro의 Google SSO는 SAML/SCIM 자동 프로비저닝을 제공하지 않아 요건 미충족.
- B. 2FA는 좋은 보안이지만 프로비저닝 자동화가 아님.
- C. Enterprise Grid는 요건은 충족하나 소규모 조직엔 과도·고비용("cost-mindful" 위배).

**출처:** Slack Help Center — *Slack plans and features* / *Configure SAML SSO* / *Manage members with SCIM*.

---

### NO.14 — HR sensitive communications (HR has its own workspace)
> **Q.** Large Inc.'s HR Director wants to streamline sharing HR policy information and handling sensitive questions from hiring managers. HR has its own workspace. How should you advise the HR Director to use Slack for this use case? (Select the best answer.)
> - A. Create an org-wide public channel for recruiting and hiring, and add all hiring managers.
> - B. Create an org-wide private channel for recruiting and hiring, and add all hiring managers.
> - C. Create a private channel in the HR workspace, and add all hiring managers in the organization.
> - D. Create a public channel in the HR workspace, and add all hiring managers.

**핵심 개념:** 민감한 채용/HR 논의는 **비공개 채널**로 접근을 제한. 대상이 '채용 매니저'로 한정되므로 전사 공유형 **org-wide 채널은 부적절**.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** HR 워크스페이스 내 비공개 채널에 필요한 채용 매니저만 초대하면, 민감 정보를 통제하면서 대상 그룹에 정확히 도달한다.
**오답 해설:**
- A. 공개 채널은 민감 정보 노출 위험.
- B. org-wide(비공개라도)는 전 워크스페이스 대상 개념이라 특정 대상 그룹에 부적합.
- D. 공개 채널은 기밀성 위배.

**출처:** Slack Help Center — *Create a channel* / *Channel visibility & private channels*.

---

### NO.15 — Which plans support customizable message/file retention?
> **Q.** Which plan(s) support(s) customizable message and file retention features?
> - A. Pro, Business+, and Enterprise Grid
> - B. Business+ and Enterprise Grid
> - C. Free, Pro, Business+, and Enterprise Grid
> - D. Enterprise Grid only

**핵심 개념:** **커스텀(임의 기간) 리텐션 설정은 유료 플랜(Pro·Business+·Enterprise Grid) 전용.** Free 플랜은 프리셋 2종(1년 보관 / 90일 후 삭제)만 있고 임의 기간 지정은 불가.
**덤프 정답:** A → ✅ 재판정 일치 *(공식 문서로 확인, 확신도: 높음)*
**정답 근거(A):** Slack 문서상 유료 플랜(Pro·Business+·Enterprise)은 커스텀 기간 리텐션이 가능하다. 문서 산문에 "delete data after a set amount of time"라는 표현이 있고, 실제 UI 옵션명은 **"Choose custom timeline"**이다. Pro도 'Pro and Business+ plans' 탭에 포함돼 지원하므로 B("Business+·Enterprise만")는 오답. Free는 90일/1년 프리셋뿐이라 커스텀 기간 옵션이 없다.
**오답 해설:**
- B. Pro도 커스텀 리텐션을 지원하므로 Pro를 뺀 B는 오답.
- C. Free를 포함하면 오답 — Free는 프리셋 2종뿐이라 '커스터마이즈' 대상이 아님.
- D. Pro·Business+도 지원하므로 "Enterprise Grid only"는 오답.

**출처:** Slack Help Center — [Customize data retention in Slack](https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack).

---

### NO.16 — Data types uniquely stored in a data residency region
> **Q.** Your organization enabled data residency and chose to host your organization's data in the Montreal, Canada region. Which specific data types will be uniquely stored in this geographic region? (Select the best answer.)
> - A. Messages, files, snippets, workspaces and channel membership information
> - B. Messages, files, snippets, posts and files
> - C. Messages, files, snippets, posts and member profiles
> - D. Messages, files, data used for analytics, snippets and posts

**핵심 개념:** 데이터 레지던시가 **리전 내 저장**하는 것은 **사용자 생성 콘텐츠**뿐이다. 공식 문서 *"Data stored in the data region"*: **Messages·canvases·snippets / 업로드된 파일 / 앱·봇 생성 메시지·파일**. 반대로 *"Data stored outside the data region"*(리전 외/글로벌): **Slack member profiles, Workspace and channel membership information, analytics용 데이터(sanitized logs 등)**.
**덤프 정답:** C → ⚠️ 재판정 불일치 (내 판단: **B**) *(공식 문서로 확인. 단 문항 자체가 조악 — 확신도: 중, 시험 의도는 C일 수도)*
**정답 근거:** C는 **"member profiles"** 를 포함하는데, 공식 문서는 member profiles를 **'리전 외 저장'으로 명시**한다 → C에는 리전 외 항목이 섞여 부정확. 보기 4개 중 **모든 항목이 '리전 내' 범주에 드는 것은 B뿐**(messages·files·snippets·posts — posts는 현재 canvases로 흡수된 사용자 콘텐츠). 다만 B는 "…posts and **files**"로 files를 중복 표기해 구성이 조악하다. 그럼에도 리전 외 항목이 섞인 A·C·D보다 문서적으로 우월하다.
**오답 해설:**
- A. "workspaces and channel membership information"은 공식 문서상 **리전 외 저장** — 오답.
- C. "member profiles"는 공식 문서상 **리전 외 저장** — 덤프가 고른 답이지만 이 항목 때문에 문서와 어긋남.
- D. "data used for analytics"는 공식 문서상 **리전 외/글로벌 처리** — 명백한 오답.

**출처:** Slack Help Center — [Data residency for Slack](https://slack.com/help/articles/360035633934-Data-residency-for-Slack).

---

### NO.17 — Efficient process for new workspace requests/approvals
> **Q.** You're an Org Admin who recently joined an organization with multiple workspaces, many of which were redundant. You now need to create a process that will efficiently allow for new workspace requests and approvals. What should you do?
> - A. Enable workspace creation requests via Org Settings.
> - B. Post the requirements in the #general channel so members can see them.
> - C. Inform users that if they want a new workspace they should reach out to you via DM.
> - D. Create a workflow in the #help-admins channel that requires users to provide justification.

**핵심 개념:** Enterprise Grid에는 **Org Settings의 '워크스페이스 생성 요청/승인' 기능이 내장**되어 있어, 요청→승인 흐름을 표준화·추적할 수 있다.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** Org Owner/Admin이 Org Settings에서 워크스페이스 생성 요청을 활성화하면, 통제된 표준 승인 절차가 만들어진다(내장 기능).
**오답 해설:**
- B. #general 게시는 통제/추적 가능한 절차가 아님.
- C. DM 요청은 비공식·추적 불가.
- D. 워크플로우도 도움은 되지만, 목적에 맞는 내장 기능(A)이 있어 더 효율적·표준적.

**출처:** Slack Help Center — *Manage workspace creation on Enterprise Grid*.

---

### NO.18 — Metric to measure transparency over a year
> **Q.** You're an Org Owner at a 10,000-person company that uses Slack across the organization. In a recent feedback survey, employees have expressed frustrations about silos, lack of transparency, and difficulty locating information. IT leadership asks you to provide metrics that can be tracked over the course of the next year to measure progress toward increasing transparency. What type of data would you recommend the team track? (Select the best answer.)
> - A. Number of weekly active members (active in the last 7 days).
> - B. Percentage of messages viewed in public channels vs. in private channels and DMs.
> - C. Number of multi-workspace channels across the organization.
> - D. Percentage of message engagement in org-wide announcements channels in the last six months.

**핵심 개념:** 투명성 지표의 핵심은 **공개 채널 대 비공개(사적 채널·DM) 메시지 비중**. 공개 활동 비중이 오를수록 조직 투명성이 높아진다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 공개 vs 비공개 메시지 비율은 투명성을 직접적으로 측정하는 지표. 비율 상승이 곧 투명성 개선을 뜻한다.
**오답 해설:**
- A. 주간 활성 멤버 수는 참여도/활성도 지표이지 투명성 지표가 아님.
- C. 멀티워크스페이스 채널 수는 협업 구조 지표에 가깝고 투명성 직접 지표는 아님.
- D. 공지 채널 인게이지먼트는 특정 채널 반응일 뿐 공개/비공개 비중을 보여주지 못함.

**출처:** Slack Help Center / Slack Analytics — *Understand your analytics dashboard* (public vs private activity).

---

### NO.19 — Two steps before moving a channel between workspaces
> **Q.** You're a Workspace Admin for an organization on Slack's Enterprise Grid plan. You've been asked to move a public channel from one workspace to another within your organization. Which two steps should you take before moving the channel? (Select the TWO best answers.)
> - A. Remove all members from the channel. They will need to be added again after the channel has moved.
> - B. Confirm that you are an admin in both the origin and destination workspaces.
> - C. Confirm that the channel history has been exported.
> - D. Confirm that the Org Owner is prepared to review and approve the channel move request.
> - E. Confirm that all channel members are members of the destination workspace.

**핵심 개념:** 채널 이동 전제 조건은 **① 원본·대상 워크스페이스 양쪽에서 관리자 권한 보유, ② 모든 채널 멤버가 대상 워크스페이스의 멤버일 것**.
**덤프 정답:** B E → ✅ 재판정 일치
**정답 근거:**
- B. 이동을 수행하려면 출발지·목적지 두 워크스페이스 모두에서 관리자여야 한다.
- E. 이동 시 멤버십 유지를 위해 채널 멤버가 대상 워크스페이스 소속이어야 한다.

**오답 해설:**
- A. 멤버 전원 제거는 불필요하며 오히려 멤버십을 유지해야 함.
- C. 히스토리 수출은 채널 이동 절차와 무관.
- D. Org Owner 승인은 조직 커스텀 정책이 없는 한 필수 아님.

**출처:** Slack Help Center — *Move a channel to a different workspace* (Enterprise Grid).

---

### NO.20 — What Channel Managers can do
> **Q.** What actions can Channel Managers take on channels they are assigned?
> - A. Convert channels from public to private / Rename or archive channels / Add and manage other Channel Managers
> - B. Convert channels from public to private / Restore a deleted channel / Access audit logs in Slack
> - C. Add, remove, and edit user roles / Rename or archive channels / Add and manage other Channel Managers
> - D. Convert channels from public to private / Restore a deleted channel / Add and manage other Channel Managers

**핵심 개념:** Channel Manager는 담당 채널에 대해 **이름 변경·아카이브, 공개→비공개 전환(비공개 생성 권한 보유 시), 다른 Channel Manager 추가/관리**가 가능. 단, **삭제 채널 복원·감사 로그 접근·조직 사용자 역할 편집은 불가**(관리자 영역).
**덤프 정답:** A → ✅ 재판정 일치 *(공식 문서로 확인, 확신도: 높음)*
**정답 근거(A):** 공식 문서상 Channel Manager는 이름 변경·아카이브, 공개→비공개 전환(비공개 채널 생성 권한 필요), 채널 게시 권한 조정, 다른 Channel Manager 관리 등을 수행.
**오답 해설:**
- B. "Restore a deleted channel"·"Access audit logs"는 Channel Manager 권한이 아님(관리자 영역).
- C. "Add, remove, edit user roles"는 워크스페이스/조직 관리자 권한이며 Channel Manager 범위 밖.
- D. "Restore a deleted channel"이 포함되어 오답.

**출처:** Slack Help Center — [Understand Channel Managers in Slack](https://slack.com/help/articles/8328303095443-Understand-Channel-Managers-in-Slack).

---

### NO.21 — Best way to create users when launching Enterprise Grid
> **Q.** Your organization is choosing an identity provider (IdP) and preparing to launch Slack Enterprise Grid. You want users to start working in Slack as soon as possible. What is the best way to create new users so they can start working on your Enterprise Grid?
> - A. Add all new users to your Enterprise Grid as guests, so their sign-in process is not disrupted after you choose an IdP and configure SSO.
> - B. Use Slack's built-in authentication (email + Slack password).
> - C. Downgrade your Slack plan to Business+ and turn off SSO.
> - D. Choose and configure your IdP before configuring SSO, since end users can't sign in to Enterprise Grid without SSO.

**핵심 개념:** Enterprise Grid는 **IdP/SSO 기반 인증이 전제**. 사용자가 로그인하려면 SSO가 먼저 구성돼 있어야 한다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** IdP 선택·구성 후 SSO를 설정해야 멤버가 정상 로그인할 수 있다. 인증 기반을 먼저 갖추는 것이 순서.
**오답 해설:**
- A. 전원을 게스트로 추가하는 것은 정식 멤버 프로비저닝이 아니며 이후 큰 혼란.
- B. 내장 인증(이메일+비번)은 Grid의 SSO 필수 모델과 배치.
- C. Business+로 다운그레이드는 Grid 배포 목적 자체를 무력화.

**출처:** Slack Help Center — *Manage SSO / Configure SAML SSO for Enterprise Grid*.

---

### NO.22 — Urgent notification across timezones in a connected channel
> **Q.** You are a Workspace Owner and the product manager for a snowboard manufacturing company based in Vancouver, Canada. As product manager for the company's RebelX line, you are responsible for all aspects of production, including managing your supplier relationships. You have a connected channel called #supplierbindings with one of your suppliers based in Osaka, Japan, and you use this channel to plan shipments of bindings and manage all interactions with this supplier. Unfortunately, one of the supplier's deliveries has not arrived, and if you don't receive it by next week, your inventory and sales will be negatively affected. Because of the timezone difference, you need to notify all channel members about the delay so they are aware as soon as possible or tomorrow morning at the start of the business day. What should you do?
> - A. Send a message that includes an @channel and @here to #supplier-bindings.
> - B. Send a message that includes an @channel and @everyone to #supplier-bindings.
> - C. Send an @everyone in a message to your workspace-wide #general channel.
> - D. Direct message your key contact who belongs to the connected channel.

**핵심 개념:** `@channel`은 활성 여부와 무관하게 채널 전원에게 알림, `@here`는 현재 온라인 멤버에게만 알림. `@everyone`은 **#general 전용**이라 일반/Connect 채널에선 쓸 수 없다.
**덤프 정답:** A → ✅ 재판정 일치 *(단, @channel만으로도 충분 — 확신도: 중)*
**정답 근거(A):** 해당 채널 멤버 전체에게 도달하려면 `@channel`이 정답. 보기 중 유효한 것은 A뿐이다.
**오답 해설:**
- B. `@everyone`은 #general 전용이라 이 채널에서 무효.
- C. 공급사와의 특정 채널 이슈를 전사 #general에 @everyone으로 보내는 것은 부적절.
- D. 특정 담당자 DM은 "모든 채널 멤버 통지" 요구를 충족하지 못함.
- (참고) `@here`는 `@channel`과 함께 쓰면 중복이지만, 보기 선택에는 영향 없음.

**출처:** Slack Help Center — *Mention someone in a message (@channel, @here, @everyone)*.

---

### NO.23 — Efficiently rename many channels (#it- → #bt-)
> **Q.** During a re-org within your organization, the IT department is renamed to Business Technology (BT). Many channels will need to change their prefixes from #it- to #bt-. The original channel creators are no longer at the organization. What is the most efficient strategy to ensure the channel prefixes are updated?
> - A. Use your preference menu to create an automatic keyword notification for IT and BT.
> - B. Promote members leading the initiative to the Channel Manager role in the key channels.
> - C. Write a script using the channels API to rename all channels with "#it-" to "#bt-" in bulk.
> - D. Join all public IT channels and request access to private channels to update settings.

**핵심 개념:** 대량·표준화 작업은 **API를 통한 일괄 처리**가 가장 효율적. (현행 Web API 메서드는 `conversations.rename`, 과거 명칭이 `channels.rename`.)
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** API로 프로그램적으로 일괄 이름 변경하면 빠르고 일관적. 생성자가 없어도 admin 토큰으로 처리 가능.
**오답 해설:**
- A. 키워드 알림은 이름을 바꾸지 못함.
- B. 채널마다 Channel Manager 지정 후 수동 변경은 느리고 오류 위험.
- D. 채널마다 참여/접근 요청은 비효율.

**출처:** Slack API — [conversations.rename](https://api.slack.com/methods/conversations.rename) (레거시 `channels.rename`).

---

### NO.24 — What to do with an inactive, closed-bug public channel
> **Q.** A few months ago, a team of developers at Blue Inc identified a new issue during testing and created a public channel called #bug-cricket to communicate about the issue. They may need to reference the history in the future. Of note, there has not been any new activity in #bug- cricket for months, and the bug case has been closed. What should the team do with #bug-cricket?
> - A. Convert to private, then archive; members retain access to files.
> - B. Archive the public channel; anyone can still browse the conversation history and messages appear in search.
> - C. Delete the channel; messages from a deleted channel are still available via search.
> - D. Remove all members, then archive; members can find messages via search but can't browse history.

**핵심 개념:** 완료됐지만 참조 가치가 있는 채널은 **아카이브**가 정답. 아카이브 채널은 검색·열람 가능하고 새 게시만 막힌다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 공개 채널을 아카이브하면 히스토리가 검색·열람 가능한 채로 보존되고 새 활동만 중단된다.
**오답 해설:**
- A. 불필요한 비공개 전환은 접근 범위를 좁혀 혼란만 유발.
- C. 채널 삭제는 대화 접근성을 잃음(삭제 메시지가 검색된다는 서술도 부정확).
- D. 멤버 전원 제거는 불필요하며 열람성을 해침.

**출처:** Slack Help Center — [Archive or delete a channel](https://slack.com/help/articles/213185307-Archive-or-delete-a-channel).

---

### NO.25 — Two actions in the External People (Slack Connect) dashboard
> **Q.** As the Org Admin of a large corporation, you've received many requests from external users connected via Slack Connect. Which TWO actions can you take within the External People Management dashboard? (Choose 2 answers.)
> - A. Remove external members from Slack Connect channels when they were invited with "Can only post" permissions.
> - B. Remove external members from Slack Connect channels when they were invited with "Can post & invite" permissions.
> - C. View all Slack Connect invitations.
> - D. Approve or deny Slack Connect requests.
> - E. View all external people connected to your org and the Slack Connect channels they belong to.

**핵심 개념:** External People 대시보드에서 Org Owner/Admin은 **외부 사용자와 소속 채널을 열람**하고 **채널에서 외부 사용자를 제거**할 수 있다. Connect 초대 열람이나 요청 승인/거부는 이 대시보드 기능이 아니다.
**덤프 정답:** B, E → ⚠️ 재판정 논란: **E는 확실, 두 번째(A/B)는 공식 문서로 확정 불가** *(확신도: 낮음 — 문항 자체가 모호)*
**정답 근거:**
- E는 확실 — 공식 문서: "Org Owners and Admins can see a list of all external people in channels hosted by your organization"이며, 이름 클릭 시 **Channels 탭**에서 소속 채널을 확인한다.
- 제거(A/B)도 대시보드 기능은 맞다 — 공식 문서: "Org Owners and Org Admins can remove external people from channels hosted by your organization." ⚠️ **그러나 문서는 제거를 초대 권한 유형("Can only post" vs "Can post & invite")과 결부하지 않는다.** A·B 모두 문서에 없는 조건을 덧붙인 것이라 **어느 쪽이 더 옳다고 가릴 근거가 없다** — 이전 판의 "A에 더 부합"은 근거 없어 **철회**한다. 문서상 유일한 조건은 "제거 옵션이 보이지 않으면 제거 불가"뿐.
- 결론: **E만 확실**하고, 두 번째 답(A/B)은 현재 공식 문서로 확정할 수 없는 **진짜 모호 문항**. 덤프의 B가 A보다 낫다고 볼 근거도 없다.

**오답 해설:**
- C. 모든 Connect '초대' 열람은 이 대시보드가 아니라 별도의 **Manage Slack Connect Invitations** 기능.
- D. Connect 요청 승인/거부도 같은 **Manage Slack Connect Invitations**(Open requests 탭)에서 처리 — 이 대시보드 기능이 아님.

**출처:** Slack Help Center — [Use the Slack Connect external people dashboard](https://slack.com/help/articles/5682545991443-Use-the-Slack-Connect-external-people-dashboard).

---

### NO.26 — Workspace access for a confidential acquisition
> **Q.** You're an Org Admin setting up a new workspace for executives collaborating on a confidential acquisition. How should you set up the workspace access setting?
> - A. By Request  · B. Open · C. Hidden · D. Invite Only

**핵심 개념:** 민감/기밀 프로젝트는 **Invite Only**로 관리자가 멤버십을 직접 통제해야 한다.
**덤프 정답:** D → ✅ 재판정 일치 *(Hidden도 병행 고려 가치 — 확신도: 중)*
**정답 근거(D):** Invite Only는 Org Admin/Workspace Owner가 초대한 사람만 참여하게 해, 공개 시점 전까지 기밀을 유지한다.
**오답 해설:**
- A. By Request는 누구나 요청 가능(가시성 노출) — 기밀엔 부적합.
- B. Open은 자유 참여로 부적절.
- C. Hidden은 워크스페이스 '이름 은닉'이라 기밀성에 도움되지만, 멤버십 통제라는 핵심 요구엔 Invite Only가 정답. (실무에선 Hidden + Invite Only 병행이 가장 안전.)

**출처:** Slack Help Center — *Manage workspace access on Enterprise Grid* (Open/By Request/Invite Only).

---

### NO.27 — Prevent unauthorized vendors contacting members via Slack Connect
> **Q.** You're an Org Owner for your organization's Slack Enterprise Grid instance. Your organization has several Slack Connect channels used to communicate with vendors, and you're concerned about unauthorized vendors contacting your members. Which setting should you enable to prevent this from happening? (Select the best answer.)
> - A. Set up custom messaging in Guidelines for using Slack Connect for approved vendors only.
> - B. Adjust Slack Connect DM settings so that only Org Admins and Org Owners can send and accept DMs from outside organizations.
> - C. Restrict Slack Connect to a specific workspace so only users with access can access your Connect channels.
> - D. Disable "Use Slack Connect with free teams" so only paid workspaces can access your Connect channels.

**핵심 개념:** 외부 접촉을 통제하려면 **누가 외부 DM을 주고받을 수 있는지**를 제한해야 한다 — Org Admin/Owner로 한정.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 외부 조직과의 DM 초대 송수신을 Org Admin/Owner로 제한하면, 미승인 벤더가 임의로 멤버에게 접촉하는 것을 차단한다.
**오답 해설:**
- A. 가이드라인 안내는 사용자에게 알릴 뿐 행위를 막지 못함.
- C. 특정 워크스페이스로 제한해도 조직 전반의 외부 DM 초대를 막지 못함.
- D. 무료팀 접근 비활성화는 '벤더 검증'과 직접 관련 없음.

**출처:** Slack Help Center — *Manage Slack Connect / Manage who can use Slack Connect DMs*.

---

### NO.28 — New member posts a project question in #general tagging everyone
> **Q.** You're a Workspace Admin for your organization's Slack instance. A new member in your workspace posts a question about a specific project in a #general channel and tags all project members. What should you ask the member to do? (Select the best answer.)
> - A. Start a group DM with project team members who may know the answer.
> - B. Start a DM to project team members individually.
> - C. Delete the message, and direct the member to the help channel.
> - D. Post the question in a channel related to the project.

**핵심 개념:** 특정 프로젝트 질문은 **관련 프로젝트 채널**에서 — 주제 집중과 이해관계자 참여를 보장. #general은 전사 공지용.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 프로젝트 채널에 올리면 관련 스테이크홀더가 모두 보고 기여할 수 있어 협업·검색성이 좋다.
**오답 해설:**
- A/B. DM은 팀 협업을 우회하고 지식이 흩어짐.
- C. 메시지 삭제는 과도하게 징벌적이며 불필요.

**출처:** Slack Help Center — *Best practices for channels*.

---

### NO.29 — ERG workspace: visible to all, leaders approve members
> **Q.** Jorge is starting an Employee Resource Group for volunteers at his company to collaborate from across different business units. This group requires a workspace that is visible to all members of his organization, so that they can volunteer to join and follow the group's progress. However, the group's leaders want the rights to approve any members before they join. Which access level should Jorge set for this workspace?
> - A. Open · B. Invite Only · C. By Request · D. Hidden

**핵심 개념:** **By Request** = 모두에게 보이지만 참여는 요청 후 관리자/소유자 승인 필요. "가시성 + 승인 통제"에 정확히 부합.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 워크스페이스가 전원에게 노출되어 자발적 참여를 유도하되, 각 요청을 리더가 승인할 수 있다.
**오답 해설:**
- A. Open은 승인 없이 자유 참여 — 승인 통제 불가.
- B. Invite Only는 초대받은 사람만 — "모두에게 보여 지원" 요구 위배.
- D. Hidden은 존재를 숨김 — 자발적 참여 유도 불가.

**출처:** Slack Help Center — *Manage workspace access (Open / By Request / Invite Only)*.

---

### NO.30 — Retention: keep important info, but a few channels ≤ 1 month
> **Q.** As a Workspace Owner on the Slack Business+ plan, you need to set message retention policies for your workspace. You'd like to keep important information in Slack so that employees can search for it, but there are a few channels with messages that you don't need to save for more than one month. How should you set up your data retention policies? (Select the best answer.)
> - A. Set global retention to one month, and adjust important channels to keep everything.
> - B. Keep the default retention settings, but set a one-month policy for channels with less important information.
> - C. Set public channels to keep all; allow members to determine private-channel retention.
> - D. Set private channels to keep everything; set public channels to one month.

**핵심 개념:** 시나리오상 **대부분은 보관(중요·검색)**, **소수 채널만 1개월**. 따라서 기본값=전체 보관(Business+ 기본)으로 두고, 그 **소수 채널에만 1개월 예외**를 거는 것이 맞다.
**덤프 정답:** A → ⚠️ 재판정 불일치 (내 판단: **B**) *(확신도: 중)*
**정답 근거(B):** 요구는 "중요 정보 보관 + *일부* 채널만 단기". 기본값(전체 보관)을 유지하고 예외로 소수 채널을 1개월로 설정하는 B가 시나리오에 정확히 맞는다.
**왜 덤프 A가 어긋나나:** A는 전역을 1개월로 낮추고 '중요' 채널을 예외로 보관 — 이는 대다수 채널을 예외로 지정해야 하는 비효율이며, "소수 채널만 단기"라는 시나리오와 반대다. (전역을 짧게 두는 것은 일반적 컴플라이언스 관행일 수 있으나, 이 문항의 조건과는 맞지 않음.)
**오답 해설:**
- C. 사적 채널 리텐션을 멤버가 정하게 하면 히스토리 공백 위험.
- D. 공개=단기/사적=보관 구성은 대부분 비즈니스 관행과 어긋남.

**출처:** Slack Help Center — [Customize data retention in Slack](https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack) (전역 정책 + 채널별 예외).

---

### NO.31 — Reduce channel sprawl / fragmentation
> **Q.** Kathleen is a Workspace Owner who leads the marketing department at a mid-sized company in Pune, India. She keeps receiving new campaigns at her desk to review and approve, but she has never heard of these initiatives. Many of her colleagues are equally confused. She has a few key public channels where she has explained to her team that marketing conversations should take place, so she wonders where her team is communicating. Upon investigation, she discovers that users are creating their own unique channels for each marketing campaign. Subsequently, important employees have been excluded, duplicate projects exist, and information is fragmented. To enhance transparency and collaboration, Kathleen emphasizes that users should discuss projects together in the agreed-upon channels, as they often involve the same people. Which settings and permissions should Kathleen change to reinforce this message?
> - A. Change channel management permission for creating private and public channels to Workspace Admins/Owners only.
> - B. Change join/leave messages so they don't show in channels.
> - C. Change the invitations permission to require Workspace Admins/Owners approval.
> - D. Change posting permission in all channels to Everyone.

**핵심 개념:** 채널 난립을 막으려면 **채널 생성 권한을 Workspace Admin/Owner로 제한**해 거버넌스를 확보한다.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 공개·비공개 채널 생성을 관리자로 제한하면 논의가 합의된 채널에 모이고 중복이 준다.
**오답 해설:**
- B. join/leave 메시지 숨김은 난립과 무관.
- C. 초대 승인은 채널 '생성' 난립을 직접 막지 못함.
- D. 게시 권한을 Everyone으로 여는 것은 오히려 통제와 반대.

**출처:** Slack Help Center — [Adjust channel management permissions](https://slack.com/help/articles/115004988303-Adjust-channel-management-permissions).

---

### NO.32 — Add outside consultants (can't self-host, security-focused, one project)
> **Q.** Your company wants to add outside consultants onto a project in Slack. They are not allowed to set up their own Slack workspace, and your company is security-focused. What is your best course of action?
> - A. Create a new workspace for external collaboration, add consultants as members.
> - B. Add consultants as Multi-Channel Guests with a six-month expiration.
> - C. Invite consultants as Multi-Channel Guests, and create a private channel for them and the project team.
> - D. Create a new channel, and add consultants as Single-Channel Guests.

**핵심 개념:** 최소 권한 원칙 — 단일 프로젝트라면 **Single-Channel Guest**(한 채널만 접근)가 가장 안전.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** Single-Channel Guest는 지정된 한 채널에만 접근해 권한을 엄격히 통제한다. 단일 프로젝트 협업에 최적.
**오답 해설:**
- A. 새 워크스페이스는 한 프로젝트엔 과도한 관리 부담.
- B/C. Multi-Channel Guest는 여러 채널 접근 → 필요 이상으로 넓고 위험.

**출처:** Slack Help Center — *Guest accounts / Single-Channel vs Multi-Channel Guests*.

---

### NO.33 — High-volume workspace requests requiring admin review
> **Q.** You're an Org Admin working on your Slack Enterprise Grid design. You expect a high volume of new workspace requests, and all requests will require admin review. What should you do to manage this process? (Select the best answer.)
> - A. Allow all users to request new workspaces, and route requests into an admin channel where admins can action them as a team.
> - B. Allow all users to request, and manually route requests to the correct admin via DM.
> - C. Turn off the request process; create a private channel and only add members you want to request.
> - D. Turn off the request process; require users to DM their workspace admin.

**핵심 개념:** 워크스페이스 생성 요청을 활성화하고 **중앙 admin 채널로 라우팅**하면 다수 요청을 팀 단위로 추적·승인할 수 있어 확장성이 좋다.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 요청을 내부 채널로 모아 여러 관리자가 함께 검토/승인 — 대량 요청에 가장 확장성 있는 방식.
**오답 해설:**
- B. 수동 DM 라우팅은 확장성이 없음.
- C/D. 요청 프로세스를 끄면 표준·추적 가능한 절차가 사라짐.

**출처:** Slack Help Center — *Manage workspace creation on Enterprise Grid* (참고: NO.17).

---

### NO.34 — Two benefits of IdP group mapping
> **Q.** You recently joined an organization that is on Slack's Enterprise Grid plan and because of your previous Slack Admin experience, you were added as a Grid Owner. You notice the organization is still managing provisioning manually, using a "just-in-time" process. At your last company, you saw the benefits of connecting identity provider (IdP) groups to Slack. Which two aspects of IdP group mapping will benefit your current organization? (Select the TWO best answers.)
> - A. Automatic additions of members in an IdP group to channels within your org.
> - B. Automatic additions and removals of members in an IdP group to workspaces within your org.
> - C. Automatic additions and removals of members to Slack Connect channels.
> - D. Member provisioning as a required step for all Org Owners.
> - E. Automatic approvals and authentications of integrations.

**핵심 개념:** IdP 그룹 매핑은 **워크스페이스/그룹 멤버십을 자동 프로비저닝·디프로비저닝**한다.
**덤프 정답:** A, B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:**
- B. IdP 그룹 소속에 따라 워크스페이스 멤버십을 자동 추가·제거.
- A. IdP 그룹을 통해 (연결된 채널/기본 채널로) 멤버를 자동 추가.

**오답 해설:**
- C. Slack Connect(외부 협업)는 IdP 그룹 매핑으로 관리하지 않음.
- D. "모든 Org Owner의 필수 단계"는 IdP 기능과 무관.
- E. 통합 승인/인증 자동화는 IdP 그룹 매핑 기능이 아님.

**출처:** Slack Help Center — *Manage provisioning / IdP group mapping* (참고: NO.37).

---

### NO.35 — Can a Workspace Owner deactivate another Workspace Owner?
> **Q.** Camdin is a Workspace Owner whose last day with the company is Friday, April 1st. Cortez, a fellow Workspace Owner, plans to deactivate Camdin's account at the end of that day. What will happen?
> - A. The account will be deactivated; Camdin is signed out immediately and can't log back in.
> - B. The account changes to "Inactive"; after 72 hours Camdin loses access.
> - C. Cortez can't deactivate it; he needs a Workspace Admin to do it.
> - D. Cortez can't deactivate Camdin's account; only the Primary Owner can deactivate a Workspace Owner.

**핵심 개념:** **일반 Workspace Owner는 다른 Owner를 비활성화할 수 없다.** Owner를 비활성화할 수 있는 것은 **Primary Owner뿐**이다. (권한 표 기준: **Workspace Admin은 멤버·게스트만**, **Workspace Owner는 멤버·게스트·Admin까지**, **Primary Owner는 Owner까지** 비활성화 가능. Primary Owner 본인은 아무도 비활성화 불가 — 먼저 소유권 이전 필요.)
**덤프 정답:** D → ✅ 재판정 일치 *(공식 문서 권한 표로 확인, 확신도: 높음)*
**정답 근거(D):** Slack "Deactivate a member's account" 문서의 권한 표에서 **"Deactivate Workspace Owners"** 행은 **Workspace Primary Owner 열에만 체크**돼 있다(Workspace Owner·Admin 열은 빈칸). 따라서 동료 Owner인 Cortez는 Camdin(다른 Owner)을 비활성화할 수 없다. ⚠️ 이 규칙은 문서에 산문 문장으로 명시된 게 아니라 **권한 표로 표현**돼 있어, 이전 판의 큰따옴표 인용문("Only the Workspace Primary Owner…")은 원문 인용이 아니라 표를 요약한 것이므로 인용부호를 뺀다.
**오답 해설:**
- A. Cortez에게 그 권한 자체가 없음.
- B. "72시간 후 비활성" 같은 지연 메커니즘은 존재하지 않음.
- C. Workspace Admin은 Owner보다 낮은 권한이라 Owner를 비활성화할 수 없음(방향이 반대).

**출처:** Slack Help Center — [Deactivate a member's account](https://slack.com/help/articles/204475027-Deactivate-a-members-account).

---

### NO.36 — Partner can't locate a Slack Connect channel
> **Q.** You're a member of a public Slack Connect channel that is being used to collaborate with members of a partner organization. You can see that one of your primary contacts at the partner organization is already a member of the channel, but they're having trouble locating the channel in their Slack instance. You send them the channel name in a direct message (DM) so that they can search it in Slack, but they still cannot locate the channel. What is the reason for this? (Select the best answer.)
> - A. The partner is not a member of the channel.
> - B. The channel is private in the partner's workspace, so they can't search it.
> - C. The partner does not have posting permissions.
> - D. The Slack Connect channel may have a different name in the partner's workspace.

**핵심 개념:** Slack Connect 채널은 **각 조직 워크스페이스마다 다른 이름**을 가질 수 있다. 검색은 자기 워크스페이스에 표시된 이름으로 해야 한다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 상대는 자기 워크스페이스에 지정된 이름으로 검색해야 하므로, 내 쪽 이름을 알려줘도 못 찾을 수 있다.
**오답 해설:**
- A. 이미 멤버라고 전제됨.
- B. 비공개여도 멤버면 검색 가능 — 원인 아님.
- C. 게시 권한과 채널 검색 가능 여부는 별개.

**출처:** Slack Help Center — *Slack Connect / Rename a Slack Connect channel*.

---

### NO.37 — Three benefits of syncing IdP groups
> **Q.** Your organization is on the Slack Enterprise Grid plan. What are three benefits of syncing identity provider (IdP) groups? (Select the THREE best answers.)
> - A. Automatically adds or removes members of an IdP group to workspaces within your org.
> - B. Makes membership for certain channels required for all members of an IdP group.
> - C. Makes membership for certain workspaces required for all members of an IdP group.
> - D. Automatically assigns system roles.
> - E. Automatically assigns approved apps to certain groups.
> - F. Automatically assigns admin roles.

**핵심 개념:** IdP 그룹 동기화는 **워크스페이스 멤버십 프로비저닝(A)**, **채널 멤버십 강제(B)**, **워크스페이스 멤버십 강제(C)** 를 자동화한다. 역할/앱 자동 할당은 아니다.
**덤프 정답:** A, B, C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:**
- A. IdP 그룹 소속에 따라 워크스페이스 멤버 자동 추가/제거.
- B. 지정 채널에 대해 IdP 그룹 멤버의 멤버십을 강제 유지.
- C. 지정 워크스페이스에 대해 IdP 그룹 멤버의 멤버십을 강제 유지.

**오답 해설:**
- D. 시스템 역할 자동 할당은 IdP 그룹 동기화 기능이 아님.
- E. 승인 앱 그룹 할당은 IdP 그룹 동기화 대상이 아님.
- F. 관리자 역할 자동 할당도 아님(역할은 별도 관리).

**출처:** Slack Help Center — *Manage provisioning / IdP group mapping*.

---

### NO.38 — Ensure new employees join their team's workspace
> **Q.** Your organization's Slack Enterprise Grid consists of dozens of workspaces with various access settings. You want to ensure that all new employees are able to join their team's respective workspace. What is the best way to set up the new employees?
> - A. HR adds new employees to workspaces; send a Slackbot "Welcome" message about other public workspaces.
> - B. Use IdP groups to assign new employees to their respective workspaces.
> - C. Managers add their employees; new employees browse other workspaces as they onboard.
> - D. Add new employees to user groups and assign the user groups to the respective workspaces.

**핵심 개념:** 워크스페이스 멤버십은 **IdP 그룹으로 자동 프로비저닝**하는 것이 정확·효율적. 사용자 그룹(user group)은 워크스페이스 멤버십을 제어하지 않는다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** IdP 그룹으로 조직 구조에 맞춰 워크스페이스에 자동 배치 — 수동 대비 오류가 적고 확장적.
**오답 해설:**
- A/C. HR·매니저 수동 추가는 오류·비효율.
- D. 사용자 그룹은 워크스페이스 내 멘션/알림용이며 워크스페이스 멤버십을 부여하지 않음.

**출처:** Slack Help Center — *Manage workspace membership with IdP groups*.

---

### NO.39 — Communicate trainings to all current AND future workspaces
> **Q.** As an Org Admin in your organization's Slack Enterprise Grid instance, you manage the existing four workspaces. Since your org is rapidly growing, you need a way to communicate upcoming trainings that are available to the entire company. What is the best action to ensure these communications are seen in each current and future workspace? (Select the best answer.)
> - A. Create an org-wide channel dedicated to company trainings.
> - B. Create a multi-workspace channel for training in each workspace.
> - C. Have each Workspace Admin post in the correct public training channel.
> - D. Create a Slack Connect channel dedicated to company trainings.

**핵심 개념:** **Org-wide 채널**은 현재·미래 모든 워크스페이스에 자동 포함되어 전사 방송에 최적.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** Org-wide 채널은 조직의 모든 멤버(현재+미래 워크스페이스)에게 자동 노출되어 별도 조율 없이 전달된다.
**오답 해설:**
- B. 멀티워크스페이스 채널은 '선택된' 워크스페이스만 포함 — 미래 워크스페이스 자동 포함 아님.
- C. 워크스페이스별 수동 게시는 조율 부담·누락.
- D. Slack Connect는 외부 협업용이라 내부 전사 공지에 부적합.

**출처:** Slack Help Center — *Create an org-wide channel*.

---

### NO.40 — Balance mobile UX and security (session duration)
> **Q.** As an admin, you want to balance the mobile user experience and security. You don't want to force users to log in too often, because it may leave them frustrated and result in lower Slack adoption and usage. What is the best solution to maintain security and ensure a positive mobile user experience?
> - A. Allow users to set their own mobile session duration.
> - B. Log all users out of mobile anytime there's a security threat.
> - C. Set a mobile session duration of 2 weeks for all mobile devices.
> - D. Allow all users to remain logged in infinitely.

**핵심 개념:** 관리자가 **적절한 모바일 세션 기간을 일괄 설정**하는 것이 보안·편의의 균형점. (특정 "2주" 값은 예시적 권장.)
**덤프 정답:** C → ✅ 재판정 일치 *(구체 기간은 예시 — 확신도: 중)*
**정답 근거(C):** 관리자가 합리적 세션 기간(예: 2주)을 설정하면 잦은 재로그인 없이 보안을 유지. 보기 중 균형을 갖춘 유일한 선택.
**오답 해설:**
- A. 사용자 자율 설정은 보안 통제를 약화.
- B. 위협 시마다 전원 로그아웃은 지나치게 파괴적.
- D. 무기한 로그인은 심각한 보안 노출.

**출처:** Slack Help Center — *Manage session duration / Mobile security for Enterprise Grid*.

---

### NO.41 — Regional help channels for a high-volume channel
> **Q.** Asher manages a global workplace and facilities team. Currently, his team receives all global requests in a channel called #help-workplace. Because the channel now receives hundreds of requests per day, the support team asks Asher if they can create regional channels to make triaging requests more manageable. How should Asher respond to this request?
> - A. Let each region create channels named after local landmarks; assign regional monitors.
> - B. Create a private channel for the team to triage requests into regions.
> - C. Create regional channels using the #help-workplace-region format; assign regional monitors.
> - D. Keep one centralized channel but require members to start posts with their region name.

**핵심 개념:** 대량 지원 채널은 **일관된 네이밍 규칙(#help-workplace-region)** 의 지역 채널로 분리해 라우팅·모니터링을 확장.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 명확·일관된 네이밍으로 지역 채널을 만들면 요청 라우팅이 쉽고 확장적이며 사용자 혼란이 적다.
**오답 해설:**
- A. 랜드마크 명명은 일관성이 없어 찾기 어려움.
- B. 사적 triage 채널은 지역 라우팅 자체를 해결하지 못함.
- D. 단일 채널 유지는 애초의 대량 문제를 그대로 둠.

**출처:** Slack Help Center — *Best practices for channel naming / support channels*.

---

### NO.42 — Students as members, faculty as Workspace Admins (efficient)
> **Q.** You're the Primary Org Owner for your university's Slack Enterprise Grid. You're responsible for launching Slack to first-year students and faculty members. What is the most efficient way to set up students as full members and faculty members as Workspace Admins? (Select the best answer.)
> - A. SCIM provisioning; then update profile fields to reflect titles via SCIM API.
> - B. SCIM provisioning; create an IdP group for faculty; then promote the IdP group in bulk to Workspace Admins.
> - C. Just-in-time provisioning; then promote each faculty member to Workspace Admin.
> - D. JIT or SCIM to invite; then create a user group of faculty and promote that user group in bulk to Workspace Admins.

**핵심 개념:** **SCIM 프로비저닝 + IdP 그룹 매핑**으로 대량 온보딩과 **역할(관리자) 일괄 부여**를 자동화하는 것이 가장 효율적.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** SCIM으로 계정을 프로비저닝하고 교수진 IdP 그룹을 Workspace Admin으로 일괄 승격하면 역할 부여까지 자동화된다.
**오답 해설:**
- A. 프로필 필드만 갱신하고 관리자 승격은 자동화하지 못함.
- C. JIT + 개별 수동 승격은 비효율.
- D. user group은 알림 그룹이지 역할(관리자) 일괄 부여 수단으로 부적합.

**출처:** Slack Help Center — *SCIM provisioning / Assign roles with IdP groups*.

---

### NO.43 — Thoughtful channel/workspace strategy before finalizing Grid design
> **Q.** You're upgrading your organization to Slack Enterprise Grid. You want to be thoughtful about your channel and workspace strategy before finalizing your design. What should you do?
> - A. Migrate existing workspaces into Grid so employees familiarize themselves while you plan.
> - B. Survey a selection of end users to determine whether existing knowledge networks are already in place.
> - C. Review technical requirements for your SSO system for compatibility.
> - D. Develop a Champions Network of interested users to help share the design.

**핵심 개념:** 설계 확정 전에는 **사용자 설문으로 실제 협업 패턴·비공식 지식 네트워크·자연스러운 그룹핑을 파악**해야 한다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 팀이 어떻게 협업하는지 조사해 기존 지식 네트워크를 반영해야 설계가 조직 현실에 맞는다.
**오답 해설:**
- A. 설계 전 마이그레이션은 성급함.
- C. SSO 검토는 중요하나 채널/워크스페이스 구조 설계와 직접 관련 없음.
- D. Champions Network는 롤아웃에 유용하나 초기 설계 단계는 아님.

**출처:** Slack Help Center / Slack 자료 — *Plan your Enterprise Grid design*.

---

### NO.44 — Who manages the channel once the project concludes
> **Q.** A team member is managing a long-term project that involves collaborating with internal and external users via Slack. Which statement is true about users managing the channel once the project work concludes?
> - A. The team member must be promoted to Workspace Admin to manage this and future project channels.
> - B. Others must be prevented from posting so it's automatically archived due to inactivity.
> - C. The channel creator is automatically assigned the Channel Manager role and can archive the channel.
> - D. Others should set an automatic expiration timeline so the channel is auto-deleted after a date.

**핵심 개념:** **채널 생성자는 자동으로 그 채널의 Channel Manager가 되며**, 프로젝트 종료 시 아카이브 등 관리 작업을 할 수 있다.
**덤프 정답:** C → ✅ 재판정 일치 *(공식 문서로 확인, 확신도: 높음)*
**정답 근거(C):** 공식 문서: "When someone creates a channel, they're automatically assigned as the Channel Manager." Channel Manager는 아카이브가 가능.
**오답 해설:**
- A. 채널 아카이브를 위해 Workspace Admin 승격은 불필요.
- B. Slack은 비활성 자동 아카이브를 이런 방식으로 하지 않음(별도 관리자 설정은 있으나 '게시 차단으로 유도'는 아님).
- D. 채널 자동 만료/삭제 네이티브 기능은 없음.

**출처:** Slack Help Center — [Understand Channel Managers in Slack](https://slack.com/help/articles/8328303095443-Understand-Channel-Managers-in-Slack).

---

### NO.45 — Bot scope for "Send messages as @bot"
> **Q.** You're a Slack admin reviewing an approval request for an app to be used in your organization. You notice that a particular app requires permission to "Send messages as @bot." Which bot scope will need to be assigned to the app to grant the requested permission? (Select the best answer.)
> - A. chat:write · B. admin.apps:write · C. admin.conversations:read · D. chathistory

**핵심 개념:** 봇이 메시지를 보내는 스코프는 **`chat:write`**.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 높음)*
**정답 근거(A):** `chat:write`는 앱이 승인된 채널/그룹/DM에 @bot으로 메시지를 보낼 수 있게 한다.
**오답 해설:**
- B. `admin.apps:write`는 앱 관리용.
- C. `admin.conversations:read`는 관리자 수준 대화 조회.
- D. `chathistory`(정확히는 `channels:history` 등)는 메시지 히스토리 읽기용.

**출처:** Slack API — [Scopes: chat:write](https://api.slack.com/scopes/chat:write).

---

### NO.46 — Business+ with Google Workspace IdP, rule-based access
> **Q.** Slack is on the Business+ plan and currently authenticates users via username and password. Your company uses Google Workspace (formerly G Suite) as its identity provider (IdP). Your security team would like to assign specific users or groups of users access to Slack from your IdP (rule-based access). How would you configure Slack to satisfy these requirements? (Select the best answer.)
> - A. Configure Google Workspace Auth; send binding emails to connect accounts.
> - B. Set up Google Workspace SAML SSO in a new workspace.
> - C. Build a custom SAML connection to use the Google Workspace ID and apply rule-based access.
> - D. Configure Google Workspace SAML-based SSO with Slack, and send binding emails to connect existing users' accounts.

**핵심 개념:** 외부 IdP(Google Workspace) 연동은 **SAML 기반 SSO** 구성 + 기존 사용자 계정 연결용 **바인딩 이메일** 발송.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** Slack은 Google Workspace의 SAML 2.0 SSO를 기본 지원. 사용자명/비번에서 전환 시 바인딩 이메일로 기존 계정을 IdP 프로필과 연결한다.
**오답 해설:**
- A. 단순 Google Auth는 SAML 기반 규칙 접근 제어에 못 미침.
- B. 새 워크스페이스 신설은 불필요.
- C. 커스텀 SAML을 별도 구축할 필요 없음 — Slack이 기본 지원.

**출처:** Slack Help Center — *Configure SAML SSO (Google Workspace) / Send binding emails*.

---

### NO.47 — External companies join securely and scalably
> **Q.** GoodAdvertisements Inc works with several companies to support global advertising campaigns and are on a paid plan. They are preparing for a campaign launch that requires input from multiple companies. GoodAdvertisements Inc wants the ability to coordinate effectively with the companies before and during their respective launch in a private channel, but it is not clear whether the companies use paid Slack plans. The Admins at the company want to take security precautions before inviting any outside individuals into their Slack workspace. What is the best way for the Admins to have the individuals from the outside companies join the Slack workspace and ensure the process scales for future launches with other companies?
> - A. Require invitation approval via a #guest-invitation-approval channel; invite outsiders as Single-Channel Guests with expiry dates.
> - B. Same approval flow, but invite as Multi-Channel Guests with expiry dates.
> - C. Admins individually send Single-Channel Guest invitations.
> - D. Ask outside companies to upgrade to paid; share the launch channel externally and set a reminder to unshare.

**핵심 개념:** 안전·확장적 외부 협업 = **승인 워크플로우 + Single-Channel Guest(최소 권한) + 만료일**.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 승인 채널로 게스트 초대를 통제하고, 필요한 한 채널만 접근하는 Single-Channel Guest에 만료일을 설정하면 안전하고 반복 가능한 프로세스가 된다.
**오답 해설:**
- B. Multi-Channel Guest는 필요 이상으로 넓은 접근.
- C. 개별 수동 초대는 확장성 부족.
- D. 상대에게 유료 업그레이드 요구는 비현실적.

**출처:** Slack Help Center — *Guest accounts / Approve guest invitations*.

---

### NO.48 — Two strategies to increase Sales team adoption
> **Q.** The Sales team at Large Inc is having trouble figuring out the role Slack should play in their work day. The Sales team travels often and prioritizes time with customers. They don't have a lot of time to attend training. Which two of the four strategies would help increase adoption on the Sales team? (Choose two.)
> - A. Install the Salesforce app immediately, as it's the #1 integration for Sales teams.
> - B. Send a weekly email campaign for two months, warning that access will be denied after the campaign.
> - C. Run a campaign promoting the Slack mobile app so they understand the value of mobility.
> - D. Survey the Sales team to understand pain points and prioritize which apps/workflows to build.

**핵심 개념:** 도입(change management)의 핵심은 **사용자 니즈 파악(설문)** 과 **그들의 업무 방식에 맞는 솔루션 홍보(모바일)**.
**덤프 정답:** C, D → ✅ 재판정 일치
**정답 근거:**
- C. 이동이 잦은 팀에 모바일 앱 가치를 알리면 지속적 연결이 가능.
- D. 설문으로 실제 애로를 파악해 우선순위 통합/워크플로우를 정함.

**오답 해설:**
- A. 니즈 파악 없이 앱부터 설치하는 것은 효과가 불확실.
- B. "접근 차단" 위협은 Slack 권장 도입 전략에 반함.

**출처:** Slack 자료 — *Driving Slack adoption / Change management*.

---

### NO.49 — Preserve full message history (Plus plan)
> **Q.** Oleg is a Workspace Owner, and his company is on the Plus plan. Oleg's company requires all messages to be saved for the history of the workspace. He has already ensured that only Owners and Admins can delete messages. Which additional settings should be selected to maintain the message history of the workspace?
> - A. "Keep all messages but don't track revisions" for all conversations, allowing overrides.
> - B. "Keep everything" for all conversations, allowing overrides.
> - C. "Keep everything" for public/private channels and DMs, NOT allowing overrides.
> - D. "Keep all messages but don't track revisions" for all conversations, NOT allowing overrides.

**핵심 개념:** 완전한 히스토리 보존 = **모든 메시지 보존(편집·삭제 이력 포함)** + **사용자 재정의(override) 불허**. ⚠️ 보기의 "Keep everything"/"don't track revisions"는 덤프 표기이고, Slack 실제 UI 라벨은 **"Never delete messages — save edits"**(편집·삭제 추적) / **"Never delete messages — don't save edits"**(추적 안 함)이다. override 토글 실제 라벨은 **"Let workspace members override these settings"**.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** 모든 대화(공개/사적/DM)를 "Keep everything"으로 설정하고 override를 막아야 사용자가 리텐션을 바꿔 공백을 만들 수 없다.
**오답 해설:**
- A/D. "revisions 미추적"은 편집/삭제 이력을 남기지 않아 완전 보존 요건에 미흡.
- B. override 허용은 사용자가 리텐션을 바꿔 히스토리 공백을 만들 수 있음.

**출처:** Slack Help Center — [Customize data retention in Slack](https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack).

---

### NO.50 — Effective use of threads
> **Q.** When advising team members on the best practices of threading, what should you tell them is an effective way of using threads?
> - A. To use slash commands without disturbing the rest of the channel members.
> - B. To add responses such as "thank you" or "I'm looking into it" without cluttering the channel.
> - C. To make multiple discussions in the same channel easier to follow.
> - D. To ensure that others in a channel will be notified of new messages.

**핵심 개념:** 스레드의 핵심 목적은 **한 채널 안의 여러 논의를 정리해 따라가기 쉽게** 하는 것.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 스레드는 특정 메시지를 중심으로 대화를 묶어, 바쁜 채널에서 여러 논의가 동시에 진행돼도 혼란을 줄인다.
**오답 해설:**
- A. 슬래시 커맨드는 스레드의 목적이 아님.
- B. 짧은 응답을 스레드에 다는 것도 가능하나 스레드의 '주된' 목적은 아님(부차적 이점).
- D. 스레드는 기본적으로 채널 전체에 알림을 주지 않음 — 오히려 반대(단, "Also send to channel" 옵션은 별개).

**출처:** Slack Help Center — *Use threads to organize discussions*.

---

> **파일 완료: NO.1~50.** 다음 파일 `slack-admin-dump-051-100.md` 로 이어집니다.
