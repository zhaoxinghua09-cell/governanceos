# GovernanceOS

[![License: MIT](https://img.shields.io/badge/Code-MIT-yellow.svg)](LICENSE)
[![Content: All Rights Reserved](https://img.shields.io/badge/Content-All%20Rights%20Reserved-red.svg)](LICENSE-CONTENT)
[![AI Governance](https://img.shields.io/badge/AI-agent-governance-2ea44f.svg)](#)
[![Security](https://img.shields.io/badge/security-compliance-blue.svg)](#)
[![Python](https://img.shields.io/badge/router-python%203-3776AB.svg)](scripts/governance_flow.py)
[![Bilingual](https://img.shields.io/badge/docs-EN%2FZH-brightgreen.svg)](README.md)

**One operating system for the full AI-agent governance lifecycle — SPEC → PLAN → GATE → AUDIT.**
A methodology collection that orchestrates 9 independently published governance sub-skills by slug. It vendors **no** sub-skill internals. Differentiator: theory (LGD three-laws) + skills + evidence chain + supervision charter, in one repo.

## What it is

GovernanceOS is a *methodology collection*, not a reimplementation of security logic. It routes you, phase by phase, to 9 sub-skills that are already published and maintained on their own. Treat this repo as the table of contents; the sub-skills are the chapters.

The LGD three-laws (registered / evidenced / gated) are embedded as live status, not bolted on.

## The one-page pipeline

```
 SPEC                PLAN                    GATE                   AUDIT
 ┌───────────┐   ┌───────────────────┐   ┌────────────────────┐   ┌──────────────────┐
 │ scope &   │──▶│ redteam -> shield │──▶│ skill-quality-gate │──▶│ badge-issuer ->  │
 │ charter   │   │ -> leak -> desens │   │ -> publish-quality │   │ badge-verify     │
 │           │   │ -> kill-switch    │   │ -gate              │   │                  │
 └───────────┘   └───────────────────┘   └────────────────────┘   └──────────────────┘
        \______________ LGD three-laws embedded ______________/
```

## Quick Start

```bash
# clone this repo
git clone https://github.com/zhaoxinghua09-cell/governanceos.git
cd governanceos

# list the whole lifecycle (4 phases, 9 sub-skills)
python3 scripts/governance_flow.py --list

# get the call note for one phase or slug
python3 scripts/governance_flow.py --route plan

# print the live LGD three-law status line
python3 scripts/governance_flow.py --badge
```

Vendor shims are included: `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/` — the same repo installs across agent CLIs.

## The 9 sub-skills (by slug)

| Phase | Slug | When to use |
|-------|------|-------------|
| PLAN | `agent-redteam-kit` | Adversarial stress-test before launch |
| PLAN | `prompt-injection-shield` | Block hostile user/tool input at runtime |
| PLAN | `prompt-leak-scanner` | Catch internal/secret leakage before shipping a prompt |
| PLAN | `doc-desens-scanner` | Mask anything leaving the boundary |
| PLAN | `agent-kill-switch` | Pre-authorize a kill card for high-risk agents |
| GATE | `skill-quality-gate` | Library-admission verdict |
| GATE | `publish-quality-gate` | External-publish verdict; blocks on blockers |
| AUDIT | `lgd-badge-issuer` | Issue a badge after gates pass |
| AUDIT | `lgd-badge-verify` | Verify someone else's badge before trusting it |

## Scope & red lines

- Vendors **no** sub-skill internals; references sub-skills by slug only.
- Pure documentation + a read-only router. No network, no business-data writes, no acting on your behalf.
- Self-assessment / method material; not a third-party certification.

## License / 许可

Mixed repo — code and prose carry different licenses:

- **Code (MIT)**: `scripts/governance_flow.py`, installers and plugin shims — see [LICENSE](LICENSE).
- **Methodology prose (all rights reserved)**: `SKILL.md`, `README.md` docs — short citation and linking allowed with attribution; republishing / adapting / ML-corpus use requires written permission — see [LICENSE-CONTENT](LICENSE-CONTENT).

## Security

Found a problem? Report it privately per [SECURITY.md](SECURITY.md). Contributions welcome per [CONTRIBUTING.md](CONTRIBUTING.md).

Contact: zhaoxinghua09@gmail.com ｜ ORCID `0009-0001-0512-1237`
