---
name: seele-creator-sourcing
description: Use when finding, validating, deduplicating, grading, contacting, negotiating with, or tracking YouTube/TikTok creators for SEELE AI, including audience evidence, quotes, Briefs, production, payment, and dashboards.
---

# KOL

## Objective

Find creators who can make target users believe: “I can use SEELE to build and play a game.” Optimize for qualified, explainable experiments rather than raw list volume.

## Required references

Read only the references needed for the current action:

- Discovery or grading: `references/sourcing-rules.md` and `references/search-keywords.md`.
- First outreach: `references/outreach-style.md`.
- Reply, quote, Brief, rights, approval, production, or payment: `references/quote-review.md`.
- First- or second-round negotiation: `references/negotiation-playbook.md`.
- Inbox status, dashboard lanes, ownership, or weekly attribution: `references/workflow-state.md`.
- CSV/XLSX/master-data fields: `references/output-schema.md`.

## Stable sourcing gates

- Treat search results as leads; open and verify every included profile and representative item.
- Review up to 10 recent relevant, non-pinned long-form items. Record sample size and median after excluding unrelated items and obvious outliers.
- Grade A requires at least 6 relevant samples. Grade B may use 4–5 when email, deduplication, activity, safety, relevance, and the required median-view gate all pass. Fewer than 4 does not enter send-ready output.
- Evaluate UGC delivery, game-creation motivation, audience overlap, product persuasion, communication efficiency, and commercial executability.
- Verify a public business email or explicit DM route. Never guess contact details, audience location, views, or content evidence.
- Normalize Channel ID/profile URL/email and deduplicate against the batch, master database, historical cycles, Pass list, and real sent-mail history.
- Respect the task’s current platform, quantity, language, market, and median-view threshold. Never lower evidence, safety, or deduplication gates merely to fill quota.

## Outreach and reply invariants

- A/B creators may enter first-contact preparation when all send-ready gates pass; B must state the exact remaining uncertainty.
- Actual sending requires explicit authorization for that workflow. Mark `已触达` only after a real sent record exists; preserve failures, bounces, skips, and drafts truthfully.
- A quote, rate card, question, counteroffer, refusal, script, video, or payment message all count as replies.
- Preserve original message, Chinese summary, sender, Beijing time, quote history, audience evidence, and next action.
- Never infer “waiting for us” from unread status. Use `references/workflow-state.md`.

## Quote and cooperation invariants

- Keep Dedicated and Integration prices separate; default to evaluating Dedicated when the user has not chosen a format.
- Quotes at or above USD 1,000 are Pass unless the user explicitly overrides that creator.
- After first-round negotiation, a price still above USD 500 is Pass under the current default; explicit creator-specific user decisions override.
- Show proposed first- and second-round counters to the user before sending unless the user has explicitly delegated that exact action.
- Price never authorizes acceptance, contract, schedule promise, Brief/access delivery, rights grant, or payment. These remain distinct approvals.
- Unknown fields stay `待确认`; do not convert creator location, phone prefix, or comment language into audience fact.

## Data and dashboard contract

- Maintain one canonical creator record per stable `creator_id`, with append-only event evidence.
- Use one action dashboard with four lanes: `待我回复`, `等待达人`, `待 MT 决定`, `合作执行中`.
- Quote round is a card field, never a separate lane.
- Use one weekly view for metrics; do not duplicate creator detail cards across competing dashboards.
- Preserve Pass/completed/history in collapsed archive data. Do not silently reactivate a Pass record.
- Every active card must show profile, current price and quote round, audience evidence, latest-message sender and Beijing date, next action, and owner.

## Output

Report actual discovered, opened/verified, rejected, deduplicated, A/B, sent-success, bounce, effective-contact, reply, and remaining-gap counts. For MT-facing creator summaries always include profile link, Dedicated/Integration price history, audience percentages with evidence period, current progress, latest-message sender, and latest-message Beijing date.

## Safety

- Use public information and compliant sources. Do not bypass login, CAPTCHA, limits, or platform controls.
- Do not extract browser cookies or fabricate proof.
- Do not write to Feishu, send non-authorized follow-ups, approve cooperation, or initiate payment without the appropriate explicit request.
- Keep recovery copies before rewriting dashboard data; archive old dashboards by moving, not deleting.
