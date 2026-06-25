"""
MISSION RUNNER — 3-stage control loop + Mission Dossier + optional Direction Checks

The army's spine. Where commander.py *defines* the commander agent, this runner *drives the
mission*: it holds the Mission Dossier (living state), runs the army across three stages, offers
two OPTIONAL Direction Checks (non-blocking), runs the FINAL Inspector, parses the verdict, and
controls re-entry and the iteration cap.

PRODUCT VARIANT: this army produces DELIVERABLES — it does NOT spend budget or push code — so
there is NO mandatory human go/no-go gate. Instead, two LIGHT, OPTIONAL Direction Checks are
offered:
  DC-1  after DISCOVER (before STRATEGISE+SHAPE): confirm the discovery brief / steer.
  DC-2  after STRATEGISE+SHAPE (before DELIVER): confirm the strategy + shape / redirect.
Both are non-blocking by default (auto_proceed); inject console_direction_check (or a custom
callable) to enable interactive steering.

Three stages per iteration:
  DISCOVER          (Phase 0 frame → O1 discovery & research)
  --- DC-1 offered: present discovery brief, offer to confirm/steer (non-blocking) ---
  STRATEGISE+SHAPE  (O2 strategy → O3 prioritisation → O4 design & validation)
  --- DC-2 offered: present strategy+shape brief, offer to confirm/redirect (non-blocking) ---
  DELIVER           (O5 delivery → O6 measurement & learning)
Then the FINAL Inspector verdict gates delivery.

A STEER on DC-1 loops back to DISCOVER (re-runs all three stages).
A STEER on DC-2 loops back to STRATEGISE+SHAPE (DISCOVER output is preserved; DC-1 is skipped).
Inspector VETO or PASS_WITH_FIXES loops back to DISCOVER for a full re-run with required fixes.
Cap at MAX_ITERS = 3; if still failing, deliver the best result with residual_risk stated.

Run:  python -m product_kit.mission "Describe the product goal here"
(Requires `pip install openai-agents` and OPENAI_API_KEY.)
"""

import json
import sys

from agents import Runner

from .commander import commander_product as commander
from .inspector import inspector

MAX_ITERS = 3  # iteration cap — deliver-with-residual-risk rather than thrash forever


# ---------------------------------------------------------------------------
# Mission Dossier
# ---------------------------------------------------------------------------

def new_dossier(goal: str) -> dict:
    """The single living-state artifact carried across the whole mission."""
    return {
        "goal": goal,
        "context": None,            # product type / audience / stage detected in framing
        "assumptions": [],
        "decisions": [],            # decisions per phase, versioned on re-entry
        "sources": [],
        "open_to_verify": [],
        "direction_check_1": None,  # optional steer recorded after DISCOVER (if used)
        "direction_check_2": None,  # optional steer recorded after STRATEGISE+SHAPE (if used)
        "verdicts": [],             # Inspector verdicts + required fixes, per iteration
        "iteration": 0,
    }


