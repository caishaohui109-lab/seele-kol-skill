# Workflow state contract

Use this contract for inbox review, progress summaries, master-data updates, and dashboards.

## Source of truth

- Determine conversation direction from the sender of the **最后一封实际邮件** in the thread.
- Ignore bounces, automated notices, drafts, labels, and UI read state. **不以已读/未读**判断是否需要回复。
- Store the supporting message ID, thread ID, sender direction, original timestamp, and Beijing-time display value.
- If sending result is uncertain, inspect the real sent record before retrying or changing status.

## Four exclusive action lanes

Every active creator appears once:

- **待我回复**: the creator sent the last human message and no MT/finance/production prerequisite blocks us.
- **等待达人**: our side sent the last human message and the next response/action belongs to the creator.
- **待 MT 决定**: `next_owner=MT`, regardless of which side sent the latest email.
- **合作执行中**: cooperation is approved or work is in Brief, script, product access, video, invoice/payment, publication, or reporting. Owner may be `我`, `达人`, `MT`, `财务`, or `制作`, but the lane stays cooperation.

`Pass` and `completed` go to collapsed history. A new email does not automatically reactivate a Pass creator; only an explicit user decision does.

## Quote rounds

Quote round is evidence displayed on the card, not an action lane. Preserve every initial quote, our counter, creator counter, acceptance/refusal, and timestamp. Labels may be `首次报价`, `第一轮后`, `第二轮后`, `第三轮后`, or `未报价`.

## Identity and cycles

- `creator_id` must be stable. Prefer YouTube Channel ID; otherwise use normalized canonical profile plus verified public business email.
- `first_contact_cycle` is immutable after it is verified from a real sent record.
- Weekly cycles run Beijing-time Friday 00:00 through Thursday 23:59:59 and use `YYYY-MM-DD至YYYY-MM-DD`.
- Each reply, quote, Brief, script, video, payment, or publication event receives its own `event_cycle` based on event time.
- A creator replying two weeks later remains attributed to the original `first_contact_cycle`; the reply also counts as a cross-cycle event in its new `event_cycle`.
- Never invent dates from filenames or the current date. Unknown historical dates remain `待核验`.

## Required active-card fields

Each card displays:

1. Creator name and profile link.
2. Current quote plus quote round.
3. Audience countries/percentages and evidence status.
4. Latest-message sender (`我方` or `达人`) plus Beijing date.
5. Next action.
6. Current owner.

Put source excerpts, rights, payment details, and full history inside collapsed details rather than the main card.

## Update order

1. Read the entire relevant thread and locate the last actual human message.
2. Append immutable event evidence.
3. Update current quote/stage/next action without overwriting price history.
4. Derive owner and exactly one action lane.
5. Rebuild action and weekly views from the same canonical master.
6. Check uniqueness, card totals, links, and timestamps before reporting synchronization.
