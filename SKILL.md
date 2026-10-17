---
name: governanceos
display_name: GovernanceOS
display_name_en: GovernanceOS
slug: governanceos
title: GovernanceOS — 一套方法论解决治理全流程（One OS for the full governance loop）
version: 1.0.0
description: "One operating system for the full AI-agent governance lifecycle: SPEC -> PLAN -> GATE -> AUDIT. Orchestrates 9 independently published governance sub-skills by slug (red-team drill, injection shield, leak scan, document desensitization, kill-switch, badge issue/verify, skill & publish quality gates); does not vendor their internals. LGD three-laws (registered / evidenced / gated) embedded as live badges. Use when the user wants an end-to-end governance plan, a pre-launch security audit, or a release-compliance review."
description_zh: "一套操作系统跑通智能体治理全生命周期：SPEC -> PLAN -> GATE -> AUDIT。按 slug 编排 9 个已独立发布的治理子技能（红队演练、注入防护、泄漏扫描、文档脱敏、停机开关、徽章签发/核验、技能质量门、发布门），不内嵌子包内部实现。LGD 三律（有籍/有证/有门禁）以实时徽标内嵌。当用户要治理方案、上线前安全审计或发布合规评审时使用。"
description_en: "One operating system for the full AI-agent governance lifecycle: SPEC -> PLAN -> GATE -> AUDIT. Orchestrates 9 independently published governance sub-skills by slug; does not vendor their internals. LGD three-laws embedded as live badges."
read_when:
  - 用户要一套智能体治理/安全合规的端到端方案或生命周期路线图（spec→plan→gate→audit）
  - 上线前要做安全审计：红队、注入防护、泄漏扫描、文档脱敏、停机卡
  - 发布合规评审：技能质量门、发布门、徽章凭证签发与核验
  - 用户说「治理全流程怎么跑」「发布前要过哪些门」「给我一套治理方法论/治理操作系统」
agent_created: true
author: SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中方法论文本不在 MIT 覆盖范围内
allowed-tools: Read, Grep, Bash
category: AI 治理
platforms: [windows, macos, linux, cli]
copyright: SynomosAI
homepage: https://zhaoxinghua09-cell.github.io/lgd-skills-index/
classification:
  skillhub: ["security-compliance"]
  iso_25010: ["Security"]
risk_tier: low
risk_rationale: "纯文档编排 + 只读路由脚本：不调用外部 API、不读写业务数据、不代执行发布动作；仅按 slug 索引已有子技能。"
tags: [governance, 治理, security, red-team, method-suite, quality-gate, badge, collection, lifecycle, governanceos]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/governance_flow.py
  runtime: python3
  call_pattern: args
input_schema:
  args:
    type: string
    description: "--list 列出全生命周期四阶段与九个子技能；--route <phase|slug> 给出该环节调用说明与预期输出；--badge 打印 LGD 三律当前达标状态"
    required: false
output_schema:
  stdout: 路由表（阶段 | slug | 何时用 | 调用说明 | 预期输出）或三律状态行
  exit_code: "rc=0 正常；rc=2 未知阶段/slug"
changelog: "1.0.0: Collection-repo upgrade of governance-method-suite (v1.0.1) to the GovernanceOS shape — lifecycle-anchored SPEC->PLAN->GATE->AUDIT orchestration, one-page ASCII pipeline, live LGD three-law badge line, quantified evidence bars, multi-vendor plugin shims."
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate

## English

### What this is
**GovernanceOS** is a *methodology collection* — one operating system that wires the full AI-agent governance lifecycle end to end. It does **not** re-implement security logic: it routes you, phase by phase, to 9 sub-skills that are already published and maintained on their own. Treat this repo as the table of contents; the sub-skills are the chapters.

Differentiator vs. every external collection (superpowers / ECC / caveman): we ship **theory + skills + evidence chain + supervision charter** in one place — the LGD three-laws (registered / evidenced / gated) are embedded, not bolted on.

### One-page lifecycle pipeline

```
 GOVERNANCEOS — one lifecycle, nine sub-skills, three laws embedded

   SPEC                PLAN                    GATE                   AUDIT
 ┌───────────┐   ┌───────────────────┐   ┌────────────────────┐   ┌──────────────────┐
 │ define    │──▶│ attack & defend:  │──▶│ two quality gates:  │──▶│ provenance &     │
 │ scope &   │   │ agent-redteam-    │   │ skill-quality-gate │   │ ledger: badge-   │
 │ charter   │   │ kit -> prompt-    │   │ -> publish-quality │   │ issuer -> badge- │
 │           │   │ injection-shield  │   │ -gate (+ doc-      │   │ verify           │
 │           │   │ -> prompt-leak-   │   │ desens-scanner &   │   │                  │
 │           │   │ scanner -> doc-   │   │ agent-kill-switch  │   │                  │
 │           │   │ desens-scanner -> │   │ as hard stop)      │   │                  │
 │           │   │ agent-kill-switch │   │                    │   │                  │
 └───────────┘   └───────────────────┘   └────────────────────┘   └──────────────────┘
        \                 \                        \                       /
         \_________________\______ LGD three-laws embedded ______________/
                 [ REGISTERED 有籍 ] 113/113 packages · 100.0%
                 [ EVIDENCED  有证 ] 112/113 packages ·  99.1%
                 [ GATED      有门禁 ] 112/113 packages ·  99.1%
                 (dashboard snapshot 2026-10-17; all 9 sub-skills below = overall GREEN)
```