def _dossier_block(dossier: dict) -> str:
    return json.dumps(dossier, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Stage briefs
# ---------------------------------------------------------------------------

def discover_brief(dossier: dict, required_fixes: list) -> str:
    """Stage 1 — run Phase 0 (frame) then O1 (discovery & research). STOP before O2."""
    parts = [
        "MISSION DOSSIER (read in; do not re-ask what is already here):",
        _dossier_block(dossier),
        "\nRun PHASE 0 (frame) then STAGE 1 — DISCOVER (O1): run the JTBD → ODI → OST pipeline, "
        "user interview synthesis, Kano classification, and market sizing. STOP before O2 "
        "(strategy & direction). Do NOT start strategy, prioritisation, or design work.",
        "\nReturn a DISCOVERY BRIEF in the user's language: the framing answers (context, stage, "
        "constraints), the job statement and four-forces diagram, ODI outcome map, OST structure, "
        "Kano classification, market sizing (TAM/SAM/SOM), and the signed Problem Statement "
        "Worksheet (context | success criteria | scope | constraints | stakeholders | key "
        "insights). Make sources and open-to-verify items explicit.",
    ]
    if required_fixes:
        parts.append(
            "\nRE-ENTRY — resolve these before re-presenting (carry the dossier forward):\n- "
            + "\n- ".join(required_fixes)
        )
    return "\n".join(parts)


def strategise_shape_brief(dossier: dict, discovery_pkg: str) -> str:
    """Stage 2 — build on the confirmed discovery: O2 (strategy) + O3 (prioritisation) + O4 (design)."""
    return "\n".join([
        "MISSION DOSSIER:",
        _dossier_block(dossier),
        "\nThe discovery below is confirmed (with any steer recorded in the dossier). "
        "Run STAGE 2 — STRATEGISE + SHAPE: deploy O2 (strategy & direction), then O3 "
        "(prioritisation), then O4 (design & validation). Include the quick Inspector GATE "
        "after O2 and after O4 as specified in your instructions. "
        "STOP before O5 (delivery).",
        "\nCONFIRMED DISCOVERY:\n" + discovery_pkg,
        "\nReturn a STRATEGY + SHAPE BRIEF in the user's language: the product vision (PR/FAQ), "
        "North Star metric + at least two counter-metrics, OKRs, PMF assessment, outcome roadmap, "
        "RICE-prioritised backlog (with named single-threaded owners per initiative), and the "
        "shaped solution (appetite + fat marker sketch + four risks assessed + riskiest assumptions "
        "tested). Make sources and open-to-verify items explicit.",
    ])


def deliver_brief(dossier: dict, strategy_shape_pkg: str) -> str:
    """Stage 3 — deliver on the confirmed strategy+shape: O5 (delivery) + O6 (measurement)."""
    return "\n".join([
        "MISSION DOSSIER:",
        _dossier_block(dossier),
        "\nThe strategy and shape below are confirmed (with any steer recorded in the dossier). "
        "Run STAGE 3 — DELIVER: deploy O5 (delivery) and O6 (measurement & learning).",
        "\nCONFIRMED STRATEGY + SHAPE:\n" + strategy_shape_pkg,
        "\nReturn the full DELIVERABLE in the user's language: user story map (backbone + walking "
        "skeleton + release slices), feature flag rollout strategy (canary / ring-based / "
        "kill-switch), launch readiness checklist (monitoring, rollback, support, legal), DORA "
        "metrics baseline (Forsgren, Humble, Kim, 2018), beta program design, North Star tracking "
        "plan, AARRR funnel analysis, cohort retention setup, A/B experiment designs with "
        "pre-registered power calculations (MDE, α, β), and product analytics instrumentation "
        "plan. Make sources and open-to-verify items explicit.",
    ])


def mission_brief(dossier: dict, required_fixes: list) -> str:
    """Single combined brief: DISCOVER → STRATEGISE+SHAPE → DELIVER (all 3 stages in one call)."""
    parts = [
        "MISSION DOSSIER (read in; do not re-ask what is already here):",
        _dossier_block(dossier),
        "\nRun the complete 3-stage product mission:",
        "  STAGE 1 — DISCOVER: Phase 0 (frame) + O1 (JTBD → ODI → OST pipeline, user interviews,"
        " Kano, market sizing). Produce a Discovery Brief.",
        "  STAGE 2 — STRATEGISE + SHAPE: O2 (strategy & direction) + O3 (prioritisation) + "
        "O4 (design & validation). Produce a Strategy + Shape Brief.",
        "  STAGE 3 — DELIVER: O5 (delivery) + O6 (measurement & learning). Produce the full "
        "Deliverable.",
        "\nReturn all three stages in sequence. Make sources and open-to-verify items explicit.",
    ]
    if required_fixes:
        parts.append(
            "\nRE-ENTRY — resolve these before re-presenting (carry the dossier forward):\n- "
            + "\n- ".join(required_fixes)
        )
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Verdict parsing
# ---------------------------------------------------------------------------

def parse_verdict(text: str) -> str:
    """Map the Inspector's free text to a machine verdict. Order matters (VETO first)."""
    upper = (text or "").upper()
    if "VETO" in upper:
        return "VETO"
    if "PASS WITH FIXES" in upper or "PASS-WITH-FIXES" in upper:
        return "PASS_WITH_FIXES"
    if "PASS" in upper:
        return "PASS"
    return "UNCLEAR"


def extract_required_fixes(text: str) -> list:
    """Best-effort pull of the required-fix bullet lines from the Inspector output.

    Captures two patterns:
      1. Lines that start with FIX / REQUIRED / BLOCK (keyword-prefixed items).
      2. Bullet lines (- / * / •) immediately following a heading that contains
         REQUIRED or BLOCK — handles "Required Fixes (Blocking):" section headers
         whose items are indented bullets on the next lines.
    """
    fixes = []
    lines = (text or "").splitlines()
    in_fixes_section = False
    for line in lines:
        raw = line.strip()
        s = raw.lstrip("-*•").strip()
        upper = s.upper()
        # Detect a section heading like "**Required Fixes (Blocking):**"
        if any(p in upper for p in ("REQUIRED FIX", "BLOCKING FIX", "MUST FIX", "REQUIRED CHANGE")):
            in_fixes_section = True
            continue
        # Exit section on a blank line or next heading
        if in_fixes_section:
            if not raw:
                in_fixes_section = False
                continue
            if raw.startswith("#") or (raw.startswith("**") and raw.endswith("**")):
                in_fixes_section = False
                continue
            # Collect bullets in the section
            if raw.startswith(("-", "*", "•")) and s:
                fixes.append(s)
                continue
        # Also capture standalone keyword-prefixed lines anywhere in the text
        if s and any(upper.startswith(p) for p in ("FIX:", "REQUIRED:", "BLOCKING:", "BLOCK:")):
            fixes.append(s)
    return fixes


# ---------------------------------------------------------------------------
# Direction Check functions (injectable; OPTIONAL and NON-BLOCKING by default)
# ---------------------------------------------------------------------------

def auto_proceed(pkg: str) -> tuple:
    """Default: no human gate. This army produces deliverables, so it proceeds without approval."""
    return ("PROCEED", "auto-proceed (no mandatory direction check)")


def console_direction_check(pkg: str) -> tuple:
    """Optional interactive light check: show the package, offer to confirm or steer.

    Recommended for high-stakes / non-obvious positioning; still NON-BLOCKING — the default is to
    proceed. Returns ("PROCEED", note) or ("STEER", note); a STEER re-enters the affected stage.
    """
    print("\n=== DIRECTION CHECK (optional) — confirm or steer before the next stage ===")
    print(pkg)
    raw = input("\nProceed to the next stage, or steer? [PROCEED / STEER] (default PROCEED): ").strip().lower()
    note = input("Steer/note (optional): ").strip()
    if raw in ("steer", "s", "revise", "r"):
        return ("STEER", note)
    return ("PROCEED", note)  # default: proceed (non-blocking)


# ---------------------------------------------------------------------------
# The mission loop
# ---------------------------------------------------------------------------

def run_mission(
    goal: str,
    dc1_fn=auto_proceed,
    dc2_fn=auto_proceed,
) -> dict:
    """Drive the full 3-stage loop with two optional direction checks. Returns the dossier.

    One commander call per outer iteration handles all 3 stages (DISCOVER → STRATEGISE+SHAPE →
    DELIVER).  Direction checks are offered after the commander returns:
      DC-1 STEER  → add steer note to required_fixes, increment outer iteration, re-run full.
      DC-2 STEER  → re-run the commander WITHOUT incrementing the outer iteration counter.
    Inspector VETO / PASS_WITH_FIXES → add required_fixes, loop outer iteration.
    """
    dossier = new_dossier(goal)
    required_fixes: list = []
    deliverable = ""

    while dossier["iteration"] < MAX_ITERS:
        dossier["iteration"] += 1
        print(f"\n=== ITERATION {dossier['iteration']}/{MAX_ITERS} ===")

        # ── Single commander call: all 3 stages in one prompt ─────────────
        mission_result = Runner.run_sync(commander, mission_brief(dossier, required_fixes))
        mission_output = mission_result.final_output
        required_fixes = []

        # ── Direction Check 1 (non-blocking; default auto-proceed) ────────
        dc1_choice, dc1_note = dc1_fn(mission_output)
        dossier["direction_check_1"] = {
            "iteration": dossier["iteration"],
            "choice": dc1_choice,
            "note": dc1_note,
        }
        print(f"Direction check 1: {dc1_choice}" + (f" — {dc1_note}" if dc1_note else ""))

        if dc1_choice == "STEER":
            required_fixes = [
                "Direction steer before strategy: "
                + (dc1_note or "steer the discovery brief")
            ]
            continue  # increment outer iteration; re-run full mission

        # ── Direction Check 2 inner loop (no outer iteration bump on STEER) ──
        while True:
            dc2_choice, dc2_note = dc2_fn(mission_output)
            dossier["direction_check_2"] = {
                "iteration": dossier["iteration"],
                "choice": dc2_choice,
                "note": dc2_note,
            }
            print(f"Direction check 2: {dc2_choice}" + (f" — {dc2_note}" if dc2_note else ""))

            if dc2_choice != "STEER":
                break

            # Re-run commander with steer; outer iteration counter stays the same.
            steer_fixes = [
                "Direction steer before delivery: "
                + (dc2_note or "steer the strategy and shape")
            ]
            mission_result = Runner.run_sync(commander, mission_brief(dossier, steer_fixes))
            mission_output = mission_result.final_output

        deliverable = mission_output

        # ── FINAL Inspector verdict ────────────────────────────────────────
        inspection = Runner.run_sync(
            inspector,
            "MODE: FINAL. Inspect this deliverable (sources / ethics & compliance / quality) "
            "and end with a clear verdict line — PASS, PASS WITH FIXES, or VETO — plus the "
            "required fixes as bullet lines:\n\n" + deliverable,
        )
        verdict = parse_verdict(inspection.final_output)
        required_fixes = extract_required_fixes(inspection.final_output)
        dossier["verdicts"].append({
            "iteration": dossier["iteration"],
            "verdict": verdict,
            "required_fixes": required_fixes,
        })
        print(f"Inspector verdict: {verdict}  ({len(required_fixes)} required fix(es))")

        if verdict == "PASS":
            dossier["delivered"] = deliverable
            return dossier
        # VETO, PASS_WITH_FIXES, or UNCLEAR → loop with required fixes; full re-run.

    # Iteration cap reached: deliver the best result with residual risk stated.
    dossier["delivered"] = deliverable
    dossier["residual_risk"] = (
        "Iteration cap reached without a clean PASS. Delivered the best result; "
        f"unresolved required fixes: {required_fixes}; "
        f"open_to_verify: {dossier['open_to_verify']}."
    )
    return dossier


# ---------------------------------------------------------------------------
# Console entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Console-script entry point (`product-kit-mission "<goal>"`)."""
    goal = sys.argv[1] if len(sys.argv) > 1 else "We have a product goal: ... (describe it)"
    # Non-blocking auto-proceed by default; inject console_direction_check (or a custom callable)
    # as direction_check_1_fn / direction_check_2_fn to enable interactive steering.
    final = run_mission(goal)
    print("\n=== DELIVERED ===")
    print(final.get("delivered", "(nothing)"))
    if final.get("residual_risk"):
        print("\n=== RESIDUAL RISK ===")
        print(final["residual_risk"])


if __name__ == "__main__":
    main()
