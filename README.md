# GovernanceOS

[![Code: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE)
[![Content: All Rights Reserved](https://img.shields.io/badge/Content-All%20Rights%20Reserved-red.svg)](LICENSE-CONTENT)
[![AI Governance](https://img.shields.io/badge/AI-agent-governance-2ea44f.svg)](#)
[![Security & Compliance](https://img.shields.io/badge/security-compliance-blue.svg)](#)
[![Python Router](https://img.shields.io/badge/router-python%203-3776AB.svg)](scripts/governance_flow.py)
[![Bilingual EN/ZH](https://img.shields.io/badge/docs-EN%2FZH-brightgreen.svg)](README.en.md)

**One operating system for the full AI-agent governance lifecycle — SPEC → PLAN → GATE → AUDIT.**
A methodology collection that orchestrates 9 independently published governance sub-skills by slug. It vendors **no** sub-skill internals. Differentiator: theory (LGD three-laws) + skills + evidence chain + supervision charter, in one repo.

## English

### The one-page pipeline

```
 SPEC                PLAN                    GATE                   AUDIT
 ┌───────────┐   ┌───────────────────┐   ┌────────────────────┐   ┌──────────────────┐
 │ scope &   │──▶│ redteam -> shield │──▶│ skill-quality-gate │──▶│ badge-issuer ->  │
 │ charter    │   │ -> leak -> desens │   │ -> publish-quality │   │ badge-verify     │
 │           │   │ -> kill-switch    │   │ -gate              │   │                  │
 └───────────┘   └───────────────────┘   └────────────────────┘   └──────────────────┘
        \______________ LGD three-laws embedded ______________/
        [ 有籍 REGISTERED ] 113/113 · 100.0%
        [ 有证 EVIDENCED  ] 112/113 · 99.1%
        [ 有门禁 GATED    ] 112/113 · 99.1%   (dashboard 2026-10-17)
```

### Evidence bars (measured)

- **788** cumulative ModelScope downloads across the 9 sub-skills (2026-10-17 11:21 snapshot).
- Batch eval RPT-20261016-TOP20-B: 7/9 executed, executable PASS ×7, reproducible PASS ×7, **FAIL ×0**.
- Six gates on this repo: YAML valid · read_when non-empty · bilingual complete · scripts runnable · desensitization 0 hits · run rc=0.

### Sub-skills (by slug — already published, independent)

| Phase | Slug | ModelScope downloads | Eval (RPT-20261016-TOP20-B) |
|-------|------|----------------------|------------------------------|
| PLAN | `agent-redteam-kit` | 96 | SK-008 exec/repro PASS · CONDITIONAL |
| PLAN | `prompt-injection-shield` | 81 | SK-091 exec/repro PASS · CONDITIONAL |
| PLAN | `prompt-leak-scanner` | 95 | SK-092 exec/repro PASS · CONDITIONAL |
| PLAN | `doc-desens-scanner` | 95 | SK-042 exec/repro PASS · CONDITIONAL |
| PLAN | `agent-kill-switch` | 92 | SK-004 exec/repro PASS · CONDITIONAL |
| GATE | `skill-quality-gate` | 70 | SK-100 exec/repro PASS · CONDITIONAL |
| GATE | `publish-quality-gate` | 96 | SK-094 exec/repro PASS · CONDITIONAL |
| AUDIT | `lgd-badge-issuer` | 79 | not in batch |
| AUDIT | `lgd-badge-verify` | 84 | not in batch |

### Install (one command)

```bash
# clone this repo, then either point your agent CLI at SKILL.md directly, or run:
./install.sh        # macOS / linux
./install.ps1       # windows (powershell)
```

Vendor shims are included: `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/` — the same repo installs across agent CLIs.

### Run the router
```bash
python3 scripts/governance_flow.py --list
python3 scripts/governance_flow.py --route plan
python3 scripts/governance_flow.py --badge
```

This repo is pure documentation + a read-only router: no network, no business-data writes, no acting on your behalf. License: MIT for code (.py); the method-doc text of SKILL.md is not covered by MIT.

## 中文

**一套操作系统跑通智能体治理全生命周期——SPEC（定界）→ PLAN（防御纵深）→ GATE（两道硬门）→ AUDIT（凭证留痕）。** 按 slug 编排 9 个已独立发布的治理子技能，**不内嵌子包内部实现**。差异点：理论（LGD 三律）+ 技能 + 证据链 + 监督章程，一仓集齐。

### 一页流水线

```
 SPEC（定界）         PLAN（防御纵深）            GATE（两道硬门）          AUDIT（凭证留痕）
 ┌───────────┐   ┌───────────────────┐   ┌────────────────────┐   ┌──────────────────┐
 │ 范围与    │──▶│ 红队 -> 注入防护  │──▶│ 技能质量门         │──▶│ 徽章签发 ->      │
 │ 监督章程  │   │ -> 泄漏扫描 ->    │   │ -> 发布门          │   │ 徽章核验         │
 │           │   │ 文档脱敏 ->停机卡 │   │                    │   │                  │
 └───────────┘   └───────────────────┘   └────────────────────┘   └──────────────────┘
        \______________ LGD 三律内嵌 ______________/
        [ 有籍 ] 113/113 · 100.0%
        [ 有证 ] 112/113 · 99.1%
        [ 有门禁 ] 112/113 · 99.1%   （看板 2026-10-17）
```

### 证据条（实测）

- 9 个子技能累计 **788** 次 ModelScope 下载（2026-10-17 11:21 快照）。
- 批量评测 RPT-20261016-TOP20-B：实跑 7/9，可执行 PASS ×7、可复现 PASS ×7、**FAIL ×0**。
- 本仓六门：YAML 有效 · read_when 非空 · 双语完整 · 脚本可跑 · 脱敏 0 命中 · 实跑 rc=0。

### 子技能（按 slug——已独立发布）

| 阶段 | slug | ModelScope 下载 | 评测（RPT-20261016-TOP20-B） |
|------|------|------------------|------------------------------|
| PLAN | `agent-redteam-kit` | 96 | SK-008 可执行/可复现 PASS · CONDITIONAL |
| PLAN | `prompt-injection-shield` | 81 | SK-091 可执行/可复现 PASS · CONDITIONAL |
| PLAN | `prompt-leak-scanner` | 95 | SK-092 可执行/可复现 PASS · CONDITIONAL |
| PLAN | `doc-desens-scanner` | 95 | SK-042 可执行/可复现 PASS · CONDITIONAL |
| PLAN | `agent-kill-switch` | 92 | SK-004 可执行/可复现 PASS · CONDITIONAL |
| GATE | `skill-quality-gate` | 70 | SK-100 可执行/可复现 PASS · CONDITIONAL |
| GATE | `publish-quality-gate` | 96 | SK-094 可执行/可复现 PASS · CONDITIONAL |
| AUDIT | `lgd-badge-issuer` | 79 | 不在本批 |
| AUDIT | `lgd-badge-verify` | 84 | 不在本批 |

### 安装（一条命令）

```bash
# 克隆本仓后，可直接让 agent CLI 指向 SKILL.md，或运行：
./install.sh        # macOS / linux
./install.ps1       # windows (powershell)
```

仓内附多端 shim：`.claude-plugin/`、`.codex-plugin/`、`.cursor-plugin/`——同一仓一次分发到多个 agent CLI。

### 运行路由
```bash
python3 scripts/governance_flow.py --list
python3 scripts/governance_flow.py --route plan
python3 scripts/governance_flow.py --badge
```

本仓为纯文档 + 只读路由：无网络、不写业务数据、不代执行。许可：代码（.py）MIT；SKILL.md 中的方法论文本不在 MIT 覆盖范围内。

---

## License / 许可

本仓为**混合仓**：代码与方法论文本采用不同许可（与上文既有声明一致）。

- **代码（MIT）**：`scripts/governance_flow.py`、`install.sh`、`install.ps1` 及各插件 shim 清单以 MIT 许可发布，见 [LICENSE](LICENSE)。
- **方法论文本（保留所有权利）**：`SKILL.md` 与 `README.md` 等文档正文不属 MIT，可在署名后短引与链接；转载、改编、入训练语料须书面申请，见 [LICENSE-CONTENT](LICENSE-CONTENT)。
- 本仓按 slug 引用 9 个已独立发布的子技能，不内嵌其内部实现；各子技能以其各自许可证为准。

安全问题请按 [SECURITY.md](SECURITY.md) 私下报告；贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。
联系：zhaoxinghua09@gmail.com ｜ ORCID 0009-0001-0512-1237
