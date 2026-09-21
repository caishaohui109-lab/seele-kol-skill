# SEELE Creator Quote Review

Use this reference whenever a creator replies with interest, a rate card, a quote, a scope question, a Brief confirmation, a negotiation point, or post-campaign delivery data.

## Source boundaries

- The SEELE creator Brief supplies hard product-exposure, duration, placement, CTA, disclosure, and acceptance requirements.
- The SEELE KOL SOP supplies the screening scorecard, median-view/CPM logic, negotiation exchanges, Deal Memo, approval, and review principles.
- The user's current hard quote ceiling is USD 1,000 for both formats. A Dedicated Video or Sponsored Integration quote at or above USD 1,000 is `Pass` before negotiation. Below that ceiling, a final negotiated price above USD 500 is `待团队审批`; a price at or below USD 500 is `可按团队流程推进`. These are current operating rules, not fixed thresholds in the four supplied documents. Price status does not itself authorize acceptance or commitment.
- Unknown facts stay `待确认`; never guess audience, engagement, rights, fee components, tax, or delivery terms.
- This reference does not replace a contract, legal/compliance review, finance approval, or platform policy.

## Required output card

Always report in this order:

1. One-line conclusion.
2. Creator/channel and main content business.
3. Cooperation format and quoted amount.
4. Reply timeline: our latest send time, creator reply time, and timezone.
5. Brief hard-gate checklist and missing items.
6. Relevant content evidence: sample count, median views, relevant-content ratio, interaction quality, and representative URLs.
7. Price math: CPM/CPV and the reference range.
8. SOP fit score with evidence; do not fill unsupported dimensions.
9. Commercial, rights, safety, payment, and delivery risks.
10. Verdict: `合理`, `有条件合理`, `偏高但可谈`, or `不建议推进`.
11. Negotiation exchange plan and a draft reply; do not send or promise acceptance without user confirmation.
12. Approval status and the next action.

## Step 0: Capture the reply

Treat every substantive reply as a reply, including a direct quote, a rate card, a question, a counteroffer, or a rejection. Record:

- original message and Chinese translation;
- our latest sent timestamp;
- creator's received/replied timestamp;
- timezone or source timezone;
- current status: `已回复`, `已报价`, `谈判中`, `待团队审批`, `已确认`, `已拒绝`, or `无回复`;
- next action and follow-up date.

Never overwrite an older quote without preserving the original amount and date.

## Step 1: Classify the cooperation format

Do not compare prices until the format is explicit. Record Dedicated and Integration amounts separately and default to Dedicated Video; use Integration only when Dedicated pricing or execution is not supportable:

- `Sponsored Integration`: a continuous independent product segment inside a regular video;
- `Dedicated Video`: the video is built around SEELE and the product process;
- Shorts, livestream, multi-video bundle, affiliate, gifting, fixed fee, performance fee, or hybrid.

If the creator says only “one video” or mixes “6–10 minutes” with “90-second integration,” mark the scope `合作范围不完整` and ask which format the quote covers.

### Hard price ceiling

- Dedicated Video quote `>= USD 1,000`: mark the offer and creator `Pass` with reason `Dedicated 报价达到硬上限`.
- Sponsored Integration quote `>= USD 1,000`: mark the offer and creator `Pass` with reason `Integration 报价达到硬上限`.
- Apply this gate to the creator's explicit current quote before CPM analysis, negotiation, or team approval.
- Do not send a counteroffer, move the offer into team approval, or use a cheaper Integration fallback to rescue a Dedicated quote that hit the ceiling unless the user explicitly asks for an exception for that creator.
- Preserve the original quote, format, date, and Pass reason in the database and dashboard.

## Step 2: Apply the Brief hard gates

### Sponsored Integration

Mark each item `满足`, `待确认`, or `不满足`:

- continuous independent segment of 60–90 seconds;
- SEELE AI and the task spoken within the first 10 seconds of the segment;
- segment starts within the first 35% of the video and no later than the first five minutes;
- at least 30 seconds of real SEELE Workspace operation;
- at least 10 seconds showing a playable result;
- one clear CTA;
- below 60 seconds or above 90 seconds only with written approval (up to 120 seconds when approved).

