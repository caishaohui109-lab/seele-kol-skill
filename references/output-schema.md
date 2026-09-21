# Output schema

The exporter writes the following columns in this exact order:

`Creator ID, 达人名称, 平台, 主页链接, 国家/语言, 粉丝数, 近期相关内容样本量, 中位播放, 内容标签, 代表内容链接, 公开商务邮箱, 建议触达渠道, 达人类型, UGC交付能力, 游戏创作动机, 受众重合度, 产品说服力, 单位传播效率, 商务可执行性, 推荐拍摄方式, 推荐内容切角, 具体测试场景, 实验假设, 测试价值, 与现有达人同质性, 推荐等级, 推荐理由, 风险或待确认项, 人工复核重点, 个性化私信草稿, 报价USD, 预估CPM, 数据核验日期, 人工确认状态, 触达状态`

## Allowed values

- 平台: `TikTok`, `YouTube`
- 推荐等级: `A`, `B`, `C`, `Pass`
- 人工确认状态: `待确认`, `通过`, `驳回`
- 触达状态: `待触达`, `已触达`, `已回复`, `有兴趣`, `已报价`, `谈判中`, `待团队审批`, `已确认`, `已拒绝`, `无回复`
- Six review dimensions: `明确符合`, `部分符合`, `不符合`, `信息不足`

Unknown facts remain blank or are marked `待确认`. Never guess an email, country, audience demographic, view count, or representative-content URL.

## Optional quote-review fields

When a creator has replied with a quote or cooperation terms, append these fields to the working sheet or progress board without changing the baseline exporter field order:

`报价合作形式, Dedicated 初始报价, Integration 初始报价, 当前优先形式, 报价拆分备注, Brief状态, Brief缺失项, CPM计算依据, SOP评分总分, 报价判断, 合理价格下限, 合理价格上限, 合理价格区间, 合理价格区间依据, 第一轮还价, 第一轮发送时间, 第一轮回复, 第二轮还价, 第二轮用户确认状态, 第二轮发送时间, 第二轮回复, 可能地区, 地区证据来源, 地区证据可信度, 地区调整幅度, 最终价格, 最终审批状态, 最终交付范围, 最终使用权, 谈价方案, 审批状态, 下一步动作, 最新回复时间, 我方最近发送时间`

Allowed guidance:

- 报价合作形式: `Sponsored Integration`, `Dedicated Video`, `Shorts`, `直播`, `多条打包`, `Affiliate`, `固定费`, `效果费`, `固定费+效果费`, or `待确认`.
- Brief状态: `满足`, `部分满足`, `范围不完整`, `不满足`, or `待确认`.
- 报价判断: `合理`, `有条件合理`, `偏高但可谈`, `不建议推进`, or `待确认`.
- 当前优先形式: `Dedicated Video`, `Sponsored Integration`, or `待确认`. Default to Dedicated and retain both price histories when Integration becomes the fallback.
- 第二轮用户确认状态: `不适用`, `待确认`, `已确认发送`, or `拒绝发送`.
- 地区证据可信度: `低`, `中`, or `高`. A phone country code alone is `低`; never store the full phone number.
- 地区调整幅度: `0%`–`15%`; it cannot exceed 15% or become the sole price justification.
- 最终审批状态: `首次报价`, `第一轮待确认`, `第一轮谈判中`, `第二轮待确认`, `第二轮已发送`, `≤500 可推进`, `500–999.99 待团队审批`, `≥1000 Pass`, or `停止推进`.
- 审批状态: `可按团队流程推进`, `待团队审批`, `已通过`, `已拒绝`, `Pass`, or `待确认`. Dedicated or Integration quotes at or above USD 1,000 are `Pass`; only quotes below that hard ceiling use the final negotiated USD 500 approval boundary.
- Timestamps must include timezone when known; do not normalize away the original message time.
- Missing quote components, rights, engagement, audience, or tax data remain `待确认` and are not filled from assumptions.

## Canonical workflow fields

The creator master and dashboard data must preserve these stable machine fields:

`creator_id, discovery_cycle, first_contact_cycle, current_stage, quote_round, latest_message_direction, latest_message_at_bjt, latest_message_id, thread_id, next_owner, next_action, event_cycle`

- `creator_id`: immutable identity, preferably YouTube Channel ID.
- `discovery_cycle`: cycle in which the creator was first found.
- `first_contact_cycle`: immutable cycle derived from the first verified sent record.
- `current_stage`: current business stage; history remains in events.
- `quote_round`: `未报价`, `首次报价`, `第一轮后`, `第二轮后`, or later rounds as observed.
- `latest_message_direction`: `我方` or `达人`, based on the last actual human message.
- `latest_message_at_bjt`: Beijing-time timestamp used in reporting.
- `latest_message_id` and `thread_id`: source evidence for replay and deduplication.
- `next_owner`: `我`, `达人`, `MT`, `财务`, or `制作`.
- `next_action`: one concrete action, not a status paragraph.
- `event_cycle`: cycle in which each event occurred; it never replaces `first_contact_cycle`.