### Entry index (phase | slug | when to use | expected output)

| # | Phase | Sub-skill slug | LGD badge | When to use | Expected output |
|---|-------|----------------|-----------|-------------|-----------------|
| 1 | SPEC | _(this suite)_ | — | Define governance scope & supervision charter before building | Scope + charter pinned; every later phase references it |
| 2 | PLAN | `agent-redteam-kit` | GATED | Before launch: stress-test the agent adversarially | Scored attack-surface report + fix list |
| 3 | PLAN | `prompt-injection-shield` | GATED | Hostile user/tool input must be blocked | Guard allow/block decision |
| 4 | PLAN | `prompt-leak-scanner` | GATED | Before shipping a system prompt: catch internal/secret leakage | Leak findings (line-level) |
| 5 | PLAN | `doc-desens-scanner` | GATED | Before a doc/code/log goes external | Masked copy + audit ledger |
| 6 | PLAN | `agent-kill-switch` | GATED | Before deploying a high-risk/funds agent | Complete kill card; blocks if fields missing |
| 7 | GATE | `skill-quality-gate` | GATED | Before admitting a skill to the library | Gate verdict + blocking findings |
| 8 | GATE | `publish-quality-gate` | GATED | Right before external publish | Publish verdict; blocks launch on blockers |
| 9 | AUDIT | `lgd-badge-issuer` | REGISTERED+GATED | After three-law assessment passes | Badge certificate + SHA-256 fingerprint + ledger row |
| 10 | AUDIT | `lgd-badge-verify` | EVIDENCED+GATED | Before trusting an external badge | Verify pass/fail with reasons |

### Quantified evidence bars (measured, not claimed)

- **Downloads — 788 cumulative ModelScope downloads across the 9 sub-skills** (snapshot 2026-10-17 11:21): redteam 96 · injection-shield 81 · leak-scanner 95 · desens 95 · kill-switch 92 · badge-issuer 79 · badge-verify 84 · skill-gate 70 · publish-gate 96.
- **Batch eval — RPT-20261016-TOP20-B**: 7 of 9 sub-skills executed this round; executable **PASS ×7**, reproducible **PASS ×7**, **FAIL ×0** (remaining 2 = badge issuer/verify, not in batch). Batch-wide verdict CONDITIONAL with 0 FAIL; the open defects are tracked upstream, not vendored here.
- **Release discipline — six gates on this collection**: YAML valid / read_when non-empty / bilingual complete / scripts runnable / desensitization 0 hits / run rc=0.

### Per-phase notes
- **SPEC first.** Pin scope and charter before any tool runs; the audit phase can only verify against a pinned spec.
- **PLAN = defense in depth.** Attack (2), shield runtime input (3), scan the prompt itself (4), desensitize anything leaving the boundary (5), pre-authorize the kill card (6).
- **GATE = two hard stops.** Library admission (7) and external publish (8); both must be green. Desens and kill-switch are already wired as gates inside PLAN.
- **AUDIT = provenance.** Issue a badge only after gates pass; verify someone else's badge before relying on it.

### Demo
```bash
# list the whole lifecycle (4 phases, 9 sub-skills)
python3 scripts/governance_flow.py --list

# get the call note for one phase or slug
python3 scripts/governance_flow.py --route plan
python3 scripts/governance_flow.py --route lgd-badge-verify

# print the live LGD three-law status line
python3 scripts/governance_flow.py --badge
```

### Scope & red lines
- This collection **vendors no sub-skill internals**. It references sub-skills by slug only; their code stays in their own packages.
- Pure documentation + a read-only router. No network, no business-data writes, no acting on your behalf.
- Sub-skill release status is tracked separately in the governance ledger; this collection does not republish or fork them.

## 中文

### 这是什么
**GovernanceOS** 是一个*方法论合集*——用一套操作系统把智能体治理的全生命周期端到端串起来。它**不重写安全逻辑**：而是按阶段，把你路由到 9 个已独立发布、各自维护的子技能。本仓是目录，子技能是章节。

与外部所有合集（superpowers / ECC / caveman）的差异：我们把**理论 + 技能 + 证据链 + 监督章程**放在一处——LGD 三律（有籍/有证/有门禁）是内嵌的，不是外挂的。

### 一页生命周期流水线

