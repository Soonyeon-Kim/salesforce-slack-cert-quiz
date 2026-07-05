# Salesforce Certified Slack Administrator — 덤프 검증·해설 (NO.51~100)

> 문서 목적·면책·표기 규칙은 [README](./README.md) 및 `slack-admin-dump-001-050.md` 상단 참고.
> 문제·보기는 영어 원문 유지, 해설은 한국어. `✅` 재판정 일치 / `⚠️` 불일치·논란.
> **이 파일의 ⚠️ 문항: NO.51, NO.71, NO.99, NO.100.**

---

### NO.51 — Wrong Slack Connect invite auto-approved
> **Q.** You're an Org Owner at a company that doesn't allow members to manage any Slack Connect permissions. A member reaches out with a concern: they sent a Slack Connect channel invitation to the wrong external company. The invitation was approved automatically. What should you tell the requestor? (Select the best answer.)
> - A. The requestor can choose how much channel history will be visible when the external org accepts. You can also offer to show them how to revoke the invitation if not yet accepted.
> - B. Channel history will not be visible when the external org accepts. You can also offer to revoke the invitation if not yet accepted.
> - C. All channel history will be visible when the external org accepts. You can also offer to revoke the invitation if not yet accepted.
> - D. All channel history will be visible when the external org accepts. You can also offer to show them how to revoke the invitation if not yet accepted.

**핵심 개념:** Slack Connect 채널에 외부 조직이 들어오면 **기존 채널 히스토리가 보인다**. 수락 전이라면 **대기 중 초대를 취소(revoke)** 할 수 있다.
**덤프 정답:** D → ⚠️ 재판정 논란 (내 판단: **C**) *(확신도: 중)*
**정답 근거:** "모든 히스토리가 보인다 + 수락 전 취소 가능"은 C·D 공통으로 맞다. 차이는 취소 주체 — 시나리오는 "멤버가 Slack Connect 권한을 전혀 관리하지 못한다"고 명시하므로, 멤버에게 "취소 *방법을 안내*(D)"하는 것은 성립하지 않는다. 권한이 있는 당신(Org Owner)이 "대신 취소를 제안(C)"하는 것이 맞다.
**오답 해설:**
- A. 채널 초대 시 인바이터가 히스토리 노출량을 "선택"하는 옵션은 표준 동작이 아님.
- B. "히스토리가 보이지 않는다"는 부정확.
- D. 취소 방법 안내 자체는 맞지만, 권한 없는 멤버가 실행할 수 없어 이 시나리오엔 부적합.

**출처:** Slack Help Center — *Slack Connect: manage channel invitations / revoke a pending invitation*.

---

### NO.52 — Measure student adoption one month in
> **Q.** You're an Org Admin for your university's Slack Enterprise Grid organization. You want to measure Slack adoption for incoming students one month into the school year. What is the best option to measure adoption analytics?
> - A. Total number of messages sent in DMs.
> - B. Total number of channels and workspaces incoming students have joined.
> - C. Average number of days users were active within the last month.
> - D. Number of workspaces incoming students have created.

**핵심 개념:** 도입/참여의 강력한 지표는 **사용자당 평균 활성 일수(active days)**. 멤버십 수나 DM 수는 실제 활동을 반영하지 못한다.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 평균 활성 일수는 지속적 사용(참여)을 직접 측정한다.
**오답 해설:**
- A. DM 수는 사적 메시징에 국한, 전반적 도입 측정 아님.
- B. 가입한 채널/워크스페이스 수는 활동이 아닌 멤버십.
- D. 워크스페이스 생성은 학생과 무관하고 보통 비활성화됨.

**출처:** Slack Help Center — *Analytics dashboard (active members)*.

---

### NO.53 — Member added to an auto-provisioning IdP group
> **Q.** What would be the expected behavior if a team member in Enterprise Grid is added to an IdP (Identity Provider) group with auto-provisioning enabled to a workspace?
> - A. Automatically added to the new workspace and unable to leave.
> - B. Notified they have a new workspace to join and unable to dismiss until they join.
> - C. No changes to the member's workspace list.
> - D. Automatically added to the new workspace unless it is a hidden workspace.

**핵심 개념:** IdP 그룹 매핑은 매핑된 워크스페이스에 멤버를 자동 프로비저닝한다. 단, **hidden 워크스페이스는 자동 추가 대상에서 제외**(초대/수동 추가 필요).
**덤프 정답:** D → ✅ 재판정 일치 *(공식 문서로 확인, 확신도: 중)*
**정답 근거(D):** 문서상 hidden 워크스페이스는 멤버가 볼 수 없어 초대/추가가 필요하므로, IdP 그룹 자동 프로비저닝은 "hidden이 아닌 한" 자동 추가한다.
**오답 해설:**
- A. "자동 추가"는 맞지만 hidden 예외를 담지 못함(또한 A는 hidden을 무시). 참고로 IdP 그룹으로 추가된 워크스페이스는 기본 워크스페이스로 취급돼 그룹에서 빠지기 전엔 떠날 수 없다는 점은 사실이다.
- B. "알림 후 강제 조인" 방식이 아님.
- C. 변화 없음은 오답 — 자동 추가된다.

**출처:** Slack Help Center — [Connect identity provider groups to your Enterprise organization](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-organization).

---

### NO.54 — Eliminate inappropriate messages from an external user
> **Q.** You're an admin in your organization's external workspace primarily used for Slack Connect conversations. You received several complaints about inappropriate messages from an external user. Which step should you take to eliminate inappropriate messages from this user moving forward?
> - A. Disconnect all shared connection points with the offender's org using the Connections menu.
> - B. Remove the user from all of their channels in bulk using the External People menu.
> - C. Mute the offensive user in each channel via channel Settings.
> - D. Encourage reporters to use /leave in each conversation with the offender.

**핵심 개념:** 특정 외부 사용자를 차단하려면 **External People 대시보드에서 그 사용자를 모든 채널에서 일괄 제거**한다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 대시보드에서 해당 외부 사용자를 채널들에서 제거하면 향후 메시지를 원천 차단하면서 조직 전체엔 영향이 없다.
**오답 해설:**
- A. 조직 간 연결 전체 해제는 과도하며 전 조직에 영향.
- C. 뮤트는 개인별로 메시지를 가릴 뿐 차단이 아님.
- D. /leave는 신고자 본인만 나가게 할 뿐 가해자를 막지 못함.

