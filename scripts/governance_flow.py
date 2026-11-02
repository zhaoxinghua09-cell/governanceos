#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
governance_flow.py — GovernanceOS orchestrator (read-only lifecycle router).

This is a thin DISPATCHER. It does NOT vendor or re-implement any sub-skill; it only
points you at the independently published sub-skill slug for each governance phase.
All real work is done by the referenced sub-skills.

Lifecycle: SPEC -> PLAN -> GATE -> AUDIT -> EVO (24 sub-skills orchestrated by slug).

Usage:
  python3 governance_flow.py --list
  python3 governance_flow.py --route plan
  python3 governance_flow.py --route lgd-badge-verify
  python3 governance_flow.py --badge
"""
import sys
import argparse

# phase -> [ (stage-key, slug, when-to-use, expected-output) ]
# THIN DISPATCHER: only references independently published sub-skill slugs.
# Adding / removing a governance capability = editing one tuple below.
PHASES = [
    ("spec", "SPEC", [
        ("spec", None,
         "Before building: pin the governance scope and supervision charter.",
         "Scope + charter pinned; every later phase references it."),
    ]),
    ("plan", "PLAN", [
        ("redteam", "agent-redteam-kit",
         "Before launch: run adversarial/red-team drills on the agent.",
         "Drill report with scored attack surfaces and fix list."),
        ("shield", "prompt-injection-shield",
         "When user/tool input could be hostile and prompt-injection must be blocked.",
         "Shield rules/guard decision for the given prompt."),
        ("leak", "prompt-leak-scanner",
         "Before shipping a prompt/system-prompt: check it leaks internals/secrets.",
         "Leak findings list with line-level hints."),
        ("desens", "doc-desens-scanner",
         "Before a document/code/log goes external: mask PII, secrets, internal paths.",
         "Desensitized copy + audit ledger of every mask."),
        ("killswitch", "agent-kill-switch",
         "Before deploying a sensitive/funds/high-risk agent: author the kill card.",
         "Kill card with stop conditions, revocation, owner, recovery; --check blocks on missing fields."),
    ]),
    ("gate", "GATE", [
        ("skill-gate", "skill-quality-gate",
         "Before a skill is admitted to the library: run the skill quality gate.",
         "Quality gate verdict with blocking findings."),
        ("publish-gate", "publish-quality-gate",
         "Right before external publish: run the release/quality gate.",
         "Publish gate verdict; blocks launch on any blocking finding."),
        ("admission-gate", "skill-admission-gate",
         "When a new skill requests library admission: run the admission gate.",
         "Admission verdict: admit / conditional / reject with reasons."),
        ("review-gate", "publish-review-gate",
         "Before a publish: run the human + automated review gate.",
         "Review verdict with checklist coverage."),
        ("release-gate", "release-gate-check",
         "At release time: verify all release prerequisites are met.",
         "Release readiness checklist with pass/fail."),
        ("skill-release-gate", "skill-release-gate",
         "When shipping a skill package: run the skill release gate.",
         "Release gate verdict; blocks on blocking finding."),
        ("oversight-gate", "human-oversight-gate",
         "For high-risk actions: require a human oversight gate.",
         "Oversight decision record with approver."),
        ("gate-policy", "gate-policy-generator",
         "When you need a gate policy for a new risk class: generate it.",
         "Generated gate policy document."),
    ]),
    ("audit", "AUDIT", [
        ("badge-issue", "lgd-badge-issuer",
         "After three-law assessment passes: issue the lgd-certified badge.",
         "Badge certificate with SHA-256 fingerprint + issuance ledger row."),
        ("badge-verify", "lgd-badge-verify",
         "When relying on someone else's badge: verify its fingerprint and ledger.",
         "Verify pass/fail with reasons."),
        ("three-laws", "lgd-three-laws-auditor",
         "Audit a package against the LGD three-laws (registered/evidenced/gated).",
         "Three-laws audit verdict with per-law evidence."),
        ("trace-audit", "agent-trace-audit",
         "Reconstruct an agent's action trace for post-incident audit.",
         "Action trace log with anomaly flags."),
        ("bias-audit", "bias-auditor",
         "Audit outputs/decisions for bias before release.",
         "Bias audit report with flagged dimensions."),
        ("env-audit", "env-var-audit",
         "Audit environment variables / secrets exposure before deploy.",
         "Env exposure report with leaked-secret findings."),
        ("gov-audit-chain", "ai-governance-audit-chain",
         "Build the governance audit chain across an agent's lifecycle.",
         "Audit chain document linking every gate/evidence."),
        ("trail-keeper", "audit-trail-keeper",
         "Maintain the immutable audit trail for compliance.",
         "Audit trail ledger with append-only entries."),
        ("pkg-compliance", "expert-package-compliance-audit",
         "Audit an expert/package for publish-compliance before launch.",
         "Compliance audit verdict with blocking findings."),
        ("traceability", "traceability-audit-team",
         "Run the traceability audit team across a deliverable.",
         "Traceability matrix with coverage gaps."),
    ]),
    ("evo", "EVO", [
        ("evolution", "agent-evolution",
         "After deploy: let the agent log findings and evolve its own playbook.",
         "Evolution log + refined operating procedure."),
    ]),
]

# LGD three-law badge line — values are READ from the LGD three-laws dashboard
# (scanned 2026-10-17T10:39:59+08:00). This router does NOT reach the network;
# the numbers are pinned here at build time from that snapshot.
LGD_BADGE = {
    "snapshot": "2026-10-17T10:39:59+08:00",
    "registered": ("113/113", "100.0%"),   # 有籍
    "evidenced": ("112/113", "99.1%"),     # 有证
    "gated": ("112/113", "99.1%"),         # 有门禁
    "all_subskills_green": True,
}


def all_stages():
    out = []
    for _, _, stages in PHASES:
        out.extend(stages)
    return out


def main():
    ap = argparse.ArgumentParser(
        prog="governance-flow",
        description="GovernanceOS — read-only lifecycle router (SPEC->PLAN->GATE->AUDIT) "
                    "over 24 published governance sub-skills.")
    ap.add_argument("--list", action="store_true",
                    help="list the full lifecycle (phase | slug | when | output)")
    ap.add_argument("--route", metavar="PHASE|STAGE|SLUG",
                    help="show the call note for one phase key, stage key, or sub-skill slug")
    ap.add_argument("--badge", action="store_true",
                    help="print the embedded LGD three-law status line")
    args = ap.parse_args()

    if args.badge:
        b = LGD_BADGE
        print("LGD three-laws (snapshot %s):" % b["snapshot"])
        print("  REGISTERED 有籍 : %s packages · %s" % b["registered"])
        print("  EVIDENCED  有证 : %s packages · %s" % b["evidenced"])
        print("  GATED      有门禁 : %s packages · %s" % b["gated"])
        print("  embedded 24 sub-skills overall green: %s" % b["all_subskills_green"])
        return 0

    if args.route:
        key = args.route.strip().lower()
        # phase key?
        for pkey, plabel, stages in PHASES:
            if key == pkey:
                print("phase=%s (%s) — sub-skills:" % (pkey, plabel))
                for (sk, slug, when, out) in stages:
                    if slug:
                        print("  [%s] slug=%s" % (sk, slug))
                        print("     when: %s" % when)
                        print("     out : %s" % out)
                    else:
                        print("  [%s] (no sub-skill — defined by this suite)" % sk)
                return 0
        # stage key or slug?
        for (sk, slug, when, out) in all_stages():
            if key == sk or (slug and key == slug):
                print("stage=%s  sub-skill=%s" % (sk, slug or "(this suite)"))
                print("  when-to-use : %s" % when)
                print("  expected-out: %s" % out)
                if slug:
                    print("  call        : invoke the '%s' sub-skill directly (its own CLI/help)." % slug)
                return 0
        print("no such phase/stage/slug: %s" % key)
        print("known phases: %s" % ", ".join(p for (p, _, _) in PHASES))
        print("known stages: %s" % ", ".join(s for (s, _, _, _) in all_stages()))
        return 2

    # default: list the whole lifecycle
    print("GovernanceOS — lifecycle SPEC -> PLAN -> GATE -> AUDIT -> EVO (24 sub-skills, by slug):")
    print("=" * 78)
    for pkey, plabel, stages in PHASES:
        print("[%s] %s" % (pkey.upper(), plabel))
        for (sk, slug, when, out) in stages:
            who = slug if slug else "(this suite)"
            print("  - %-12s -> %-24s | %s" % (sk, who, out))
    print("=" * 78)
    print("tip: python3 governance_flow.py --route <phase|stage|slug>  |  --badge")
    return 0


if __name__ == "__main__":
    sys.exit(main())
