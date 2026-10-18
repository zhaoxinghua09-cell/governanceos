# AGENTS.md — 给 AI Agent 的工作指引

本文件面向自动化 AI Agent（编码助手、技能加载器、文档维护机器人）。人类读者请看 [README.md](README.md)。

## 这个仓库是什么

`governanceos` 是一个 **方法论合集（collection）**，不是可运行的 SDK，也不内嵌任何子技能的内部实现。核心资产是 `SKILL.md`（遵循 Agent Skills 规范，带 YAML frontmatter）与一个只读路由脚本 `scripts/governance_flow.py`。它按 slug 把你路由到 9 个已独立发布的治理子技能（红队、注入防护、泄漏扫描、文档脱敏、停机开关、技能质量门、发布门、徽章签发/核验）。

## 可用的工作命令

```bash
# 列出全生命周期（4 阶段、9 子技能）
python3 scripts/governance_flow.py --list

# 查某个阶段或 slug 怎么调
python3 scripts/governance_flow.py --route plan
python3 scripts/governance_flow.py --route lgd-badge-verify

# 打印 LGD 三律实时状态行
python3 scripts/governance_flow.py --badge
```

前置依赖：Python 3。无第三方包、无网络调用、无业务数据写入。

## 约定（Do）

- 修改前先读 `SKILL.md` 的 YAML frontmatter，**保持字段兼容**（`name` / `slug` / `version` / `license` 等）。
- 新增或调整子技能路由时，同步更新 `README.md` 与 `SKILL.md` 中的入口索引表，并保持双语（EN/ZH）一致。
- 改动路由脚本后，跑 `python3 scripts/governance_flow.py --list` 确认 rc=0、表项完整。

## 禁止（Don't）

- 不要改动 `SKILL.md` 的 `copyright` / `author` / `license_scope` 字段，也不要改 `LICENSE` / `LICENSE-CONTENT` 的权利主体——**权属字段只由维护者变更**。
- 不要把任何子技能的内部实现复制进本仓；本仓只按 slug 引用。
- 不要在仓库内提交任何密钥、令牌或真实业务数据。
- 不要声称本仓「已认证 / 已商用交付 / 已服务特定客户」；评测与下载数据为指定快照时点，勿改写。

## 边界

本仓专注智能体治理**方法论编排与路由**；不重写安全工具、不代执行发布动作、不托管子技能包（分发走各自远端）。