**출처:** Slack Help Center — [Use the Slack Connect external people dashboard](https://slack.com/help/articles/5682545991443-Use-the-Slack-Connect-external-people-dashboard).

---

### NO.55 — Can't find external contact on Slack Connect
> **Q.** You recently started working with a new external organization that will supply crucial ingredients needed to make your products. It's important to be connected with them at a moment's notice, and you've noticed that your emails often go unanswered for long periods of time. You decide to look up your key contact's email on the Slack Connect page but get no results. What is the reason you can't find the external contact on Slack Connect?
> - A. The external org won't be discoverable since you don't have a Slack Connect channel with them yet.
> - B. The external org is using a free version of Slack.
> - C. The external org has turned off Slack Connect.
> - D. The external org has turned off Slack Connect Discoverability.

**핵심 개념:** 다른 조직이 검색으로 발견되려면 **Slack Connect Discoverability**가 켜져 있어야 한다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 상대 조직이 Discoverability를 껐다면 Slack을 쓰더라도 검색 결과에 뜨지 않는다.
**오답 해설:**
- A. 아직 채널이 없어도 discoverable한 조직은 검색 가능.
- B. 무료 플랜도 일부 제한 하에 Connect 초대 수락 가능 — 검색 실패의 결정적 원인 아님.
- C. Connect 자체를 끄면 채널 생성이 막히지만, "검색이 안 되는" 구체 이유는 Discoverability(D).

**출처:** Slack Help Center — *Slack Connect discoverability settings*.

---

### NO.56 — Allow non-admin members to invite guests
> **Q.** Lydia, an Org Admin on Enterprise Grid, wants to appoint members from her company's corporate events team to invite external guests to Slack. However, these corporate events team members are regular Slack members, not Workspace Admins. Where should Lydia go to allow these individuals to start inviting guests on Slack?
> - A. Workspace Transfer Ownership page · B. Organization Policies · C. Workspace Invitations page · D. Workspace Settings

**핵심 개념:** Enterprise Grid에서 초대·게스트 권한은 **Organization Policies**(조직 정책)에서 설정 — 특정 비관리자에게 게스트 초대 권한 부여 포함.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** 조직 정책에서 외부 초대 권한을 구성해 특정 멤버가 게스트를 초대하도록 허용한다.
**오답 해설:**
- A. 소유권 이전과 무관.
- C. 워크스페이스 초대 페이지는 개별 초대 실행용이지 권한 정책 설정이 아님.
- D. 워크스페이스 설정만으로는 조직 차원 초대 권한 부여가 어려움.

**출처:** Slack Help Center — *Manage invitations / Organization-level policies (Enterprise Grid)*.

---

### NO.57 — HR sensitive comms across separate department workspaces
> **Q.** Large Inc. is a consumer goods company that uses the Slack Enterprise Grid org. Large Inc.'s Human Resources (HR) director is looking to streamline how they: * Share department-specific policies, and * Handle sensitive questions hiring managers may have regarding recruiting and candidate offers. Each department has its own separate Enterprise Grid workspaces. How should the HR director use Slack for this use case? (Select the best answer.)
> - A. Multi-workspace public channel per department; add hiring managers.
> - B. Multi-workspace private channel per department; add hiring managers.
> - C. Private channel in the HR workspace; add departmental hiring managers.
> - D. Separate hiring-manager group DMs per department.

**핵심 개념:** 부서가 **서로 다른 워크스페이스**에 있고 민감 정보를 다루므로, **멀티워크스페이스 비공개 채널**로 여러 워크스페이스 멤버가 안전하게 협업한다.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(B):** 멀티워크스페이스 private 채널은 여러 워크스페이스의 멤버를 안전하게 모으며 부서별 민감 논의에 적합.
**오답 해설:**
- A. 공개 채널은 민감 정보에 부적합.
- C. HR 워크스페이스 한 곳의 private 채널은 다른 워크스페이스 hiring manager 접근을 제한(참고: NO.14는 HR이 단일 워크스페이스라 C가 정답이었음 — 조건 차이).
- D. 그룹 DM은 지속 협업엔 비확장적·비조직적.

**출처:** Slack Help Center — *Multi-workspace channels (Enterprise Grid)*.

---

### NO.58 — Public-channel views dropped; what next
> **Q.** Anastasia is an Org Owner on the Enterprise plan. In the Sales Workspace, Anastasia has noticed a large drop in the percentage of views in public channels. What should Anastasia do next?
> - A. Ask the team to react with :eyes: when they've read a message.
> - B. Identify the most active members and ask them to post more.
> - C. Provide additional learning and host a Slack day.
> - D. Instruct managers to use more @channel and @here.

**핵심 개념:** 참여 하락에는 **교육·재참여 캠페인(Slack Day)** 으로 지속가능한 행동 변화를 유도한다.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** Slack Day 등 학습 세션으로 공개 소통의 가치를 재교육하는 것이 지속적 해법.
**오답 해설:**
- A. 이모지 읽음 표시는 단기 미봉책.
- B. 일부 활성 멤버에게 요청하는 것만으론 전략 부족.
- D. @channel/@here 남발은 알림 피로만 유발.

**출처:** Slack 자료 — *Driving adoption / Slack Days*.

---

### NO.59 — Champion receiving many DMs; encourage best practices
> **Q.** Jose works at Globex and is a Slack administrator and Champion. He receives several Slack direct messages per day from employees looking for more information on a range of topics, such as how to connect apps to their Slack workspace and where to find training materials. Jose wants to encourage Slack best practices among employees. Which course of action should Jose take in this situation?
> - A. Answer; if they still can't find it, post their question in a public #help channel and respond in thread.
> - B. Ask employees to post their own question in a public #help channel where Jose's team responds in thread.
> - C. Post their question on their behalf in a public #help channel and respond in thread.
> - D. Respond to each employee via DM.

**핵심 개념:** 답을 **검색 가능하게** 만들고 개방 문화를 모델링하려면, 질문자가 **직접 공개 #help 채널에 올리게** 유도한다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 공개 채널 게시를 습관화하면 지식이 축적·검색되고 중복 문의가 준다.
**오답 해설:**
- A. 답을 먼저 다는 하이브리드는 공개 습관 형성이 약함.
- C. 대신 올려주면 질문자의 공개 행동 습관이 형성되지 않음.
- D. DM 답변은 지식이 흩어지고 반복됨.

**출처:** Slack 자료 — *Promote open communication / knowledge sharing*.

---

### NO.60 — Drive behavioral change toward public channels
> **Q.** Lindy leads an internal communications team. Her team wants to use public channels to gain more transparency in their internal communication. Employees currently tend to default to private channels/direct messages out of habit. Lindy needs to show employees the benefits of public channels. Which initiative should Lindy proceed with to drive behavioral change?
> - A. Encourage executives to model the behavior and communicate in public channels themselves.
> - B. Plan a Slack Day (with admins/champions) on the benefits of public channels and search.
> - C. Have the executive team mandate public channel usage.
> - D. Temporarily disallow private channel creation and announce why.

**핵심 개념:** 문화 변화에는 **리더십의 모범(모델링)** 이 가장 영향력이 크다. 강제(mandate)나 기능 차단은 반발을 부른다.
**덤프 정답:** A → ✅ 재판정 일치 *(B도 강력 — 판단형 문항, 확신도: 중)*
**정답 근거(A):** 경영진이 공개 채널을 직접 사용하면 강력한 문화적 본보기가 되어 행동 변화를 이끈다.
**오답 해설:**
- B. Slack Day 교육은 유용하나(둘째로 강력), 리더십 모델링만큼 파급력은 아님.
- C. 강제 지시는 반발 유발.
- D. private 채널 생성 차단은 강압적이라 반감.

**출처:** Slack 자료 — *Building a public-first culture / leadership modeling*.

---

### NO.61 — Duplicate channels / hard to find; first step
> **Q.** Marianne, an Org Admin, hears feedback that it's difficult for her members to find channels. She regularly receives requests in the #help-slack channel from members who accidentally created duplicate channels because they weren't aware there was already a channel on a certain topic. Which action should Marianne's team take first to address the problem?
> - A. Allow all members to archive channels.
> - B. Standardize and communicate channel naming conventions.
> - C. Encourage members to add a channel purpose and topic.
> - D. Restrict new channel creation to admins only.

**핵심 개념:** 중복·검색성 문제의 **첫 단계**는 **네이밍 규칙 표준화·공지**.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 일관된 네이밍은 기존 채널을 쉽게 찾고 목적을 이해하게 해 중복을 줄인다.
**오답 해설:**
- A. 아카이브 권한 확대는 중복 문제 해결과 무관.
- C. 목적/토픽 추가도 좋지만 우선순위는 네이밍 규칙.
- D. 생성 제한은 더 강한 조치로, "첫 단계"로는 과함.

**출처:** Slack Help Center — *Channel naming best practices*.

---

### NO.62 — Sales works with customers; reps change accounts frequently
> **Q.** You're a Workspace Owner for a Slack Business+ workspace. The sales team wants to work with customers in Slack, but sales representatives change accounts frequently. Which best practice process should you establish?
> - A. Invite customers to existing account channels as Single-Channel Guests; archive when relationship ends.
> - B. Create new account channels and share them with customers using Slack Connect.
> - C. Create new account channels; add customers as Single-Channel Guests with a 1-year expiration.
> - D. Create a new free Slack workspace; invite sales and customer care as full members.

**핵심 개념:** 장기 외부 협업은 **Slack Connect**(공유 채널)가 게스트 계정보다 낫다 — 계정 수동 관리 불필요.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** Slack Connect로 고객과 공유 채널을 쓰면 담당 변경에도 계정을 새로 만들 필요 없이 안정적으로 협업.
**오답 해설:**
- A/C. 게스트 계정은 수동 관리 부담이 큼.
- D. 새 무료 워크스페이스는 소통을 파편화.

**출처:** Slack Help Center — *Slack Connect for external collaboration*.

---

### NO.63 — What happens when a Slack Connect channel is disconnected
> **Q.** You're a Slack admin for SealBox, a company specializing in waterproof laptop cases. In preparation for a new product launch, SealBox partners with an advertising agency, Ad Heroes Inc. You create a Slack Connect channel and share it with Ad Heroes' Slack workspace. The members of the Ad Heroes team are concerned about losing access to messages and files shared in the channel once the project ends and the channel is disconnected. What will happen once the channel is disconnected? (Select the best answer.)
> - A. All orgs retain full access and can continue using it normally.
> - B. Ad Heroes retains full control and can keep posting messages/files.
> - C. Ad Heroes keeps an archived version, but only files posted by Ad Heroes' members are visible.
> - D. The channel is archived in Ad Heroes' workspace, but all messages/files shared by both orgs remain accessible.

**핵심 개념:** 연결 해제 시 **각 조직은 아카이브 사본을 보유**하고, 양측이 공유한 모든 메시지·파일은 접근 가능한 채로 남는다. 이후 게시는 불가.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** 각 조직 워크스페이스에 아카이브되며 양측 콘텐츠가 보존된다.
**오답 해설:**
- A. 해제 후 "정상 사용 지속"은 불가(아카이브됨).
- B. 해제 후 계속 게시 불가.
- C. "자기 조직 파일만 보인다"는 부정확 — 양측 콘텐츠 모두 접근 가능.

**출처:** Slack Help Center — *Disconnect from an organization (Slack Connect)*.

---

### NO.64 — Reduce off-hours notifications across time zones
> **Q.** You're an Org Admin for a global organization operating in multiple time zones. In your org- wide #help-slack channel, members report they are receiving notifications outside of their working hours from other members operating in different time zones. In addition to recommending Do Not Disturb (DND) preferences, how can you help promote a digital HQ at your organization and ensure that members are receiving notifications only during working hours? (Select the best answer.)
> - A. Set profile status to Away when not online.
> - B. Use Scheduled Send so messages are delivered during shared working hours.
> - C. View a recipient's local time in their profile before sending.
> - D. Set reminders to send the message during shared working hours.

**핵심 개념:** **Scheduled Send**로 지금 작성하고 상대의 근무 시간에 맞춰 전송을 예약하면 알림 시점을 능동적으로 조정할 수 있다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** Scheduled Send는 전송 자체를 지연시켜 근무 시간 외 알림을 방지한다.
**오답 해설:**
- A. Away 상태는 알림을 지연시키지 못함.
- C. 로컬 시간 보기는 도움되나 알림 자체를 미루지 못함.
- D. 개인 리마인더는 수동적.

**출처:** Slack Help Center — *Schedule messages to send later*.

---

### NO.65 — Delegate responsibilities in a 10-workspace Grid
> **Q.** You're the Primary Org Owner of a large Slack Enterprise Grid org composed of 10 workspaces for individual business units. How should you delegate responsibilities appropriately?
> - A. Delegate a Workspace Admin from each BU for everyday tasks.
> - B. Delegate an Org Admin from each BU.
> - C. Create a multi-workspace channel for selected members to manage all admin requests.
> - D. Delegate an Org Owner from each business.

**핵심 개념:** 최소 권한 — 워크스페이스별 일상 업무는 **Workspace Admin**에게 위임하면 충분.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** Workspace Admin은 멤버 관리·앱 승인·설정 등 워크스페이스 단위 업무에 적합하며 권한이 과하지 않다.
**오답 해설:**
- B/D. Org Admin/Owner는 조직 전체 권한이라 과도·위험.
- C. 채널은 실제 관리 권한을 위임하지 못함.

**출처:** Slack Help Center — *Types of roles / delegate workspace administration*.

---

### NO.66 — Onboard users into discrete workspaces with access limits
> **Q.** You're an Org Admin for your Slack Enterprise Grid org. Three departments must collaborate while maintaining access controls. How should users be onboarded into discrete workspaces while maintaining access limits?
> - A. Create a workflow to manage access requests; add users manually upon approval.
> - B. Allow users to join workspaces at their own direction.
> - C. Connect an IdP group to appropriate workspaces to control membership.
> - D. Direct users to self-manage memberships via invite requests.

**핵심 개념:** 안전·자동화된 워크스페이스 멤버십 통제는 **IdP 그룹 연결**로 부서/역할 기반 자동 관리.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** IdP 그룹을 워크스페이스에 연결하면 부서 기준으로 멤버십이 자동 관리돼 규정 준수·보안에 유리.
**오답 해설:**
- A. 수동 추가는 오류·비효율.
- B/D. 자율 참여/자가 관리는 통제 환경에 부적합.

**출처:** Slack Help Center — *Connect IdP groups to workspaces*.

---

### NO.67 — Only Org Admins/Owners should approve new Connect channels
> **Q.** You're an Org Admin in your Slack Enterprise Grid org. Your security team has requested that all new Slack Connect channels only be approved by Org Admins and Org Owners. What should you do? (Select the best answer.)
> - A. Change permissions so any Workspace Admin/Owner can approve.
> - B. Advise Workspace Admins/Owners to forward all requests to Org Admins/Owners.
> - C. Use Slack's default permissions, which already state only Org Admins/Owners approve new channel requests.
> - D. Send all requests to a private channel on an Org Admin/Owner-only workspace.

**핵심 개념:** Enterprise Grid에서 **Slack Connect 채널 승인은 기본적으로 Org Admin/Owner만** 가능. 별도 설정 불필요.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** 기본 권한이 이미 요건과 일치하므로 그대로 사용하면 된다.
**오답 해설:**
- A. Workspace Admin/Owner 승인 허용은 요건에 반함.
- B. 수동 포워딩은 불필요.
- D. 별도 채널 워크플로우도 불필요.

**출처:** Slack Help Center — *Manage Slack Connect / channel approvals (Enterprise Grid)*.

---

### NO.68 — Appropriate channel name (prefixes: help-, proj-, announcements-)
> **Q.** You're a Workspace Admin for AcmeTesting Inc., which has standard prefixes: help-, proj-, and announcements-. What is an appropriate channel name within the AcmeTesting Sales workspace? (Select the best answer)
> - A. #sales-help-services · B. #acme-sales proj finance · C. #help-finance · D. #announcements-team

**핵심 개념:** 채널명은 **접두사를 맨 앞**에 두고 하이픈으로 단어를 연결하는 규칙을 따른다(#help-finance).
**덤프 정답:** C → ✅ 재판정 일치 *(D도 형식상 유효 — 확신도: 중)*
**정답 근거(C):** `help-` 접두사 + 주제(finance)로 규칙에 부합하는 명확한 이름.
**오답 해설:**
- A. `help-` 접두사가 맨 앞이 아님(순서 뒤바뀜).
- B. 공백 포함 등 형식 위반.
- D. `#announcements-team`은 형식상 접두사 규칙엔 맞지만 주제가 모호(안내 채널 목적 불명확)해 C보다 부적절.

**출처:** Slack Help Center — *Channel naming conventions*.

---

### NO.69 — Show if HR workspace lags (DM vs channel)
> **Q.** Mayim, the Chief Human Resources Officer at Large Inc, is concerned that her team communicates mostly via direct messages rather than channels. She wants to know if the HR workspace is lagging behind the rest of the organization. What information should the Workspace Admin provide to help Mayim?
> - A. The percentage of DM messages in the HR workspace compared to the org's overall DM percentage.
> - B. The claim that HR is more confidential and should expect more DMs.
> - C. Instructions to run an in-channel emoji poll on channel vs DM usage.
> - D. The number of messages in the #help-hr triage channel over 30 days.

**핵심 개념:** 팀 간 소통 패턴 비교에는 **워크스페이스별 DM 비중을 조직 전체와 비교**하는 분석이 정확.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** HR의 DM 비중을 조직 평균과 비교하면 HR이 실제로 뒤처지는지 객관적으로 확인된다.
**오답 해설:**
- B. 근거 없는 일반화.
- C. 이모지 설문은 주관적·부정확.
- D. 단일 채널 메시지 수는 비교 지표가 아님.

**출처:** Slack Help Center — *Workspace analytics (messaging patterns)*.

---

### NO.70 — Two actions for thoughtful Enterprise Grid design
> **Q.** You lead a team responsible for launching Slack Enterprise Grid to all employees. Your leadership team firmly believes that Slack is currently too noisy and that a workspace dedicated to each major business unit will reduce noise. You want to be thoughtful about the workspace design and create an Enterprise Grid design that will best facilitate collaboration across your company. What are two actions you should take? (Select the TWO best answers.)
> - A. Create a business case for a thoughtful Grid design, and present it to leadership.
> - B. Create success criteria and key design principles, and work with your Slack account team to weigh pros/cons of each design model.
> - C. Create an implementation plan with a multi-workspace business-unit model.
> - D. Create and launch an employee survey to understand knowledge sharing and current usage.
> - E. Create an implementation plan with one large workspace to avoid silos.

**핵심 개념:** 설계 확정 전에는 **전략적 토대(비즈니스 케이스 + 성공기준·설계 원칙 + 계정팀 협업)** 를 먼저 세운다.
**덤프 정답:** A, B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거:**
- A. 전략적 설계의 필요성을 리더십에 설득하는 비즈니스 케이스.
- B. 성공기준·설계 원칙을 정하고 Slack 계정팀과 설계 모델을 비교.

**오답 해설:**
- C/E. 구체 구현안(다중/단일 워크스페이스)은 전략적 토대 없이 앞서감.
- D. 사용자 설문도 매우 유용하나(참고: NO.43), 이 문항은 '리더십 정렬·설계 원칙'이라는 토대 단계를 우선으로 봄.

**출처:** Slack 자료 — *Enterprise Grid design best practices*.

---

### NO.71 — EMM communication: when will users be signed out?
> **Q.** You're an Org Owner of a Slack Enterprise Grid org. Your company recently selected an Enterprise Mobility Management (EMM) provider and you will be turning on EMM. You're preparing a communication to share with your end users so they understand when they need to take action. What guidance would you include in your communication? (Select the best answer.)
> - A. End users will be immediately signed out of Slack on any unmanaged mobile devices.
> - B. Signed out if they don't complete EMM setup within one week.
> - C. Signed out if they don't complete EMM setup within 72 hours.
> - D. Signed out if they don't complete EMM setup within 24 hours.

**핵심 개념:** EMM 활성화 후 멤버는 **정해진 기한 내에 EMM 설정을 완료**해야 하며, 미완료 시 모바일 Slack에서 로그아웃된다. ⚠️ 공식 문서상 기한은 **12시간**이다(EMM을 켜면 정규 Slack 앱에서 "within 12 hours, 종종 그보다 훨씬 빨리" 로그아웃). **이 문항 보기에는 12시간이 없다.** (cf. NO.3)
**덤프 정답:** A → 🟡 재판정 정정: **A 수용(4개 중 최선)** *(이전 판 'C=72시간'은 잘못된 72h 수치에 기댄 오류 — 철회. 확신도: 중)*
**정답 근거:** Slack 공식 문서: "When EMM is turned on, members required to use the Slack for EMM app will be signed out of the regular Slack app **within 12 hours** (though often, this happens much sooner)." 설정 기한도 **12시간**("Members will have 12 hours to set up EMM… if a member does not complete the EMM setup, they will be signed out of Slack on their mobile devices"). 즉 실제 수치는 12시간이지 72시간이 아니다.
**보기 판정:** 시간창을 명시한 B(1주일)·C(72시간)·D(24시간)는 **모두 실제 12시간과 불일치**해 어느 것도 정확하지 않다. 반면 A("미관리 기기에서 곧 로그아웃")는 "정규 앱에서 12시간 내(종종 훨씬 빨리) 로그아웃" 동작과 부합해 4개 중 가장 방어 가능하다. 따라서 덤프의 **A를 수용**하고, 앞서 골랐던 C는 근거 없는 수치라 **철회**한다.
**오답 해설:**
- A. 문서상 로그아웃은 "즉시"라기보다 "12시간 내(종종 훨씬 빨리)"지만, 시간창이 틀린 B·C·D보다 정확하다.
- B. 1주일 창은 문서에 없음.
- C. "72시간" 창은 **어느 공식 Slack 문서에서도 확인되지 않음**(NO.3와 동일한 덤프 오기).
- D. 24시간은 설정 완료 기한이 아님(안드로이드의 '외부 워크스페이스' 로그아웃 맥락 24시간과 혼동한 값).

**출처:** Slack Help Center — [Enable Enterprise Mobility Management](https://slack.com/help/articles/115002579426-Enable-Enterprise-Mobility-Management-for-your-organization) (현재 문서: "within 12 hours"). 설정 기한 "12 hours to set up EMM …" 문구는 [Install EMM](https://slack.com/help/articles/115002247686-Install-Enterprise-Mobility-Management) 구버전.

---

### NO.72 — Manage high-volume workspace requests
> **Q.** You're an Org Admin responsible for managing your organization's three workspaces grouped by business vertical. Your organization wants to increase Slack usage across departments, and you anticipate new workspace requests. Given these business requirements, what is the best way to manage requests to create new workspaces?
> - A. Review/approve/reject requests in one public, searchable channel.
> - B. Route requests from an org-wide help channel to a private admin-only channel where admins review the business rationale.
> - C. Don't allow users to request workspaces; encourage more channels instead.
> - D. Encourage users to create workspaces themselves, then link via domain claiming.

**핵심 개념:** 워크스페이스 생성 요청은 **비공개 관리자 채널로 라우팅**해 비즈니스 타당성을 검토하는 것이 거버넌스에 맞다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 요청을 private 관리자 채널로 모아 검토하면 새 워크스페이스가 보안·전략에 부합하는지 통제할 수 있다.
**오답 해설:**
- A. 공개 채널은 민감한 관리 논의를 노출.
- C/D. 요청 프로세스 우회는 거버넌스를 무너뜨리고 파편화 위험.

**출처:** Slack Help Center — *Manage workspace creation requests (Enterprise Grid)*.

---

### NO.73 — Contest: who sent the most messages
> **Q.** You're a Workspace Owner introducing Slack to your organization for the first time. In order to encourage employees to use Slack, you've organized a contest to see who can send the most messages in Slack channels in a week. What's the best way to determine the winner? (Select the best answer.)
> - A. View the Channels tab in the analytics dashboard.
> - B. Install a custom bot in each channel to count messages.
> - C. View the Members tab in the analytics dashboard.
> - D. Export messages to view offline.

**핵심 개념:** **Members 탭**은 사용자별 전송 메시지 수를 보여줘 개인 참여를 추적하기 쉽다.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** Members 탭에서 멤버별 메시지 수를 확인하면 승자를 바로 알 수 있다.
**오답 해설:**
- A. Channels 탭은 채널별 활동(사용자별 아님).
- B/D. 봇 설치·수출은 네이티브 분석이 있는데 불필요·복잡.

**출처:** Slack Help Center — *Analytics dashboard (Members tab)*.

---

### NO.74 — Delegate app approval to "Ambassadors"
> **Q.** Large Inc has a number of apps pre-approved in the App Directory for their teams to use, but their admins want to nominate a group of "App Approval Ambassadors" in addition to their Workspace Owners. These "Ambassadors" will be responsible for reviewing and approving or denying apps in a #plz-app-request channel. How can the Org Admin ensure that these "Ambassadors" are able to most efficiently approve or deny apps?
> - A. Ambassadors review in the channel and use emoji to alert Admins to whitelist the app.
> - B. Promote Ambassadors to Workspace Owners.
> - C. Promote Ambassadors to Workspace Admins.
> - D. Add Ambassadors as "selected members or groups" to manage Approved Apps.

**핵심 개념:** 앱 승인 권한은 **"선택된 멤버/그룹"으로 위임**할 수 있어, Owner/Admin으로 승격하지 않고도 앱을 검토·승인하게 만든다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** 특정 멤버/사용자 그룹에게 앱 관리 권한을 위임하면 통제된 방식으로 승인 역량을 확장할 수 있다.
**오답 해설:**
- A. 이모지 알림은 결국 관리자가 수동 처리해야 하므로 비효율.
- B/C. Owner/Admin 승격은 필요 이상의 광범위 권한 부여.

**출처:** Slack Help Center — *Manage app approvals / delegate app management*.

---

### NO.75 — Notify 10 of 50 channel members (recurring weekly)
> **Q.** The marketing team at ACME Ltd has 10 team members and has a public channel called #marketing- discussion. The team collaborates and shares ideas on this channel. Now, other teams have joined, so the total channel membership is 50. The marketing director has the following needs: * There is an urgent marketing idea that must be prioritized in tomorrow morning's planning meeting. * The 10 team members are the only ones attending the planning meeting. * The 10 team members need to be notified before the meeting. Of note, the marketing director sends urgent re-prioritization messages weekly. How should the marketing director reach the marketing team?
> - A. DM each of the 10 members individually.
> - B. Create an @marketing-team user group and @mention it in the channel.
> - C. Post to the channel without notifying anyone.
> - D. Use @here and @channel to notify the entire channel.

**핵심 개념:** 특정 하위 집단을 반복적으로 알릴 땐 **사용자 그룹(@마케팅팀)** 을 만들어 멘션 — 무관한 멤버를 방해하지 않는다.
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 사용자 그룹 멘션으로 정확히 10명만 알림. 반복 사용에도 효율적.
**오답 해설:**
- A. 개별 DM 10회는 비효율·오류 위험.
- C. 아무도 알림받지 못해 요구 미충족.
- D. @here/@channel은 50명 전원을 불필요하게 알림.

**출처:** Slack Help Center — *Create and use user groups*.

---

### NO.76 — Ensure departing user loses Slack access (via IdP)
> **Q.** Moshi is a Workspace Owner on the Plus plan. John is leaving the company on Friday, and Moshi will be deactivating John's IdP account. What does Moshi need to do to ensure that John won't have access to Slack?
> - A. Change the email and reset the password; changing the email ends John's session.
> - B. Deactivating the IdP account will automatically delete the bound Slack account via SSO.
> - C. Check that the IdP supports de-provisioning via SCIM and that the connector app is installed and configured correctly.
> - D. Activate "Just-in-Time" de-activations to auto-remove John and anyone inactive >14 days.

**핵심 개념:** IdP 비활성화가 Slack 계정 비활성화로 이어지려면 **IdP가 SCIM 디프로비저닝을 지원**하고 커넥터가 올바로 구성돼 있어야 한다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** SCIM이 구성돼 있어야 IdP의 사용자 비활성화가 Slack 계정 비활성화를 트리거한다.
**오답 해설:**
- A. 이메일 변경/비번 리셋은 안전·확장적 방법이 아님.
- B. IdP 비활성화가 Slack 계정을 "삭제"하지는 않음(비활성화이며, SCIM 구성이 전제).
- D. "JIT 비활성화"는 Slack 기능이 아님.

**출처:** Slack Help Center — [Manage members with SCIM provisioning](https://slack.com/help/articles/212572638-Manage-members-with-SCIM-provisioning).

---

### NO.77 — Lock guest invitation policy to Org level
> **Q.** You're the Org Admin for a company's Slack Enterprise Grid organization. Currently, Workspace Admins can decide how guest invitations are managed within their workspace. You want to lock this policy so that guest invitations can only be approved by Org Owners and Admins. What action should you take to make this change? (Select the best answer)
> - A. Lock guest invitations from each workspace's settings page.
> - B. Ask the Org Owner because only Org Owners can change org-level policies.
> - C. Notify users that guest invitations must be submitted at the org level.
> - D. Lock guest invitations from the org admin dashboard.

**핵심 개념:** 조직 차원 정책 잠금은 **Org Admin 대시보드**에서 — Workspace Admin의 독립 제어를 막는다.
**덤프 정답:** D → ✅ 재판정 일치
**정답 근거(D):** Org Admin/Owner가 대시보드에서 게스트 초대 설정을 잠그면 워크스페이스 단위 제어를 무력화한다.
**오답 해설:**
- A. 워크스페이스 설정만으론 조직 차원 잠금 불가.
- B. Org Admin도 가능하므로 Org Owner에게 요청할 필요 없음.
- C. 공지만으론 강제력이 없음.

**출처:** Slack Help Center — *Manage guest access (Enterprise Grid) / org-level settings*.

---

### NO.78 — What happens to Slack accounts when removed from IdP
> **Q.** Large Corp is shutting down its Marketing team based in Europe. Deprovisioning is supported through their IdP. When Large Corp removes users from their IdP, what will happen to their Slack accounts?
> - A. Deactivated but not signed out of devices; a session reset is also required.
> - B. Deleted permanently, and all messages/files deleted too for compliance.
> - C. Deactivated, signed out on all devices, removed from channels; but only their DM messages/files are deleted.
> - D. Deactivated, signed out on all devices, removed from channels; but their messages and files won't be deleted.

**핵심 개념:** SCIM/IdP 디프로비저닝은 계정을 **비활성화 + 전 세션 로그아웃 + 채널에서 제거**하지만, **메시지·파일은 삭제하지 않는다**(별도 리텐션 정책이 없는 한).
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** 디프로비저닝은 접근을 차단하되 콘텐츠는 보존한다.
**오답 해설:**
- A. 전 세션 로그아웃이 됨(별도 리셋 불필요).
- B. 계정/콘텐츠 영구 삭제는 아님.
- C. "DM 콘텐츠만 삭제"는 부정확 — 삭제되지 않음.

**출처:** Slack Help Center — *Deactivation and deprovisioning via SCIM*.

---

### NO.79 — Two key considerations before installing an app
> **Q.** You're a Workspace Owner and App Manager for your company's Slack Enterprise Grid instance. The Human Resources (HR) team wants to pilot a Wellness app for employees. As an App Manager, what are the two key considerations you should understand before installing the app in Slack? (Select the TWO best answers.)
> - A. Is this app available in the Slack App Directory?
> - B. Does the app meet data security policies for your organization?
> - C. What external services or APIs is the app connecting to?
> - D. Does the app connect with your HR system?

**핵심 개념:** 앱 설치 전 핵심 검토는 **조직 데이터 보안 정책 부합 여부**와 **연결되는 외부 서비스/API**.
**덤프 정답:** B, C → ✅ 재판정 일치
**정답 근거:**
- B. 조직 데이터 보안 정책을 충족하는지 검토.
- C. 앱이 어떤 외부 서비스/API와 통신하는지 파악.

**오답 해설:**
- A. App Directory 등재 여부가 보안 준수를 보장하지 않음.
- D. HR 시스템 연동은 유용하나 초기 보안 평가의 핵심은 아님.

**출처:** Slack Help Center — *App review and security considerations*.

---

### NO.80 — Where to find daily/weekly active users (Business+)
> **Q.** You're a Workspace Admin for your organization's Slack Business+ instance. You need to report on the number of both daily and weekly active users within your workspace in the last 30 days. Where can you find this information? (Select the best answer.)
> - A. Org analytics dashboard · B. Workspace analytics dashboard · C. Analytics members dashboard · D. Message activity analytics

**핵심 개념:** 워크스페이스 단위 DAU/WAU는 **Workspace analytics dashboard**에서 확인. (Org analytics는 Enterprise Grid 전용.)
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** 워크스페이스 분석은 멤버·채널·활동(일간/주간 활성 사용자 포함)을 보여준다.
**오답 해설:**
- A. Org analytics는 Grid 전용.
- C. Members 대시보드는 멤버별 통계 중심.
- D. Message activity는 메시지 데이터 중심으로 활성 사용자 전반이 아님.

**출처:** Slack Help Center — *Workspace analytics overview*.

---

### NO.81 — 15 external users for a 12-month partnership
> **Q.** You're a Support Agent on the admin team for your Slack Enterprise Grid workspace. An employee requests adding 15 new members from an external company for a 12-month joint marketing partnership. How should you respond?
> - A. Advise using Slack Connect channel(s); the external org can set up a free Slack instance if needed.
> - B. Add the external users to your IdP so they authenticate via SAML SSO.
> - C. Approve and invite them as Multi-Channel Guests with a 12-month expiration.
> - D. Set up a separate Slack workspace jointly owned by both orgs.

**핵심 개념:** 조직 대 조직의 지속 협업은 **Slack Connect**가 게스트/신규 워크스페이스보다 안전·확장적. 외부 조직은 무료 Slack으로도 참여 가능.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** Slack Connect 채널로 외부 조직과 협업하면 외부인을 내 워크스페이스에 멤버/게스트로 들이지 않아도 된다.
**오답 해설:**
- B. 외부 계약자를 IdP에 넣는 것은 불필요·위험.
- C. 15명 Multi-Channel Guest는 관리 확장성이 낮음.
- D. 공동 소유 워크스페이스는 거버넌스를 복잡하게 함.

**출처:** Slack Help Center — *Slack Connect collaboration best practices*.

---

### NO.82 — Add all current+future users to a Connect workspace
> **Q.** You're the Grid Owner for your sales company's Slack Enterprise Grid instance. Departments are spread across multiple workspaces and collaborate with their customers through Slack Connect. Your company is growing quickly, and you want to have more control over external collaboration. You decide to set up an external workspace dedicated to Slack Connect channels. This workspace should include all current users, plus any future users. What is the easiest and most efficient way to go about adding users to the new workspace? (Select the best answer.)
> - A. Make the workspace a default workspace for all current and future users.
> - B. Use an org-wide default channel to introduce it and ask current Connect users to join.
> - C. Use the workspace's admin dashboard to add all users manually.
> - D. Sync all current and future users to the workspace using IdP groups.

**핵심 개념:** **기본 워크스페이스(default workspace)** 로 지정하면 현재·미래 모든 조직 멤버가 자동 추가된다 — 가장 쉬운 방법.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(A):** 기본 워크스페이스는 조직의 전원(현재+미래)을 수동 개입 없이 자동 포함한다.
**오답 해설:**
- B. 자발적 참여 요청은 누락 발생.
- C. 수동 추가는 미래 사용자를 담지 못함.
- D. IdP 그룹 동기화도 가능하나 설정·그룹 관리 부담이 더 큼("가장 쉬운"엔 A).

**출처:** Slack Help Center — *Manage default workspaces (Enterprise Grid)*.

---

### NO.83 — What members experience when SSO becomes mandatory
> **Q.** When a workspace's settings are changed to make single sign-on (SSO) mandatory, which series of events will members experience? (Select the best answer.)
> - A. A Slackbot message requiring them to click an authentication link to validate SSO.
> - B. Immediately logged out and required to authenticate via SSO before logging back in.
> - C. A notification from their SSO provider and immediate logout.
> - D. An email with a link to connect and authenticate their Slack account with their SSO provider.

**핵심 개념:** SSO를 필수로 설정하면 멤버는 **바인딩 이메일**을 받아 링크로 Slack 계정을 IdP 계정과 연결·인증한다.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(D):** 전환 시 이메일 링크로 계정을 연결하는 것이 지원되는 흐름이다.
**오답 해설:**
- A. Slackbot 링크 방식이 아님.
- B/C. 연결 완료 전 즉시 강제 로그아웃되는 흐름이 아님.

**출처:** Slack Help Center — *Manage SSO / send binding emails*.

---

### NO.84 — Which plans support Legal Holds
> **Q.** Which Slack plan(s) support the Legal Holds feature?
> - A. Business+ and Enterprise Grid · B. Free, Pro, Business+ and Enterprise Grid · C. Enterprise Grid only · D. Pro, Business+ and Enterprise Grid

**핵심 개념:** **Legal Holds는 Enterprise Grid 전용** 컴플라이언스 기능.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 높음)*
**정답 근거(C):** Legal Holds로 특정 사용자의 메시지·파일을 보존하는 기능은 Enterprise Grid에서만 제공.
**오답 해설:**
- A/B/D. Free·Pro·Business+는 Legal Holds 미지원.

**출처:** Slack Help Center — *Legal holds (Enterprise Grid)*.

---

### NO.85 — First step for regulatory compliance
> **Q.** You're an Org Owner at a financial company and administer 20 workspaces on a Slack Enterprise Grid plan. Your company is concerned about staying in compliance with government-mandated regulatory requirements across all communication tools. What is the first step you should take to ensure that communications remain compliant for your company? (Select the best answer.)
> - A. Meet with your compliance and legal teams to set policies for Slack.
> - B. Promote a member of your compliance team to Org Owner.
> - C. Implement a 24-hour retention policy.
> - D. Implement eDiscovery to archive all communications.

**핵심 개념:** 컴플라이언스는 **정책 수립이 먼저**, 기술 구현은 그 다음.
**덤프 정답:** A → ✅ 재판정 일치
**정답 근거(A):** 법무·컴플라이언스 팀과 규제 요건에 맞춘 소통·리텐션·모니터링 정책을 먼저 정해야 올바른 기술 선택이 가능.
**오답 해설:**
- B. Org Owner 승격은 정책 없이 해결되지 않음.
- C. 24시간 리텐션은 규제와 맞지 않을 수 있음(임의 설정 위험).
- D. eDiscovery는 이후 단계.

**출처:** Slack 자료 — *Compliance planning*.

---

### NO.86 — Keep mobile secure if device is lost/stolen
> **Q.** You're an Org Admin for an organization with sales associates traveling globally. You need to ensure Slack mobile access remains secure even if a device is lost or stolen. What is the best option to increase the likelihood of keeping information on mobile devices secure? (Select the best answer.)
> - A. Require users to sign out when not in use.
> - B. Require mobile devices to have a passcode.
> - C. Turn on Mobile Session Duration to auto-logout after a set time.
> - D. Do not allow Slack app download on corporate mobile devices.

**핵심 개념:** **Mobile Session Duration**으로 일정 시간 후 자동 로그아웃하면 분실·도난 시 위험을 줄인다.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(C):** 세션 자동 만료는 Slack이 제공하는 모바일 보안 통제로, 분실 기기에 남은 세션 위험을 낮춘다.
**오답 해설:**
- A. 수동 로그아웃은 신뢰성이 낮음.
- B. 패스코드는 좋은 관행이나 Slack 고유 기능이 아님(기기 정책).
- D. 앱 다운로드 금지는 소통 자체를 막음.

**출처:** Slack Help Center — *Manage mobile session duration*.

---

### NO.87 — When to revoke an EKM key
> **Q.** You are a Slack admin and you have just implemented Enterprise Key Management (EKM) within your Enterprise Grid. In which situation would it be most appropriate to revoke the key?
> - A. When a Multi-Channel Guest is invited into a workspace.
> - B. When working with contractors in a Slack Connect channel.
> - C. When sensitive information is placed in the incorrect channel and shared with other users.

**핵심 개념:** EKM 키 폐기는 **민감 정보가 잘못 노출된 경우**(예: 엉뚱한 채널 공유) 그 콘텐츠를 영구 접근 불가로 만들 때 적절.
**덤프 정답:** C → ✅ 재판정 일치
**정답 근거(C):** 부적절하게 노출된 콘텐츠를 차단하려 키를 폐기하는 것이 EKM의 대응 시나리오.
**오답 해설:**
- A. 게스트 초대는 정상적 협업 맥락.
- B. Slack Connect 계약자 협업도 정상 맥락 — 데이터 유출이 없으면 폐기 사유 아님.

**출처:** Slack Help Center — *Slack Enterprise Key Management (EKM)*.

---

### NO.88 — External contractor needs multiple channels
> **Q.** You're a Workspace Admin on a Slack Enterprise Grid plan. Your marketing team is working with an external contractor for a new product launch. The contractor does not have Slack access, and multiple internal teams need to collaborate with them. Which type of access should you recommend for the contractor?
> - A. Multi-Channel Guest with access to all relevant project channels.
> - B. Slack Connect DM between the contractor and project lead.
> - C. Single-Channel Guest with access to one project channel.
> - D. Full member with access to the marketing workspace.

**핵심 개념:** 외부 사용자가 **여러 채널**은 필요하나 워크스페이스 전체는 아닐 때는 **Multi-Channel Guest**가 적합. (한 채널이면 Single-Channel Guest — cf. NO.32.)
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(A):** 여러 팀·채널 협업이 필요하므로 Multi-Channel Guest가 워크스페이스 전체 접근 없이 필요한 채널만 부여한다.
**오답 해설:**
- B. Connect DM은 다채널 협업엔 부족.
- C. Single-Channel은 여러 채널 필요 상황엔 과소.
- D. 정식 멤버는 외부인에게 부적절.

**출처:** Slack Help Center — *Guest accounts (Multi-Channel vs Single-Channel)*.

---

### NO.89 — Approval process with least effort (Business+)
> **Q.** You're a Workspace Owner, responsible for setting up your company's Slack Business+ workspace for the first time. You want admins to have visibility into request approvals (for invites, apps, Slack Connect, etc.). What is the best way to set up an approval process within Slack that will require the least effort?
> - A. Use Workflow Builder to create multiple approval workflows from #help-slack.
> - B. Do nothing — Slack's default settings route approval requests to Workspace Admins via a Slackbot DM.
> - C. Pin a request-template message in #general asking users to submit requests there.
> - D. Set up a #admins-approval channel and route each request type there.

**핵심 개념:** Slack은 기본적으로 **승인 요청(앱·Connect·초대)을 Slackbot DM으로 Workspace Admin/Owner에게 자동 라우팅**한다 — 별도 설정 없이 최소 노력.
**덤프 정답:** B → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(B):** 기본 동작으로 승인 요청이 관리자에게 전달되므로 추가 구성이 필요 없다.
**오답 해설:**
- A/C/D. 커스텀 워크플로우·채널 구성은 "최소 노력" 요건에 어긋남(맞춤 프로세스가 필요할 때만).

**출처:** Slack Help Center — *Manage approval requests*.

---

### NO.90 — Can guests be required to use the Slack for EMM app?
> **Q.** You're an Org Admin at a security-conscious financial services company. You're rolling out Enterprise Mobility Management (EMM) across the organization. Leadership asks if it is possible to require guests to use the Slack for EMM app. How should you respond to this request? (Select the best answer.)
> - A. It's not possible to require guests to use the Slack for EMM app.
> - B. Guests are required to use the Slack for EMM app by default.
> - C. Guests can be required to use the Slack for EMM app.
> - D. Guests can only log in through the desktop app.

**핵심 개념:** **EMM 적용 대상은 정식 멤버뿐**이며, 게스트(Single/Multi-Channel)는 EMM 강제 대상이 아니다.
**덤프 정답:** A → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(A):** EMM 요건은 조직의 정식 멤버에게만 적용되고 게스트는 제외되므로, 게스트에게 Slack for EMM 앱을 강제할 수 없다.
**오답 해설:**
- B/C. 게스트를 EMM으로 통제할 수 있다는 것은 부정확.
- D. 데스크톱 전용 로그인 서술은 무관.

**출처:** Slack Help Center — *EMM and guest accounts*.

---

### NO.91 — Most important step for ease of administration
> **Q.** You're overseeing the workspace design for your organization's launch of Slack Enterprise Grid. You want to prioritize ease of administration for channels, workspaces, users, and user groups. Which is the most important step when setting up your workspaces? (Select the best answer.)
> - A. Minimize the number of multi-workspace channels.
> - B. Take into account the cultural dynamics within the company.
> - C. Ensure users can frequently and easily switch between workspaces.
> - D. Identify an appropriate set of Workspace Owners and Admins for each workspace.

**핵심 개념:** 관리 용이성의 가장 직접적 요인은 **각 워크스페이스에 적절한 Owner/Admin을 지정**하는 것(거버넌스·관리 효율).
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 적절한 관리 리더십 배치가 채널·멤버·정책 관리 효율에 가장 큰 영향을 준다.
**오답 해설:**
- A. 멀티워크스페이스 채널 최소화도 중요하나 관리 리더십만큼 직접적이지 않음.
- B. 문화 고려는 설계 요소지만 '관리 용이성'의 핵심은 아님.
- C. 잦은 워크스페이스 전환은 관리 셋업과 직접 관련 없음.

**출처:** Slack 자료 — *Enterprise Grid workspace setup*.

---

### NO.92 — Find what a former employee accessed
> **Q.** You're an Org Owner on your organization's Slack Enterprise Grid instance. An employee recently quit, and there's concern that the employee exported sensitive information prior to leaving. The security team wants to know what this former employee may have accessed. What should you do? (Select the best answer.)
> - A. Revoke the encryption key with EKM to protect the former employee's data.
> - B. Use the member analytics dashboard to confirm account activity.
> - C. Export the former employee's access logs from the admin dashboard.
> - D. Access your SIEM tool to view actions logged by the former employee.

**핵심 개념:** 상세 활동/접근 추적은 **감사 로그(Audit Logs) → SIEM 연동**으로 확인하는 것이 정확·심층적.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** SIEM(감사 로그 연동)으로 사용자 활동의 상세·이력 로그를 검토해 무엇을 했는지 파악한다.
**오답 해설:**
- A. EKM 키 폐기는 데이터를 잠글 뿐 "무엇을 접근했는지" 알려주지 않음.
- B. 멤버 분석은 활동량 통계이지 접근 상세가 아님.
- C. 관리자 대시보드에서 사용자별 접근 로그를 바로 '수출'하는 방식은 표준 기능이 아님(감사 로그 API/SIEM 사용).

**출처:** Slack Help Center — *Audit Logs API / monitoring security events*.

---

### NO.93 — Plans supporting SAML SSO (50 employees)
> **Q.** You're a prospective customer looking to purchase Slack for your organization of approximately 50 employees. You need to ensure that the plan supports SAML single sign-on (SSO) for authentication. Which plan(s) fit the requirement?
> - A. Enterprise Grid only · B. Pro, Business+, and Enterprise Grid · C. Free, Pro, Business+, and Enterprise Grid · D. Business+ and Enterprise Grid

**핵심 개념:** **SAML 기반 SSO는 Business+·Enterprise Grid**에서 지원(Free·Pro 미지원).
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 높음)*
**정답 근거(D):** SAML SSO는 Business+ 이상에서 제공되므로 D.
**오답 해설:**
- A. Grid 전용은 지나치게 좁음 — Business+도 지원.
- B/C. Pro·Free는 SAML SSO 미지원.

**출처:** Slack Help Center — *Slack plans and features (SSO)*.

---

### NO.94 — Reduce noise in #hr-benefits (sensitive info posted)
> **Q.** Medium Inc's #hr-benefits channel is a default channel designed to educate employees on benefit information and updates. However, it is now filled with requests for benefits help. Sometimes people even post sensitive personal information when asking questions. Which TWO options, combined, present the best solution to reduce noise in this channel? (Choose two.)
> - A. Limit posting permissions to Org Admins, plus specific people.
> - B. Create a private channel and implement a personal benefits workflow that doesn't broadcast sensitive info in channel.
> - C. Encourage employees to DM the HR team with questions and confidential info.
> - D. Archive the channel and create a new one.

**핵심 개념:** 소음 감소 + 민감정보 보호 = **게시 권한 제한(A)** + **비공개 채널 + 개인 벤핏 워크플로우(B)**.
**덤프 정답:** A, B → ✅ 재판정 일치
**정답 근거:**
- A. 게시 권한을 관리자+특정인으로 제한해 읽기 전용화(공지 채널 소음 제거).
- B. private 채널 + 워크플로우로 민감 질문을 공개 노출 없이 HR에 라우팅.

**오답 해설:**
- C. DM 권장은 구조적·확장적 프로세스가 아님.
- D. 아카이브는 기존 벤핏 정보 접근을 끊어 불필요.

**출처:** Slack Help Center — *Channel posting permissions / Workflow Builder*.

---

### NO.95 — Key benefit of a user group for Workspace Admins
> **Q.** Your Slack Governance Support model includes a group of people designated as Workspace Admins to distribute the workload. What is a key benefit of setting up a user group for the Workspace Admins?
> - A. Any Grid member can @mention the group from any workspace to notify all members.
> - B. Slack Connect partners can be added to the user group.
> - C. Any Slack member can add themselves to the group to follow along.
> - D. Any @mention of the group notifies all members, letting any member reach the group with questions.

**핵심 개념:** 사용자 그룹을 @멘션하면 **그룹 전원에게 알림** → 여러 사람에게 한 번에 도달.
**덤프 정답:** D → ✅ 재판정 일치 *(확신도: 중)*
**정답 근거(D):** 그룹 멘션으로 모든 멤버가 알림을 받아 질문·업데이트 전달이 쉽다.
**오답 해설:**
- A. "어느 워크스페이스에서나" 멘션은 워크스페이스/그룹 가시성 설정에 좌우되어 일반화 불가.
- B. 외부(Connect) 사용자는 사용자 그룹에 추가 불가.
- C. 사용자는 스스로 그룹에 가입할 수 없음.

**출처:** Slack Help Center — *Using user groups*.

---

### NO.96 — Two Workflow Builder triggers
> **Q.** What are two triggers that can be used to launch a workflow using Workflow Builder? (Choose TWO)
> - A. A keyword is used in a message.
> - B. A new channel is created.
> - C. A new member joins a channel.
> - D. A new member joins the workspace.
> - E. A specific date and time.

**핵심 개념:** 네이티브 WFB 트리거에는 **채널 참여(C)** 와 **지정 날짜·시간(스케줄)(E)** 이 포함된다.
**덤프 정답:** C, E → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거:**
- C. 누군가 채널에 참여할 때 워크플로우 시작.
- E. 예약된 날짜·시간에 워크플로우 실행.

**오답 해설:**
- A. 키워드는 커스텀 앱 없이는 네이티브 트리거가 아님.
- B. 채널 생성은 트리거가 아님.
- D. '워크스페이스 참여' 단독은 트리거가 아님(특정 채널 참여와 연결돼야 함).

**출처:** Slack Help Center — *Workflow Builder triggers*.

---

### NO.97 — Prevent accidental sharing of sensitive info (account numbers)
> **Q.** You're a Primary Org Owner for a bank's Slack Enterprise Grid. Your compliance team is concerned that customer service employees may accidentally share sensitive information like account numbers. What recommendation should you make?
> - A. Install an eDiscovery app to log all message content.
> - B. Integrate with a Data Loss Prevention (DLP) provider to remove sensitive data shared in Slack.
> - C. Build a bot that asks members to remove sensitive data if shared.
> - D. Designate one admin per channel to monitor and report sensitive data.

**핵심 개념:** 민감 데이터 노출을 **선제적으로 차단·격리·삭제**하려면 **DLP 통합**(Discovery API 기반)이 정답. (cf. NO.212)
**덤프 정답:** B → ✅ 재판정 일치
**정답 근거(B):** DLP는 메시지·파일을 실시간 모니터링해 패턴(계좌번호 등)을 탐지·차단한다.
**오답 해설:**
- A. eDiscovery는 아카이브용이지 노출 방지가 아님.
- C. 봇 요청은 사후 반응적.
- D. 수동 모니터링은 비효율·오류.

**출처:** Slack Help Center — *Integrate DLP with Slack (Discovery API)*.

---

### NO.98 — Free→paid upgrade recommendation
> **Q.** You're a Workspace Owner at a small business that used Slack's Free plan in their first year. However, its business is growing fast enough to justify upgrading to a paid plan. The requirements: * Users want to be able to access their old messages and integrate Slack with their calendars. * You want to use Okta to provision users in order to provide additional security and simplicity to the employee onboarding process. * Field representatives need to be able to access Slack securely on their company-owned mobile devices. Based on the requirements, what should you recommend? (Select the best answer.)
> - A. Stay with the Free plan · B. Move to Pro · C. Move to Business+ · D. Move to Enterprise Grid

**핵심 개념:** 전체 히스토리 + SAML SSO(Okta) 프로비저닝 + EMM(모바일 보안)을 모두 충족하는 최적 플랜은 **Business+**. Grid는 과함.
**덤프 정답:** C → ✅ 재판정 일치 *(확신도: 중-높음)*
**정답 근거(C):** Business+는 전체 메시지 히스토리, Okta 등 SAML SSO 프로비저닝, EMM/MDM을 제공한다.
**오답 해설:**
- A. Free는 히스토리·SSO·EMM 요건 미충족.
- B. Pro는 SAML SSO(Okta)·EMM 미지원.
- D. Enterprise Grid는 소규모 성장 기업엔 과도.

**출처:** Slack Help Center — *Slack plans and features*.

---

### NO.99 — Custom emoji: CIO hesitant, doesn't want admin burden
> **Q.** A 5,000-employee company with multiple international offices is planning to launch Slack to its entire organization. Their goal is to increase collaboration and build a stronger company culture. The CIO is hesitant to allow members to upload custom emoji to Slack, but she doesn't want to burden her Workspace Admin team with requests for custom emoji uploads. Which solution addresses the CIO's concerns?
> - A. Allow all members to upload custom emoji, but communicate/document appropriate use.
> - B. Pre-load a set of custom emoji voted on by a council of leaders, and don't allow anyone to request uploads.
> - C. Do not allow any custom emoji creation.
> - D. Restrict custom emoji uploads to Workspace Owners/Admins, and don't allow anyone to request uploads.

**핵심 개념:** CIO의 두 우려는 ①멤버 업로드에 대한 거부감(부적절 이미지 리스크) ②관리자에게 요청 부담을 지우고 싶지 않음. 두 가지를 모두 충족하려면 **사전 큐레이션된 세트를 배포하고 요청은 받지 않는** 방식이 맞다.
**덤프 정답:** A → ⚠️ 재판정 불일치 (내 판단: **B**) *(확신도: 중)*
**정답 근거(B):** 리더 협의체가 선정한 이모지를 사전 로드하고 업로드 요청을 막으면, 부적절 콘텐츠 리스크(①)와 관리자 요청 부담(②)을 동시에 해소한다.
**왜 덤프 A가 어긋나나:** A는 "전 멤버 업로드 허용"인데, 이는 CIO가 명시적으로 **"멤버 업로드를 꺼린다"** 는 전제와 정면 배치된다. 가이드라인만으로는 부적절 업로드 리스크를 근본 차단하지 못한다.
**오답 해설:**
- A. CIO의 우려(멤버 업로드)를 그대로 허용 — 문항 요구 위배.
- C. 이모지를 전면 금지하면 회사의 '문화 구축' 목표를 훼손(균형 상실).
- D. 관리자에게 업로드를 몰아주는 형태로, 문화적 다양성 확보 측면에서 B(협의체 큐레이션)보다 약함.

**출처:** Slack Help Center — *Manage custom emoji permissions*. (판단형 문항 — 시나리오의 CIO 우려 해소 관점.)

---

### NO.100 — Which provider is "required" for Pro plan SSO?
> **Q.** Your organization recently purchased the Slack Pro plan. As the IT lead, you're responsible for setting up single sign-on (SSO). Which provider is required for the Pro plan? (Select the best answer.)
> - A. G Suite Auth · B. Azure SAML · C. Auth0 · D. Okta

**핵심 개념:** Slack **Pro는 SAML SSO를 지원하지 않고**, Google Workspace(구 G Suite) 로그인 정도만 사용 가능. SAML provider(Azure·Okta·Auth0)는 Business+·Enterprise Grid에서 쓰인다.
**덤프 정답:** A → ⚠️ 재판정 논란 (보기 중 최선은 A, 그러나 전제가 부정확) *(확신도: 중)*
**정답 근거:** 보기 중 Pro에서 유일하게 사용 가능한 것은 Google(G Suite)이므로 **정답으로는 A**가 맞다. 다만 문제의 "**required(필수)**" 프레이밍은 부정확 — Pro에서 SSO는 필수가 아니고 특정 provider가 강제되는 것도 아니며, Google 로그인은 "지원"될 뿐이다. 진정한 SAML SSO가 필요하면 Business+ 이상이어야 한다.
**오답 해설:**
- B. Azure SAML — SAML은 Business+ 이상.
- C. Auth0 — SAML provider로 Business+ 이상.
- D. Okta — SAML provider로 Business+ 이상.

**출처:** Slack Help Center — *Slack plans and features (SSO by plan)* / *Configure SAML SSO*.

---

> **파일 완료: NO.51~100.** 다음 파일 `slack-admin-dump-101-150.md` 로 이어집니다.