```
 GOVERNANCEOS —— 一个生命周期、九个子技能、三律内嵌

   SPEC（定界）         PLAN（防御纵深）            GATE（两道硬门）          AUDIT（凭证留痕）
 ┌───────────┐   ┌───────────────────┐   ┌────────────────────┐   ┌──────────────────┐
 │ 界定治理  │──▶│ 先攻后防：        │──▶│ 两道质量门：        │──▶│ 出处与台账：      │
 │ 范围与    │   │ agent-redteam-    │   │ skill-quality-gate │   │ badge-issuer ->  │
 │ 监督章程  │   │ kit -> prompt-    │   │ -> publish-quality │   │ badge-verify     │
 │           │   │ injection-shield  │   │ -gate（+文档脱敏与  │   │                  │
 │           │   │ -> prompt-leak-   │   │  停机开关作为硬停） │   │                  │
 │           │   │ scanner -> doc-   │   │                    │   │                  │
 │           │   │ desens-scanner -> │   │                    │   │                  │
 │           │   │ agent-kill-switch │   │                    │   │                  │
 └───────────┘   └───────────────────┘   └────────────────────┘   └──────────────────┘
        \                 \                        \                       /
         \_________________\______ LGD 三律内嵌 __________________/
                 [ 有籍 ] 113/113 包 · 100.0%
                 [ 有证 ] 112/113 包 ·  99.1%
                 [ 有门禁 ] 112/113 包 ·  99.1%
                 （看板快照 2026-10-17；下列 9 个子技能三律全部 GREEN）
```

### 入口索引（阶段 | slug | 何时用 | 预期输出）

| # | 阶段 | 子技能 slug | LGD 徽标 | 何时用 | 预期输出 |
|---|------|-------------|----------|--------|----------|
| 1 | SPEC | _（本合集）_ | — | 动工前界定治理范围与监督章程 | 范围+章程钉死；后续各阶段以此为据 |
| 2 | PLAN | `agent-redteam-kit` | 有门禁 | 上线前对抗性压测智能体 | 攻击面评分报告 + 修复清单 |
| 3 | PLAN | `prompt-injection-shield` | 有门禁 | 需拦截恶意用户/工具输入 | 放行/拦截判定 |
| 4 | PLAN | `prompt-leak-scanner` | 有门禁 | 发系统提示词前查内部/密钥泄漏 | 泄漏发现（行级） |
| 5 | PLAN | `doc-desens-scanner` | 有门禁 | 文档/代码/日志对外前 | 脱敏版 + 留痕清单 |
| 6 | PLAN | `agent-kill-switch` | 有门禁 | 高危/资金类智能体部署前 | 完整制动卡；缺项即阻断 |
| 7 | GATE | `skill-quality-gate` | 有门禁 | 技能入库存准入前 | 门禁结论 + 阻断项 |
| 8 | GATE | `publish-quality-gate` | 有门禁 | 对外发布前最后一道 | 发布结论；有阻断项即不许上线 |
| 9 | AUDIT | `lgd-badge-issuer` | 有籍+有门禁 | 三律考核通过后申请徽章 | 徽章证书 + SHA-256 指纹 + 台账行 |
| 10 | AUDIT | `lgd-badge-verify` | 有证+有门禁 | 信任外部徽章前 | 通过/不通过 + 原因 |

### 量化证据条（实测，非口号）

- **下载量 —— 9 个子技能累计 788 次 ModelScope 下载**（2026-10-17 11:21 快照）：红队 96 · 注入防护 81 · 泄漏扫描 95 · 文档脱敏 95 · 停机开关 92 · 徽章签发 79 · 徽章核验 84 · 技能质量门 70 · 发布门 96。
- **批量评测 —— RPT-20261016-TOP20-B**：本轮实跑 9 个子技能中的 7 个；可执行 **PASS ×7**、可复现 **PASS ×7**、**FAIL ×0**（余 2 个为徽章签发/核验，不在本批）。整批评测 verdict 为 CONDITIONAL、FAIL 为 0；未闭环缺陷留在上游跟踪，本合集不复制其实现。
- **发布纪律 —— 本合集六门**：YAML 有效 / read_when 非空 / 双语完整 / 脚本可跑 / 脱敏 0 命中 / 实跑 rc=0。

### 阶段说明
- **先 SPEC。** 先钉范围与章程再跑工具；审计阶段只能对照钉死的规范核验。
- **PLAN = 纵深防御。** 先攻（2）、运行时拦注入（3）、扫提示词本身（4）、对出边界的东西脱敏（5）、预先写好制动卡（6）。
- **GATE = 两道硬停。** 入库准入（7）与对外发布（8），两道都要绿；脱敏与停机开关已作为门内硬停。
- **AUDIT = 凭证。** 门禁全过才发徽章；信任别人的徽章前先核验。

### 示例
```bash
# 列出全生命周期（4 阶段、9 子技能）
python3 scripts/governance_flow.py --list

# 查某个阶段或 slug 怎么调
python3 scripts/governance_flow.py --route plan
python3 scripts/governance_flow.py --route lgd-badge-verify

# 打印 LGD 三律实时状态行
python3 scripts/governance_flow.py --badge
```

### 边界与红线
- 本合集**不内嵌任何子技能内部实现**，仅按 slug 引用；子包代码留在各自包内，不改不复制。
- 纯文档 + 只读路由脚本：无网络、不写业务数据、不代你执行任何动作。
- 各子技能的发布状态在治理台账单独跟踪；本合集不重发、不 fork 它们。
