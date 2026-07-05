# Salesforce Certified Slack Administrator — 덤프 검증·해설 (NO.101~150)

> 문서 목적·면책·표기 규칙은 [README](./README.md) 참고. 문제·보기는 영어 원문, 해설은 한국어. `✅` 일치 / `⚠️` 불일치·논란.
> **이 파일의 ⚠️ 문항: NO.105, NO.124(B 서술 문서 미확인·소거법).**
> 참고: NO.110은 NO.60, NO.113은 NO.69, NO.122는 NO.81과 사실상 동일(보기 순서만 다름).

---

### NO.101 — Two reasons to use SAML SSO
> **Q.** What are two reasons why a company would be interested in using SAML single sign-on (SSO) to authenticate its users on Slack? (Select the TWO best answers.)
> - A. More control over security policies, including password format requirements.
> - B. It replaces the need for admins to set up an IdP for Slack.
> - C. It's a standard security feature available on all of Slack's paid plans.
> - D. Employees can use the same login credentials they already use for other applications.
> - E. It lets your org control the encryption keys to users' data.

**핵심 개념:** SAML SSO는 **IdP를 통해 인증 정책(비밀번호 규칙·세션 등)을 통제**하고 **기존 자격증명으로 단일 로그인**을 제공한다.
**덤프 정답:** A, D → ✅ 재판정 일치
**정답 근거:** A 인증/보안 정책을 조직이 통제. D 다른 앱과 동일 자격증명으로 로그인.
**오답 해설:** B SSO는 IdP가 있어야 성립(대체 아님). C 모든 유료 플랜이 아님(Business+ 이상). E 암호화 키 통제는 EKM.
**출처:** Slack Help Center — *Single sign-on (SSO) overview*.

---

### NO.102 — Two benefits of SCIM provisioning
> **Q.** Your company is on the Slack Business+ plan and is interested in setting up SCIM provisioning in their identity provider (IdP) to more efficiently manage their Slack user base. Which two benefits would the company gain from using SCIM provisioning? (Select the TWO best answers.)
> - A. Automatically deactivate users from their IdP.
> - B. Users remember one set of credentials for all apps.
> - C. Sync custom profile fields for better analytics.
> - D. No pre-provisioning; accounts auto-create on first login.
> - E. Pre-provision Multi-Channel and Single-Channel Guests.

**핵심 개념:** SCIM는 **IdP 기반 계정 자동 비활성화**와 **게스트 사전 프로비저닝**을 제공(인증이 아닌 프로비저닝).
**덤프 정답:** A, E → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:** A IdP 비활성화 → Slack 계정 자동 비활성화. E Multi/Single-Channel Guest 사전 프로비저닝.
**오답 해설:** B는 SSO(인증). D는 JIT 프로비저닝(SCIM 아님). C "분석용 프로필 동기화"는 SCIM 핵심 이점이 아님.
**출처:** Slack Help Center — *Manage members with SCIM provisioning*.

---

### NO.103 — Requesting Multi-Channel Guest access
> **Q.** Your company is on the Slack Enterprise Grid plan. The marketing team is working on a new branding campaign and would like to add consultants to your org as Multi-Channel Guests. What should the marketing team do to request access for these consultants? (Select the best answer.)
> - A. Invite via the workspace drop-down menu, and route approvals to a dedicated channel for admin approval.
> - B. Add consultants as full members for maximum flexibility.
> - C. @mention their Workspace Admin in the #proj channel.
> - D. DM an Org Owner requesting guest access.

**핵심 개념:** 게스트 초대는 **워크스페이스 메뉴로 초대 + 승인 프로세스(전용 채널)로 라우팅**하는 것이 표준.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(A):** 워크스페이스 메뉴 초대 + 승인 채널 라우팅이 통제된 표준 절차.
**오답 해설:** B 정식 멤버는 과도한 접근. C @mention은 표준 요청 절차 아님. D Org Owner DM은 비공식·비효율.
**출처:** Slack Help Center — *Invite guests / manage guest accounts*.

---

### NO.104 — Two recommended actions for an app-approval process
> **Q.** You're a Slack Workspace Owner responsible for setting up an app-approval process. In order to set up this process, which two actions are recommended? (Select the TWO best answers.)
> - A. Instruct requestors to post a business justification in #help-admins.
> - B. Restrict apps not already used by your org.
> - C. Send all app approval requests to app managers in a Slackbot message.
> - D. Turn on app approval so members can only install pre-approved apps.
> - E. Send all notifications to a specific channel that includes all app managers.

**핵심 개념:** 앱 승인은 **앱 승인 기능 활성화(D)** + **요청 알림을 앱 매니저 채널로 라우팅(E)** 하는 구조가 표준.
**덤프 정답:** D, E → ✅ 재판정 일치
**정답 근거:** D 승인된 앱만 설치되게 제한. E 매니저가 모인 채널에서 검토·승인.
**오답 해설:** A/C 임시·수동 방식으로 확장성 낮음. B 공식 승인 절차와 무관한 제한.
**출처:** Slack Help Center — *Manage app approval*.

---

### NO.105 — Two features in Slack's native mobile controls (Enterprise Grid)
> **Q.** Your organization would like to maintain their Bring Your Own Device (BYOD) policy on Slack's Enterprise Grid plan and have not yet decided on an Enterprise Mobility Management (EMM) provider. Which two features are included in Slack's native mobile controls on the Enterprise Grid? (Select the TWO best answers.)
> - A. Block file downloads and copying on mobile devices.
> - B. Domain allow list to limit mobile access to corporate workspaces only.
> - C. Remotely erase data if a device is stolen.
> - D. IdP group management for mobile devices.
> - E. Jailbreak or root detection for mobile devices.