### Dedicated Video

- total video is at least six minutes;
- valid SEELE content is at least 60% and at least four minutes;
- “SEELE AI” and the task are clear within the first 30 seconds;
- real SEELE Workspace appears within the first 25% of the video;
- the video shows `input → generate → modify/choose` with corresponding evidence;
- final playable result and CTA appear before the end.

### What counts as valid exposure

- clear spoken or readable SEELE AI name;
- real Workspace operation;
- the Prompt/material input corresponding to the final work;
- real generation, modification, iteration, and playtest;
- a final result that can be matched to the shown process.

### What does not count

- logo-only exposure or a sponsor mention only at the opening/closing;
- unrelated footage, concept video, CG, or third-party content presented as SEELE output;
- Prompt, Workspace, and final work that do not correspond;
- praise without a verifiable creation process.

Also check clear commercial disclosure (`Sponsored`, `Paid Partnership`, `Affiliate`, or local equivalent), one primary CTA, and authorized links. Disclosure cannot be hidden only in a collapsed area or a block of hashtags.

## Step 3: Decompose the quote

Separate the creator's total into:

- production and organic publishing fee;
- platform/advertising authorization;
- paid usage and whitelisting;
- exclusivity and territory;
- raw files and secondary edits;
- rush delivery, multilingual versions, or additional platforms;
- script/concept/rough-cut/final review and revision rounds;
- taxes, payment/platform fees, cancellation, and postponement terms.

If an item is not stated, write `待确认`, not an industry assumption.

## Step 4: Build the evidence set

Use 10 recent relevant non-pinned posts where possible (at least six). Exclude unrelated posts and obvious outliers, and record the sample count. Collect:

- relevant-content median views;
- relevant-content ratio among recent posts;
- interaction rate by views: `(likes + comments + shares) ÷ views` when the platform exposes the fields;
- effective-comment quality: real questions/discussion versus bots, mutual likes, or emoji-only comments;
- posting recency and stability;
- audience country/language evidence when available;
- representative URLs and screenshots/data dates.

Do not use follower count, one viral video, or a simple unlabelled average as a substitute for relevant median views.

## Step 5: Calculate price value

Only run this step for quotes below the hard USD 1,000 ceiling or for a user-approved exception.

Use:

```text
estimated CPM = quoted organic fee ÷ relevant median views × 1,000
estimated CPV = total creator cost ÷ effective views
base media value = relevant median views ÷ 1,000 × reference CPM
```

The SOP reference for YouTube long-form is generally `$5–10 CPM`, with `$5–15` as the Europe/US reference. Treat this as a media baseline, not an automatic price ceiling. Show separately:

- media value supported by views;
- production value supported by the required demonstration;
- audience scarcity, brand safety, and asset-reuse premium;
- rights value supported by paid usage, whitelisting, exclusivity, or raw assets.

If the quote is far above the reference, state what evidence would justify the premium. If there is no evidence, label it `偏高`.

## Step 6: Score creator fit using the SOP

Use the seven dimensions, with evidence for every score:

| Dimension | Points |
|---|---:|
| Audience-market match | 20 |
| Content-product match | 20 |
| Playback quality/stability | 15 |
| Interaction/community quality | 10 |
| Product demo/narrative ability | 15 |
| Brand safety/compliance | 10 |
| Cost/delivery reliability | 10 |

Thresholds: `≥80` priority, `70–79` candidate, `60–69` special opportunity only, `<60` no cooperation. Any brand-safety redline vetoes the total score. If evidence is missing, mark the dimension `信息不足` rather than awarding points.

Fit before reach: AI game development, indie game, game-jam, Unity/Unreal/Godot, AI creation, and no-code creation are stronger matches than general game highlights or news. A stable 5K+ relevant median with real comments is an execution reference, not a replacement for product fit.

## Step 7: Check commercial execution and risk

Confirm:

- creator or agency identity and payment entity;
- schedule, response speed, and history of on-time delivery;
- revision limits and review deadlines;
- payment method, tax, invoice, and cancellation;
- content ownership, usage period, territory, exclusivity, paid ads, and whitelisting;
- third-party IP, music, images, people, and game assets;
- advertising disclosure and AI-generated-content labeling;
- no fake traffic, automated clicks, self-referrals, or deceptive incentives.