**핵심 개념:** Slack Enterprise Grid **네이티브 모바일 보안 기능**(EMM 없이 사용)은 문서상 5종이다: 파일 다운로드/메시지 복사 차단, 2차 인증 요구, 필수 모바일 브라우저 지정, 탈옥/루팅 기기 차단, 최소 앱 버전 요구. 이 문항 정답은 그중 **A(다운로드/복사 차단) + E(탈옥/루팅 차단)**.
**덤프 정답:** A, B → ⚠️ 재판정 불일치 (내 판단: **A, E**) *(공식 문서로 확인, 확신도: 높음)*
**정답 근거(A, E):** "Mobile security for Enterprise Grid" 문서의 *"Native security features … For devices that aren't managed by EMM"* 목록에 **"Block file downloads and message copying"(A)** 와 **"Block jailbroken or rooted devices"(E)** 가 명시돼 있다.
**왜 덤프 B가 틀렸나:** "도메인 허용목록으로 모바일 접근을 회사 워크스페이스로 제한"(B)은 **EMM 전용 기능**이다 — **AppConfig 키/값(`WhitelistedDomains`)** 으로 설정하며("only allow access to your org domain when members use your EMM app"), EMM 등록 앱이 필요하므로 BYOD·EMM 미사용 기기엔 적용 불가 → 네이티브 통제가 아니다.
**오답 해설:** C 원격 삭제(remote wipe)는 EMM/MDM 필요(네이티브 목록에 없음). D IdP 그룹 관리는 모바일 전용 네이티브 통제가 아님.
**출처:** Slack Help Center — [Mobile security for Enterprise Grid](https://slack.com/help/articles/360033806733-Mobile-security-for-Enterprise-Grid) (네이티브 기능 목록), [Block file downloads and message copying](https://slack.com/help/articles/360016181794-Block-file-downloads-and-message-copying-on-Enterprise-Grid), [Block jailbroken or rooted devices](https://slack.com/help/articles/360042097113-Block-jailbroken-or-rooted-mobile-devices-from-accessing-Slack).

---

### NO.106 — Controlled rollout updates, minimize off-topic
> **Q.** Paul leads an accounting team and is implementing a new expense reporting system. He wants to update employees on the status of the system's rollout to different offices. He also wants to post links to help articles and online trainings that the team can use as resources. However, he wants to maintain control over the flow of information for these updates and would like to minimize off-topic discussion. Which of the following would help him achieve his goal?
> - A. New public workspace "Expenses" for all employees.
> - B. Private channel #expense-system-updates with all employees.
> - C. New invite-only workspace "Expenses."
> - D. Public announce-only channel for the expense system.

**핵심 개념:** 통제된 전사 업데이트는 **공개 announce-only 채널** — 지정 인원만 게시, 전원 열람/반응.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** announce-only 채널은 정보 흐름을 통제하면서도 전사 가시성을 극대화.
**오답 해설:** A/C 워크스페이스 신설은 과도. B private 채널은 가시성을 좁힘.
**출처:** Slack Help Center — *Restrict who can post in a channel (announcement channel)*.

---

### NO.107 — Business+: urgently review public channel content (trade secret leak)
> **Q.** You're a Workspace Owner on the Slack Business+ plan. Your company receives a report indicating the leak of trade secrets and needs to urgently investigate by reviewing Slack content in public channels. What is the best way to quickly handle this request? (Select the best answer.)
> - A. Contact Slack to export all channels/conversations incl. private and DMs.
> - B. Contact Slack to export the required public channel data.
> - C. Use the Import/Export Data tool in workspace settings to export the required public channel data.
> - D. Use the Discovery APIs to export the required public channel data.

**핵심 개념:** Business+에서 **공개 채널 데이터는 표준 Import/Export 도구**로 직접 수출 가능. Discovery API는 Grid 전용.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** Workspace Owner는 표준 수출 도구로 공개 채널 데이터를 Slack 문의 없이 내보낼 수 있다.
**오답 해설:** A/B 사설 채널·DM 수출은 별도 승인 필요(여기선 공개 채널만). D Discovery API는 Enterprise Grid 전용.
**출처:** Slack Help Center — *Export data from Slack*.

---

### NO.108 — Healthcare: dozen rotating consultants over 6–8 months
> **Q.** As an Org Admin at a healthcare company, you've been tasked with simplifying the experience for getting an upcoming communications project Slack-ready. A team of your organization's employees will work with a dozen rotating consultants at a communications agency to manage several communications campaigns over the next 6 to 8 months. You'll manage this external collaboration using guests or Slack Connect. What is the best method for managing this collaboration?
> - A. Use Slack Connect so each org manages privacy settings, naming, and its own members as needs shift.
> - B. Provide the agency guest accounts so they can invite additional external users.
> - C. Use Slack Connect to automatically sunset external access after 8 months.
> - D. Provide guest accounts so you can block file uploads/downloads.

**핵심 개념:** 조직 대 조직의 유동적 협업은 **Slack Connect** — 각 조직이 자기 멤버·정책을 관리.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(A):** Slack Connect는 상대 조직이 자기 인원을 직접 관리하므로 인원이 바뀌어도 유연.
**오답 해설:** B/D 게스트는 외부 인원을 내가 다 관리해야 해 부담. C Connect가 자동으로 access를 sunset하지 않음(만료는 수동 관리).
**출처:** Slack Help Center — *Slack Connect external collaboration*.

---

### NO.109 — Delete an inappropriate custom emoji
> **Q.** Brian, an HR manager, discovers an inappropriate custom emoji, and submits a request to Shonda, the Workspace Admin, to delete it. How should Shonda address this request?
> - A. Disable custom emoji addition (which also removes existing emoji).
> - B. Direct Brian to the Customize Slack page to delete it himself.
> - C. Navigate to Customize Slack and remove the emoji.
> - D. Tell Brian you can't delete but can replace it.

**핵심 개념:** Workspace Owner/Admin은 **Customize Slack 페이지에서 특정 커스텀 이모지를 삭제**할 수 있다.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 관리자가 문제 이모지를 직접 제거하는 것이 정확한 조치.
**오답 해설:** A 전체 생성 비활성화는 특정 이모지 제거와 무관. B 비관리자 Brian은 삭제 불가. D 삭제는 가능함.
**출처:** Slack Help Center — *Manage custom emoji*.

---

### NO.110 — Drive behavioral change to public channels (= NO.60)
> **Q.** Lindy leads an internal communications team. Her team wants to use public channels to gain more transparency in their internal communication. Employees currently tend to default to private channels/direct messages out of habit. Lindy needs to show employees the benefits of public channels. Which initiative should Lindy proceed with to drive behavioral change?
> - A. Temporarily disallow private channel creation and announce why.
> - B. Have the executive team mandate public channel usage.
> - C. Encourage executives to model the behavior in public channels themselves.
> - D. Plan a Slack Day on the benefits of public channels and search.

**핵심 개념:** 리더십의 **모범(모델링)** 이 문화 변화에 가장 큰 영향. (NO.60과 동일 문항.)
**덤프 정답:** C → ✅ 재판정 일치 *(D도 강력 — 확신도: 중)*
**정답 근거(C):** 경영진이 직접 공개 채널을 쓰면 강력한 문화적 본보기가 된다.
**오답 해설:** A/B 강제/차단은 반발. D 교육(Slack Day)은 유용하나 리더십 모델링만큼 파급력은 아님.
**출처:** Slack 자료 — *Public-first culture / leadership modeling*.

---

### NO.111 — Two scenarios where SCIM is the best method
> **Q.** In which two scenarios would SCIM provisioning be the best method of adding users to a workspace? (Select the TWO best answers.)
> - A. Multiple workspaces per subsidiary in Grid; need to assign users to specific workspaces.
> - B. Work with a packaging supplier; want all employees of both companies to communicate.
> - C. Preserve users' apps/integrations when deprovisioned.
> - D. Want users to have accounts only if they plan to use them.
> - E. Launch Slack to all employees in a single day and sunset the former platform.

**핵심 개념:** SCIM은 **대규모 사용자를 워크스페이스에 자동 배정**하고 **대규모 일괄 온보딩**에 이상적.
**덤프 정답:** A, E → ✅ 재판정 일치
**정답 근거:** A 자회사별 다중 워크스페이스에 사용자 배정. E 전사 일괄 런칭.
**오답 해설:** B는 Slack Connect. C는 앱 동작과 무관. D는 JIT 프로비저닝.
**출처:** Slack Help Center — *SCIM provisioning*.

---

### NO.112 — How default channels help end users
> **Q.** You're an Org Admin planning the structure of your organization's new workspace, and you decide to establish a few default channels for everyone to access. How does defining default channels help end users?
> - A. Default channels are always required, so members won't miss updates.
> - B. Users are auto-added to a set of private and public channels.
> - C. Members and guests can find each other as they're added.
> - D. Default channels orient new members and model channel naming conventions.

**핵심 개념:** 기본 채널은 **신규 멤버를 안내하고 네이밍 규칙을 학습**시키는 역할.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 신규 멤버를 주요 조직 채널에 노출해 규범·네이밍을 자연스럽게 익히게 한다.
**오답 해설:** A "항상 필수"는 부정확. B 기본 채널은 private일 수 없음. C 일반 사용 설명(기본 채널 특유가 아님).
**출처:** Slack Help Center — *Set default channels*.

---

### NO.113 — Show if HR workspace lags (= NO.69)
> **Q.** Mayim, the Chief Human Resources Officer at Large Inc, is concerned that her team communicates mostly via direct messages rather than channels. She wants to know if the HR workspace is lagging behind the rest of the organization. What information should the Workspace Admin provide to help Mayim?
> - A. Messages in #help-hr triage channel over 30 days.
> - B. Instructions to run an in-channel emoji poll.
> - C. Percentage of DM messages in HR workspace vs the org's overall DM percentage.
> - D. The claim that HR is more confidential and should expect more DMs.

**핵심 개념:** 팀 간 소통 패턴 비교 = **DM 비중을 조직 평균과 비교**. (NO.69와 동일 문항.)
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** HR의 DM 비중 대 조직 평균 비교가 객관적 판단 근거.
**오답 해설:** A 단일 채널 수치. B 주관적 설문. D 근거 없는 일반화.
**출처:** Slack Help Center — *Workspace analytics*.

---

### NO.114 — Lost office device logged into Slack
> **Q.** Your company uses Slack Enterprise Grid. An employee loses an office device that is logged into Slack. What should an Org Admin do to mitigate risk?
> - A. Ask the user to End all sessions in their Slack settings.
> - B. Deactivate the user, reactivate once the device is located.
> - C. Sign the member out of the org via "Sign out of Slack" in the admin dashboard.
> - D. Notify Workspace Owners to temporarily remove the user from workspaces.

**핵심 개념:** Org Admin은 대시보드에서 **멤버를 전 세션에서 원격 로그아웃**해 즉시 접근을 차단(비활성화 없이).
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** 원격 세션 종료로 데스크톱/모바일/웹 접근을 즉시 막는다.
**오답 해설:** A 기기를 잃어 사용자가 실행 불가. B 비활성화는 과함(복구 가능성). D 워크스페이스 조치는 조직 전체 위험엔 부족.
**출처:** Slack Help Center — *Manage sessions / sign members out*.

---

### NO.115 — Deactivate departing members (list, after departure)
> **Q.** You're an Org Admin for an organization with an Enterprise Grid plan. You receive a list of several full members who will be leaving the organization in 5 days, with the instruction to deactivate their accounts after their departure. What is the best way to do this?
> - A. Deactivate in the Organization Settings 'Members' tab.
> - B. Contact Slack via /feedback to deactivate them.
> - C. Deactivate the members utilizing the SCIM API.
> - D. Request the Primary Org Owner, as only they can do this.

**핵심 개념:** 대량·자동 비활성화는 **SCIM API/IdP 동기화**로 처리하는 것이 확장적.
**덤프 정답:** C → ✅ 재판정 일치 *(A도 유효 — 확신도: 중)*
**정답 근거(C):** SCIM으로 IdP 데이터와 동기화하여 계정 비활성화를 자동화.
**오답 해설:** A 수동(Org Settings)도 가능하나 확장성이 낮음. B /feedback은 표준 관리 방법 아님. D 비활성화는 Primary Org Owner 전용이 아님.
**출처:** Slack Help Center — *User lifecycle management with SCIM*.

---

### NO.116 — Reduce @here/@channel noise
> **Q.** Bella is a Workspace Admin at a company with 3,500 employees. She is receiving complaints from her colleagues that "Slack is too noisy". Her team is bothered by frequent use of @here and @channel in public channels. She has never evaluated or changed the default settings, so she wants to change how those notifications work in her workspace. How can Bella change her workspace's messaging restrictions to minimize disruption?
> - A. DM each user asking them not to.
> - B. Set @here/@channel to be used only in private channels.
> - C. Restrict @here/@channel usage to Owners and Admins only.
> - D. Restrict public channel posting to Owners and Admins.

**핵심 개념:** Slack은 **@channel/@here/@everyone 사용을 Owner/Admin으로 제한**하는 설정을 제공.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** 대규모 공개 채널의 오남용을 막으면서 구조적 커뮤니케이션은 유지.
**오답 해설:** A 개별 DM은 비확장적. B 그런 세분 설정은 없음. D 게시 자체를 막는 것은 과함.
**출처:** Slack Help Center — *Manage @channel, @here, @everyone permissions*.

---

### NO.117 — Prepare for a 3-month exec check-in to define Slack success
> **Q.** A project team in charge of implementing Slack plans to check in with their executive team three months after the launch. The goal of this check-in meeting is to define the success of Slack at the organization. What should the team do to prepare for this milestone most effectively?
> - A. Show SSO configuration progress and IT help-desk training.
> - B. Meet with key business units to identify and measure productivity opportunities.
> - C. Show the admin console depth of settings/policies.
> - D. Display weekly active members trending from launch.

**핵심 개념:** 성공 정의는 **사용을 비즈니스 성과·생산성에 연결**하는 것 — 기술 셋업/활성 수만이 아님.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 비즈니스 유닛과 함께 Slack이 개선한 워크플로우·협업을 파악·측정해야 가치 중심 대화가 된다.
**오답 해설:** A/C 기술적 진행. D 활성 사용자 수만으론 가치를 설명하기 부족.
**출처:** Slack 자료 — *Define success and ROI*.

---

### NO.118 — New hire can't join a searchable External workspace
> **Q.** Pawnee Technologies is a global cloud software company that uses Slack Enterprise Grid to communicate and collaborate. You're a Slack Workspace Admin for your company's External workspace where your team collaborates with external partners. Today you're onboarding a new team member who will need to log in and join your workspace. You receive a direct message (DM) from them reporting a problem. While they had no issues joining the Global and Social workspaces, they report that Slack isn't giving them an option to join the External workspace, even though it shows up when they search for it. Why is the new hire unable to join your workspace? (Select the best answer.)
> - A. The Admin must add them as a Single-Channel Guest.
> - B. The workspace requires approval from the external partner.
> - C. The workspace requires the member to request to join.
> - D. The workspace requires an invitation from the Workspace Admin.

**핵심 개념:** **Invite Only** 워크스페이스는 검색엔 보여도 참여하려면 Workspace Admin의 초대가 필요하다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 검색에 뜨지만 "가입 옵션이 없다"는 것은 초대 전용을 의미(By Request라면 '요청' 버튼이 보임).
**오답 해설:** A 게스트 추가는 이 상황의 원인 아님. B 외부 파트너 승인 방식 아님. C By Request면 요청 옵션이 보였을 것.
**출처:** Slack Help Center — *Workspace visibility and access (Invite Only)*.

---

### NO.119 — Effect of mandatory 2FA
> **Q.** Which of the following statements describes the effect of configuring mandatory Two Factor Authentication (2FA) in Slack?
> - A. Members must have a complex password updated regularly.
> - B. Members must use a biometric reader.
> - C. Members use SSO to handle usernames/passwords.
> - D. Members must submit a verification code along with their password each sign-in.

**핵심 개념:** 2FA는 로그인 시 **비밀번호 + 인증 코드(앱/SMS)** 를 함께 요구한다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 높음)*
**정답 근거(D):** 비밀번호가 유출돼도 두 번째 요소(코드) 없이는 접근 불가.
**오답 해설:** A 비밀번호 정책, B 생체, C SSO — 모두 2FA의 정의가 아님.
**출처:** Slack Help Center — *Set up two-factor authentication*.