Product access, product facts, and current capabilities must be verified before the Brief. Blocking product bugs must be resolved before similar content is scheduled.

## Step 8: Classify the quote

- `合理`: scope is complete, hard gates are met, the CPM/production/rights value is explainable, and commercial risk is controlled.
- `有条件合理`: media CPM is high, but strong fit, scarce audience, exceptional demonstration, or reusable rights provide evidence for the premium; list the conditions.
- `偏高但可谈`: content fit is good but the quote is not supported by current reach or rights; propose scope exchanges.
- `不建议推进`: hard Brief failure, poor audience fit, brand-safety redline, suspicious data, or high price without evidence. A quote at or above the operating hard ceiling is recorded as `Pass`, not merely `偏高但可谈`.

## Step 9: Negotiate without changing the experiment unknowably

Load `negotiation-playbook.md` for the counter amount, phone-country-code boundary, two-round sending authorization, stopping rule, and exact message templates. Do not change creator type, format, angle, and deliverables at the same time if the goal is to learn which variable works. Use one or two controlled exchanges:

- shorten usage period;
- remove or reduce exclusivity;
- change dedicated video to integration;
- adjust duration or delivery specification while retaining hard Brief gates;
- reduce revision rounds;
- extend timeline;
- bundle multiple videos;
- use a fixed fee plus a performance component.

Write the proposed fee, retained deliverables, removed rights, and approval requirement. A high-fit creator with a high quote should receive a negotiation plan, not only “太贵了”.

## Step 10: Approval and Deal Memo

The user's operating rules are:

- Dedicated Video or Sponsored Integration quote at or above USD 1,000: `Pass` before negotiation or approval;
- final negotiated price at or below USD 500: `可按团队流程推进`;
- final negotiated price above USD 500 and below USD 1,000: `待团队审批` before accepting or committing.

Neither status authorizes automatic acceptance, signing, schedule promises, Brief/product-access delivery, payment, or rights grants.

The SOP additionally requires second approval for over-budget changes, new rights, or schedule changes. Before contracting, write a Deal Memo covering:

- subject, channel, contact, payment entity/country;
- platform, quantity, duration, language, date, link location, and CTA;
- creative must-show/must-avoid and real-experience allowance;
- concept, script, rough cut, final review deadlines and revision rounds;
- natural publishing period, ads, whitelisting, editing, territory, term, exclusivity;
- currency, tax, payment milestones, invoice/fees, cancellation;
- data screenshots, T+1/T+7/T+30 fields, attribution link/code;
- disclosure, AI label, IP/privacy, removal and repair rules.

Never treat an email promise as final until it is written into the Deal Memo or contract.

## Step 11: Publish acceptance and review

Before payment, verify:

- public URL and agreed public-retention period;
- product process, final result, CTA, link, pinned comment, and disclosure;
- no watermark, black frames, wrong text, sensitive data, unauthorized IP, or false product claim;
- agreed ad code/whitelisting/raw assets are delivered;
- no anomalous traffic or clicks.

Record:

- `T+1`: launch proof, views, exposure, engagement, link status, early comments;
- `T+7`: views, engagement rate, clicks, registrations, activations, subscriptions/revenue;
- `T+30`: long-tail views, attributed conversion, refunds/risk, revenue, and asset reuse.

End with a reusable grade: `A 核心伙伴`, `B 可复用`, `C 观察`, or `D 停止`, supported by evidence and a re-invest/stop recommendation.

## Compact output template

```text
【报价判断】
达人/主页：
主业与受众：
报价合作形式：
报价与拆分：
我方发送时间 / 对方回复时间：

【Brief 核对】
满足项：
待确认项：
不满足项：

【数据与价格】
相关样本量：
相关内容中位播放：
互动/评论证据：
估算 CPM/CPV：
SOP 参考：

【结论】
匹配度与证据：
商务/版权/合规风险：
报价判断：
谈价方案：
审批状态：
下一步：
```