---

### NO.120 — Ongoing enablement on new Slack features across workspaces
> **Q.** You're an Org Primary Owner on your company's Slack Enterprise Grid. You have six workspaces, each representing one line of business. Your company's Chief Information Officer (CIO) is keen on keeping all members of the organization informed about new Slack features on an ongoing basis. How can you ensure all members are receiving ongoing enablement on new Slack features? (Select the best answer.)
> - A. Org-wide channel with recurring feature announcements and bookmarked learning material.
> - B. Advise Workspace Admins to point members to Slack's website.
> - C. Pin messages in a multi-workspace channel.
> - D. Direct members to a #help-slack channel to ask questions.

**핵심 개념:** 전사 지속 안내는 **org-wide 채널 + 학습 자료 북마크**로 능동 전달.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** org-wide 채널은 모든 워크스페이스 멤버에게 도달하며 자료 접근도 쉽다.
**오답 해설:** B/C 멤버가 정보를 찾아야 함. D 반응형(질문 대기)이라 능동 안내가 아님.
**출처:** Slack Help Center — *Org-wide channels / change enablement*.

---

### NO.121 — True/False: claiming domains subjects all workspaces to Grid policies
> **Q.** A user with a claimed email domain tries to create a new workspace. The user is redirected to the Enterprise Grid org's workspace directory and is asked to join an existing workspace or contact the Grid Org Owners for more details. True or False: Claiming relevant domains for your Enterprise ensures that all workspaces are subject to the organization's Grid policies, such as message retention, SSO/security settings, and eDiscovery/archiving.
> - A. True · B. False

**핵심 개념:** 도메인 클레임은 해당 도메인 사용자가 만든 워크스페이스를 조직으로 유입시켜 **중앙 거버넌스(보안·컴플라이언스·리텐션)** 아래 두게 한다.
**덤프 정답:** A (True) → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거:** 도메인 클레임으로 미관리 워크스페이스 난립을 막고 일관된 정책을 강제한다.
**오답 해설:** B(False)는 오답 — 클레임된 도메인 사용자의 신규 워크스페이스는 조직으로 유입돼 리텐션·SSO·eDiscovery 등 Grid 정책의 적용을 받는다.
**출처:** Slack Help Center — *Claim domains (Enterprise Grid)*.

---

### NO.122 — 15 external members for a 12-month partnership (= NO.81)
> **Q.** You're a Support Agent on the admin team for your organization's Slack Enterprise Grid workspace. You receive a service request from one of your employees to add 15 new members from a single external company to Slack in order to support a 12-month joint marketing partnership. The team requires multiple channels and members for external collaboration. How should you respond to the service request? (Select the best answer.)
> - A. Invite as Multi-Channel Guests with a 12-month expiration.
> - B. Use Slack Connect channel(s); the external org can set up a free Slack instance if needed.
> - C. Add external users to your IdP for SAML SSO.
> - D. Set up a jointly-owned separate workspace.

**핵심 개념:** 조직 대 조직 협업은 **Slack Connect**가 게스트/신규 워크스페이스보다 안전·확장적. (NO.81과 동일.)
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 외부인을 게스트로 들이지 않고 공유 채널로 협업.
**오답 해설:** A 15명 게스트는 관리 확장성 낮음. C IdP 편입은 부적절·위험. D 공동 워크스페이스는 거버넌스 복잡.
**출처:** Slack Help Center — *Slack Connect best practices*.

---

### NO.123 — Three best default prefixes
> **Q.** You're a Slack admin creating a list of default prefixes. You want to provide employees with standard naming conventions to use when they create new channels. After reviewing existing channels, you determine that there are three types of channels most often created: * Slack Connect channels for collaborating with partners. * Channels for groups within a line of business. * Channels to support collaboration on specific engagements. What are the three best prefixes to add to your default list? (Select the THREE best answers.)
> - A. #team- · B. announce · C. #help · D. #proj- · E. #slack · F. #ext-

**핵심 개념:** #team-(부서/기능 그룹), #proj-(프로젝트/엔게이지먼트), #ext-(외부/Slack Connect).
**덤프 정답:** A, D, F → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:** A LOB 내 그룹, D 특정 엔게이지먼트 협업, F Slack Connect 외부 파트너.
**오답 해설:** B announce는 공지용, C help는 지원용, E #slack은 표준 접두사 아님.
**출처:** Slack Help Center — *Channel naming conventions*.

---

### NO.124 — What's true when public file sharing is enabled
> **Q.** What is true when public file sharing is enabled?
> - A. Integrated DLP can monitor files in private channels and DMs.
> - B. Your org's file sharing settings apply to all files uploaded to a Slack Connect channel by any of the up to 250 orgs in the channel.
> - C. File upload permissions to Slack Connect channels can't be restricted.
> - D. In a public channel, only admins can create an external link for a file.

**핵심 개념:** 이 문항은 **소거법**으로 푼다. Slack Connect 파일 문서 기준으로 A·C·D가 모두 명백히 틀리므로 B가 남는다. ⚠️ B의 "한 조직 설정이 참여 250개 조직의 모든 파일에 적용"이라는 서술 **자체는 공식 문서로 직접 확인되지 않는다** — 실제 문서는 **조직별 통제 모델**(각 조직이 자기 멤버 업로드를 관리, Org는 외부 조직별 업로드 권한을 개별 설정)을 기술한다.
**덤프 정답:** B → ✅ 재판정 일치(소거법) *(단 B 서술은 문서 미확인 — 확신도: 중-낮음)*
**정답 근거:** A·C·D가 문서상 오답이라 소거로 B가 최선. B 문장을 문서가 적극 뒷받침하지는 않지만 나머지 셋보다 덜 틀리다.
**오답 해설:**
- A. DLP는 "public file sharing" 활성화와 무관한 별개 기능.
- C. **틀림** — Slack Connect 파일 업로드 권한은 제한 가능("owners and admins can manage these permissions").
- D. **틀림** — 공개 채널에선 **모든 멤버**가 외부 링크를 만들 수 있다(관리자 전용 아님).
**출처:** Slack Help Center — [Manage file uploads … for Slack Connect](https://slack.com/help/articles/1500005777562-Manage-file-uploads-canvas-sharing-and-list-sharing-for-Slack-Connect), [Add files to Slack](https://slack.com/help/articles/201330736-Add-files-to-Slack).

---

### NO.125 — What "public file sharing" gives members
> **Q.** You've just joined the Org Admin team at your organization. You notice that the setting for "public file sharing" is toggled to "enabled" in your organization. What ability does enabling "public file sharing" give members?
> - A. Share files externally by creating public URLs.
> - B. Share files in public channels within the Grid.
> - C. Share files with guests.
> - D. Share files externally via Slack Connect channels.

**핵심 개념:** 관리자 설정 **"Public File Sharing"** 은 파일의 **외부 링크(external link) 생성 → Slack 밖 공유**를 허용한다. (현재 UI 용어는 "external link"; "public URL/public link"는 동일 개념의 옛/API 용어 `files.sharedPublicURL`.)
**덤프 정답:** A → ✅ 재판정 일치 *(공식 문서로 확인, 확신도: 높음)*
**정답 근거(A):** 문서: "share it outside of Slack by creating an external link" — 외부 링크로 Slack 밖에서도 파일을 열람하게 한다.
**오답 해설:** B 내부 공유, C 게스트 공유, D Connect 공유는 각각 별개 기능.
**출처:** Slack Help Center — [Manage public file sharing](https://slack.com/help/articles/4412651915539-Manage-public-file-sharing), [Add files to Slack](https://slack.com/help/articles/201330736-Add-files-to-Slack).

---

### NO.126 — Remove a confidential file + find who downloaded it
> **Q.** Amy is an Org Owner on an Enterprise Grid plan. A workspace Admin informs Amy that a confidential file has been uploaded to a public channel by mistake. Amy needs to remove the file and determine who has downloaded it. What should Amy do to accomplish this goal?
> - A. Use a DLP solution to delete the file, and review the Audit Logs API to see who downloaded it.
> - B. Use MDM to disable downloads, then use session management.
> - C. Use a third-party eDiscovery app to delete it and use data exports.
> - D. Use EKM to revoke key access and review EKM logs.

**핵심 개념:** 민감 파일 **삭제는 DLP**, **다운로드 행위 추적은 Audit Logs API**.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** DLP로 파일을 제거하고 Audit Logs API로 다운로드 사용자를 확인.
**오답 해설:** B MDM은 기기 보안이지 파일 추적 아님. C eDiscovery 수출은 특정 다운로드 행위를 바로 보여주지 않음. D EKM 로그는 다운로드 행위를 보여주지 않음.
**출처:** Slack API — *Audit Logs API* / Slack Help Center — *DLP integration*.

---

### NO.127 — Two most security-critical settings
> **Q.** The Slack implementation team at Large Inc is confirming all of the settings on their new Enterprise Grid organization and wants to make sure that they have appropriately involved the Security team in any critical security decisions. Which TWO of the following settings are most critical to discuss with their Security team? (Choose two.)
> - A. Whether to enable admin-approved apps.
> - B. Who is allowed to add custom emoji.
> - C. Who can create and archive channels.
> - D. Who can invite new members.

**핵심 개념:** 외부 접근·서드파티 노출과 직결되는 **앱 승인(A)** 과 **멤버 초대 권한(D)** 이 보안상 핵심.
**덤프 정답:** A, D → ✅ 재판정 일치
**정답 근거:** A 서드파티 앱 통제, D 외부/신규 사용자 유입 통제.
**오답 해설:** B 이모지, C 채널 생성은 UX 영향이지 핵심 보안 사안은 아님.
**출처:** Slack Help Center — *Enterprise security controls*.

---

### NO.128 — Key benefit of a user group for a new-hire class
> **Q.** You're a Workspace Admin looking to set up a user group for a new hire class your organization has recently hired. What is a key benefit of setting up a user group for these individuals?
> - A. Users only get access to channels they're added to, keeping others confidential.
> - B. The group can be added to all relevant onboarding channels so no one is left out.
> - C. Any member from any workspace can notify new hires with one @mention.
> - D. Admins can create a group-only DM to foster community.

**핵심 개념:** 사용자 그룹을 **온보딩 채널들에 일괄 추가**하면 누구도 누락되지 않고 온보딩이 단순해진다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 그룹을 여러 채널에 추가해 멤버십 관리를 간소화.
**오답 해설:** A 사용자 그룹이 채널 접근을 자동 제한하지 않음. C 멘션은 그룹/채널 설정에 좌우. D 커뮤니티 조성은 핵심 이점이 아님.
**출처:** Slack Help Center — *Manage user groups (onboarding)*.

---

### NO.129 — When to create a channel rather than a DM
> **Q.** Which of the following scenarios would best justify creating a channel in your company's existing workspace, rather than starting a direct message?
> - A. Confirm meeting times. · B. A new line of business at your company. · C. A few quick questions. · D. Tell your manager you're not feeling well.

**핵심 개념:** 지속적·투명한 주제/팀/프로젝트 공간이 필요할 때(예: 신규 사업부) 채널을 만든다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 신규 사업부는 전용·투명한 상시 공간이 필요.
**오답 해설:** A/C/D 빠르거나 개인적 대화는 DM이 적합.
**출처:** Slack Help Center — *Channels vs direct messages*.

---

### NO.130 — Retire a channel but keep it for reference
> **Q.** Britt is a Workspace Admin who created a public channel called #bread-buds for co-workers who enjoy bread- making. The company has had new team members join, and the conversation has become more general about all types of carbohydrates. Britt decides it's time to expand the channel. Rather than rename it, Britt creates a new channel #carbohydrate-chats to be inclusive and start fresh with activity. At the same time, Britt wants to keep #bread-buds so the team can reference baking instructions that have been gathered over the past few years, but she doesn't want anyone posting in it. What should Britt do?
> - A. Convert #bread-buds to private, archive it, direct everyone to the new channel.
> - B. Delete #bread-buds, reference messages as needed.
> - C. Remove all members from #bread-buds and invite them to the new channel.
> - D. Post a redirect message in #bread-buds and archive it.

**핵심 개념:** 은퇴 채널은 **전환 안내 게시 후 아카이브** — 읽기 전용·검색 가능으로 히스토리 보존.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 아카이브는 새 게시를 막고 히스토리를 검색·참조 가능하게 유지 — Britt의 목표에 정확히 부합.
**오답 해설:** A 불필요한 비공개 전환. B 삭제는 참조 접근 위험. C 멤버 제거는 불필요.
**출처:** Slack Help Center — *Archive or delete a channel*.

---

### NO.131 — Org-wide news, admins-only posting, everyone must see
> **Q.** You're an Org Owner on the Slack Enterprise Grid plan responsible for posting news for your entire organization to read. You want to limit posting permissions to admins only. Sometimes the newsletters contain important action items, so it's important that everyone in your organization sees the message. What is the best way to post your message? (Select the best answer)
> - A. Default org-wide #announcements channel; post there.
> - B. Send to your team's channel and copy/paste the link to each team channel.
> - C. Send to all department-specific channels.
> - D. Send to #general with @channel.

**핵심 개념:** 공식 전사 공지는 **관리자만 게시 가능한 org-wide #announcements 채널**.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 전원 가시성 + 관리자 전용 게시로 깔끔한 공지 채널.
**오답 해설:** B/C 중복·파편화. D #general @channel은 스팸·피로.
**출처:** Slack Help Center — *Org-wide announcement channels*.

---

### NO.132 — Roles for approving invites + vendor in various channels
> **Q.** Tracy works on a marketing team and needs to collaborate with a marketing vendor for a new project being planned in various channels. To ensure the project is not delayed, Tracy must approve the new member invitations. Which statement is true about roles in this scenario?
> - A. Admin role to invite/approve; Single-Channel Guest for the vendor.
> - B. Admin role to invite/approve; Multi-Channel Guest for the vendor.
> - C. Member role to invite/approve; Multi-Channel Guest for the vendor.
> - D. Member role to invite/approve; Single-Channel Guest for the vendor.

**핵심 개념:** 초대 승인·역할 관리는 **Admin** 권한이 필요하고, "다양한 채널"이 필요한 벤더는 **Multi-Channel Guest**.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** Admin이 초대/승인 가능, 벤더는 여러 채널 접근 → Multi-Channel Guest.
**오답 해설:** A Single-Channel은 여러 채널에 부족. C/D Member는 초대 승인 권한 부족.
**출처:** Slack Help Center — *User roles / guest access*.

---

### NO.133 — Consolidate Tidepool (Pro) into Hurricane (Business+)
> **Q.** You're a Workspace Admin on the Slack Business+ plan. Your company, Hurricane Inc., recently acquired another company, Tidepool Ltd., that uses the Slack Pro plan. You need to consolidate Tidepool's Slack workspace into Hurricane's workspace. What is the best option for moving Tidepool's channels? (Select the best answer.)
> - A. Recreate channels in Hurricane to mirror Tidepool's.
> - B. Use the Move Channels page in the admin dashboard.
> - C. Export public channels from Tidepool, then import into Hurricane.
> - D. Copy channels via Copy Channels on the Channel Management page.

**핵심 개념:** 표준 워크스페이스 간(Pro→Business+) 통합은 **공개 채널 수출 → 대상 워크스페이스로 임포트**. Move Channels는 Enterprise Grid 전용.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** 수출/임포트로 히스토리를 보존하며 이전.
**오답 해설:** A 재생성은 히스토리 손실. B Move Channels는 Grid 전용. D Copy Channels 기능은 없음.
**출처:** Slack Help Center — *Import/export data*.

---

### NO.134 — Determine which orgs you work with in Slack Connect
> **Q.** You're an Org Owner trying to determine which organizations your company works with in Slack Connect channels. What is the best way to gather this information?
> - A. Review the Slack Connect section of the sidebar.
> - B. Review Slack Connect connections in the Org Admin dashboard.
> - C. Search Slack Connect channels in the channel management dashboard.
> - D. Export the list of Slack Connect channels from analytics.

**핵심 개념:** **Org Admin 대시보드의 Slack Connect connections** 섹션에서 연결된 조직 목록을 확인.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** 대시보드가 연결된 조직 전체를 보여준다.
**오답 해설:** A 사이드바는 개인 뷰. C 채널 관리는 채널만. D 분석 수출은 사용 지표 중심.
**출처:** Slack Help Center — *Manage Slack Connect connections*.

---

### NO.135 — When a private channel best suits
> **Q.** You provide channel strategy recommendations to your organization and want to ensure the right level of information visibility. In which situation would a private channel best suit the needs of the teams involved?
> - A. HR + hiring team discuss an open role incl. requirements, compensation, candidate info.
> - B. A team kicks off a new project and needs a channel.
> - C. A cross-functional team explores new product ideas.
> - D. A globally distributed org creates a channel for HQ events.

**핵심 개념:** **민감·기밀 논의(채용·보상·후보자 정보)** 는 private 채널.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 보상·후보자 정보는 전 멤버에게 노출되면 안 되는 민감 정보.
**오답 해설:** B/C/D 프로젝트·브레인스토밍·이벤트는 가시성을 위해 보통 공개 채널이 적합.
**출처:** Slack Help Center — *When to use private channels*.

---

### NO.136 — Track who downloaded a deleted confidential file
> **Q.** You're an Org Owner for a financial organization's Slack Enterprise Grid. Someone accidentally shared confidential financial statements in a public Slack channel. You have since deleted the file; however, you want to track which users have downloaded the file from Slack. What is the best way to do this? (Select the best answer.)
> - A. Use Discovery APIs to export public channel data.
> - B. Use the Audit Logs API to audit the file download action.
> - C. Use the Audit Logs API to export public channel data.
> - D. Use the Import/Export Data tool to export public channel data.

**핵심 개념:** 파일 다운로드 같은 **행위 추적은 Audit Logs API**.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(B):** Audit Logs API가 특정 파일의 다운로드 행위와 사용자를 기록.
**오답 해설:** A Discovery는 콘텐츠 검색/수출용. C/D 채널 데이터 수출은 다운로드 행위를 보여주지 못함.
**출처:** Slack API — *Audit Logs API*.

---

### NO.137 — Prevent free workspaces with org email
> **Q.** You're a Workspace Admin on the Slack Pro plan. Your compliance team asks you to prevent users from creating free workspaces with their organization email addresses. What should you recommend?
> - A. Stay on Pro, enable domain claiming.
> - B. Upgrade to Business+, enable EKM.
> - C. Upgrade to Enterprise Grid, enable domain claiming.
> - D. Ask the Org Owner to enable 2FA.

**핵심 개념:** **도메인 클레임은 Enterprise Grid 전용** — 조직 도메인으로 독립 워크스페이스 생성을 차단.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** Grid + 도메인 클레임으로 회사 이메일 기반 워크스페이스 난립을 막는다.
**오답 해설:** A Pro는 도메인 클레임 불가. B EKM은 무관. D 2FA는 인증 강화지 생성 차단 아님.
**출처:** Slack Help Center — *Claim domains (Enterprise Grid)*.

---

### NO.138 — Which options describe Champions (choose all)
> **Q.** Andrew is a Workspace Owner and head of HR for a government agency in Munich, Germany. As the head of HR, he manages all aspects of human resources in order to create an engaged workforce and resilient organization. The HR teams use a variety of technologies, and leadership is implementing a new integrated tool to improve collaboration and productivity. While the tool has many benefits, the adoption rate has been slow due to a lack of internal awareness. Andrew wants to convince leadership that he needs internal Slack advocates who can lead and support co- workers through the transition. He has a few people in mind who he would nominate as Champions. Which options appropriately describe Champions? (Choose all that apply.)
> - A. They are Slack Administrators, so they have the correct permissions.
> - B. They communicate and promote transparency to reinforce the tool's value.
> - C. They model best practices and rally the team toward common goals.
> - D. They identify key use cases and modify them over time.

**핵심 개념:** Champion은 **관리자일 필요가 없고**, 모범을 보이며 투명성·활용 사례를 이끄는 문화 옹호자.
**덤프 정답:** B, C, D → ✅ 재판정 일치
**정답 근거:** B 투명성 촉진, C 모범·팀 결집, D 활용 사례 발굴·개선.
**오답 해설:** A Champion이 되기 위해 Slack 관리자일 필요는 없음.
**출처:** Slack 자료 — *Build a Slack Champion network*.

---

### NO.139 — Visibility for a fundraising workspace (low admin energy)
> **Q.** You're a Slack admin at a nonprofit organization. You need to add a new workspace to your Slack Enterprise Grid. This workspace needs to support the fundraising efforts of the development team. It should be a place for the team to collaborate on upcoming campaigns, events, and conduct retrospectives on past efforts. You can't devote significant admin energy to managing this workspace, and most members of your org participate in fundraising efforts in some capacity. What visibility setting should you select for this new workspace? (Select the best answer.)
> - A. Open · B. Invite Only · C. By Request · D. Hidden

**핵심 개념:** 폭넓게 참여하고 관리 부담을 줄이려면 **Open**(누구나 초대/승인 없이 참여).
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(A):** Open 워크스페이스는 승인 없이 조직 누구나 참여 — 전사 참여형 활동에 이상적.
**오답 해설:** B/C 초대·승인은 관리 개입 필요. D Hidden은 제한·기밀 그룹용.
**출처:** Slack Help Center — *Workspace visibility settings*.

---

### NO.140 — Determine if an external person uses Slack
> **Q.** What is a way to determine if an external person outside of your organization also uses Slack?
> - A. Ask your Workspace Primary Owner.
> - B. Invite them to a Slack Connect channel to verify.
> - C. Search for their email in the "Slack Connect" section of your sidebar.
> - D. Search for their email in the "People" section of your sidebar.

**핵심 개념:** 사이드바 **Slack Connect** 섹션에서 이메일을 검색하면 상대 조직의 Slack 사용 여부를 확인할 수 있다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** Slack Connect 검색으로 외부 사용자 존재를 확인.
**오답 해설:** A 수동. B 초대 먼저는 비효율. D "People"은 내부 디렉터리 검색.
**출처:** Slack Help Center — *Slack Connect discovery*.

---

### NO.141 — Free plan: employees join, block outsiders w/o approval
> **Q.** You're the Workspace Primary Owner of a Slack Free plan. You want to allow all employees in your company to join your workspace when they're ready. You also want to prevent anyone outside your company from accessing your workspace without admin approval. What should you do? (Select the best answer.)
> - A. Allow all members to invite new members.
> - B. Invite all employees by entering their email addresses.
> - C. Direct employees to access Slack through your IdP.
> - D. Enable employees to sign up using the company's email domain.

**핵심 개념:** Free 플랜에서 **회사 이메일 도메인 가입**을 켜면 도메인 사용자만 자동 가입하고 외부인은 차단된다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 지정 도메인(@company.com) 사용자만 초대 없이 가입 가능하게 해 요건 충족.
**오답 해설:** A 전원 초대 허용은 외부인 유입 위험. B 수동 초대는 "준비되면 가입" 자율성과 어긋남. C IdP 강제는 보통 유료 플랜.
**출처:** Slack Help Center — *Workspace access on Free plans (email domain sign-up)*.

---

### NO.142 — Auto-join important channels for new users
> **Q.** You're a Workspace Admin, and you want all new users to be added to several important channels when they first log in. What should you do to ensure new users automatically join these channels? (Select the best answer.)
> - A. Create a workflow that sends a welcome message promoting the channels.
> - B. Pin the important channels in #general.
> - C. Train managers to add new hires to the channels.
> - D. Add the important channels to your workspace's default channels.

**핵심 개념:** **기본 채널(default channels)** 은 신규 멤버가 최초 로그인 시 자동 참여하는 채널.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 기본 채널로 지정하면 자동 참여가 보장된다.
**오답 해설:** A/B 인지에 도움되나 자동 참여를 강제하지 않음. C 수동은 비효율·누락 위험.
**출처:** Slack Help Center — *Set default channels*.

---

### NO.143 — Which cross-functional strategy to AVOID
> **Q.** In Large Inc's Enterprise Grid design, each business unit has its own workspace, and everyone is also a member of the Global workspace. The Sales team at Large Inc are slow adopters of Slack and have been using email instead of Slack to communicate with peers. Which of these strategies should the Sales team AVOID using to connect cross-functionally more effectively with Slack?
> - A. Move their channels into the Global workspace and convert default channels to private, to ease privacy fears.
> - B. Create an org-wide #sales-wins channel.
> - C. Create a #customer-feedback channel to convey concerns to Product/Engineering.
> - D. Create an org-wide #help-sales channel for cross-functional questions.

**핵심 개념:** 핵심 채널을 **비공개로 만드는 것은 투명성·발견성을 해쳐** 크로스펑셔널 협업 목적에 반한다 → 피해야 할 전략.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 채널을 Global로 옮기고 private로 바꾸면 발견성·협업이 줄어 Slack의 연결·투명성 목표와 배치.
**오답 해설:** B/C/D는 모두 투명성·협업을 촉진하는 바람직한 전략.
**출처:** Slack 자료 — *Change management and adoption*.

---

### NO.144 — Streamline Grid design (marketing 1 ws, sales 2 ws)
> **Q.** Your company just moved to Slack Enterprise Grid after using Slack inconsistently across departments. Current situation: * Marketing team: one workspace with hundreds of channels and customizations. * Sales team: two separate workspaces ("The Greatest Sales Team" and "More Deals More Money") with a few dozen channels each. What is the best approach for streamlining your Enterprise Grid design while still meeting organizational needs? (Select the best answer.)
> - A. Move sales data into marketing, rename to "Marketing and Sales," archive the two sales workspaces.
> - B. Delete the two sales workspaces and create a new "Sales" (since you can't change the URL). Leave marketing as-is.
> - C. Consolidate the two sales workspaces, rename as "Sales," update the URL to match branding. Leave marketing as-is.
> - D. Export all workspace data and import into a single consolidated workspace.

**핵심 개념:** 불필요한 혼란 없이 **가능한 곳만 통합** — 잘 작동하는 marketing은 그대로 두고 sales 둘을 하나로 합쳐 이름/URL 정리.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** sales 두 워크스페이스를 통합·리브랜딩하고 marketing은 유지 — 최소 disruption.
**오답 해설:** A marketing까지 합치는 것은 불필요한 혼란. B "URL 변경 불가"는 사실이 아님(변경 가능). D 전부 단일 워크스페이스로는 과도한 통합.
**출처:** Slack 자료 — *Enterprise Grid migration strategy*.

---

### NO.145 — Off-topic payroll requests in #help-benefits (two ways)
> **Q.** You're a Workspace Owner at Acme Inc. You notice that the #help-benefits channel receives a large number of off-topic payroll requests. In which two ways can you help address this issue? (Choose 2 answers.)
> - A. Respond to each payroll request with a reminder that the channel is benefits-only.
> - B. Set a clear channel topic and pin a post defining scope.
> - C. Use share to DM the payroll team about each request.
> - D. Add payroll team members to #help-benefits to respond.
> - E. Encourage payroll to create their own public #help channel.

**핵심 개념:** 채널 목적을 **명확히(토픽·핀 게시)** 하고, **전용 채널(#help-payroll)** 로 유도하면 구조적으로 해결된다.
**덤프 정답:** B, E → ✅ 재판정 일치
**정답 근거:** B 범위 명시로 오게시 감소. E 전용 채널로 올바른 곳 안내.
**오답 해설:** A/C 수동 리디렉트는 근본 해결 아님. D 페이롤 인원을 벤핏 채널에 넣는 것은 구조 개선이 아님.
**출처:** Slack Help Center — *Channel organization best practices*.

---

### NO.146 — Help service agents collaborate on high-priority tickets
> **Q.** Your organization's Head of Customer Service wants to better support internal collaboration between service agents working through high-priority customer tickets. As a Workspace Admin, what recommendation should you provide to help service agents collaborate more efficiently in Slack and reduce meetings?
> - A. Create a new channel per ticket and use emoji reactions.
> - B. Use Huddles when troubleshooting high-priority tickets.
> - C. Post Clips in team channels for troubleshooting demos.
> - D. Ask for help in the team channel and troubleshoot in thread.

**핵심 개념:** 실시간 경량 협업은 **Huddles** — 회의를 잡지 않고 즉석에서 문제 해결.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** Huddle로 실시간 트러블슈팅해 회의 부담을 줄인다.
**오답 해설:** A/C 비동기 작업엔 유용하나 실시간 협업 대체는 아님. D 스레드는 실시간보다 느림.
**출처:** Slack Help Center — *Use huddles*.

---

### NO.147 — Too many social channels; hard to find customer info
> **Q.** You're an admin for your company's Slack Enterprise Grid org. There are now too many social channels in a single workspace, and employees report difficulty finding relevant customer information. What do you recommend as a next step? (Select the best answer.)
> - A. Create a Social workspace and make all channels multi-workspace.
> - B. Delete or consolidate some social channels.
> - C. Create a new Social workspace and move the relevant channels there.
> - D. Delete social channels inactive for 90+ days.

**핵심 개념:** 소셜 채널이 업무 발견성을 해치면 **별도 Social 워크스페이스로 분리·이동**해 초점을 유지.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** 소셜·커뮤니티 논의를 별도 워크스페이스로 옮기면 업무 콘텐츠 발견성이 개선된다.
**오답 해설:** B/D 삭제는 커뮤니티 문화 훼손 위험. A 멀티워크스페이스화는 가시성만 늘려 clutter 해소가 안 됨.
**출처:** Slack 자료 — *Workspace design for scalability*.

---

### NO.148 — When to convert a public channel to private
> **Q.** Your organization is busy with quarterly account and financial planning. Many conversations are happening in Slack across all departments in various channels. In which situation is it best for an existing public channel to be converted to a private channel?
> - A. A project team has difficult comments/conversations this quarter.
> - B. Participants prefer a private project channel out of habit.
> - C. A channel for an office-location event not needed by other offices.
> - D. Finance/execs' quarterly-planning discussion evolves to require unreleased quarterly earnings.

**핵심 개념:** **민감·기밀 정보(미공개 실적, M&A)** 가 오가기 시작하면 접근을 제한하기 위해 비공개로 전환.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 아직 공개되지 않은 분기 실적은 제한된 그룹만 접근해야 하는 민감 정보.
**오답 해설:** A 어조 문제, B 습관/선호, C 관련성 — 기밀성 사유가 아님.
**출처:** Slack Help Center — *Convert a channel to private*.

---

### NO.149 — Contractor supporting many teams' public channels (6 months)
> **Q.** Medium Inc is on a Standard Slack plan and has recently hired Preethi as a contractor to take care of their food & beverage service. Preethi is on a six-month contract, supporting many teams within the food & beverage department. Each team has set up a public channel to triage requests, and Preethi is responsible for responding to these requests. What type of workspace access would be most suitable for Preethi?
> - A. Member with no deactivation time.
> - B. Single-Channel Guest with 6-month deactivation.
> - C. Member with 6-month deactivation.
> - D. Multi-Channel Guest with 6-month deactivation.

**핵심 개념:** 여러 채널 접근 + 기간 한정 = **Multi-Channel Guest + 만료일**.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** 여러 채널이 필요하나 정식 멤버 접근은 과하므로 Multi-Channel Guest에 6개월 만료 설정.
**오답 해설:** B Single-Channel은 여러 팀 채널에 부족. A/C Member는 과도한 접근(보안 위험).
**출처:** Slack Help Center — *Manage guest access*.

---

### NO.150 — Which system role assigns admin responsibilities
> **Q.** You've been working among a small group of experienced Slack admins. Your company is beginning to grow exponentially, and admin responsibilities such as channel administration, legal holds, and user management are overwhelming your small team. Your team decides to assign a few system roles to support the admin team. Which role will be responsible for assigning admin responsibilities? (Select the best answer.)
> - A. Compliance Admin · B. Roles Admin · C. Channels Admin · D. Users Admin

**핵심 개념:** **Roles Admin**이 조직 전반의 시스템 역할을 배정·관리한다.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(B):** Roles Admin은 멤버에게 시스템 역할을 부여·관리하는 권한을 가진다.
**오답 해설:** A Compliance는 리걸 홀드·데이터 수출. C Channels는 채널 구조. D Users는 멤버 프로필·비활성화.
**출처:** Slack Help Center — *System roles overview*.

---

> **파일 완료: NO.101~150.** 다음 파일 `slack-admin-dump-151-200.md` 로 이어집니다.
