"""End-to-end harness test for the mission loop — no SDK, no network, no API key.

We inject a fake `agents` module into sys.modules BEFORE importing product_kit.mission
(the package and its officers/soldiers all do `from agents import ...` at import time and
call `.as_tool()` while building the graph). Then we drive `run_mission` by scripting
`Runner.run_sync` outputs and injecting `dc1_fn` / `dc2_fn`, covering the product-kit
control-flow branches:
  PROCEED->PASS            — happy path
  DC-1 STEER->loop         — loops back to the discover stage (increments iteration)
  DC-2 STEER->loop         — loops back to the strategise_shape stage (inner loop, no iteration bump)
  VETO->iteration cap      — MAX_ITERS VETOs produce residual_risk delivery
  PASS_WITH_FIXES->recheck — loops with required fixes until PASS

NB: unlike Solve-Kit there is NO mandatory HITL gate — both Direction Checks are optional
and non-blocking (default auto_proceed), so there is no NO-GO branch.

The `agents` SDK is stubbed in tests/conftest.py (shared, installed before any test imports).
"""

import pytest

from product_kit import mission


class _Result:
    def __init__(self, final_output):
        self.final_output = final_output


class ScriptedRunner:
    """Returns scripted final_outputs in order; records the calls made."""

    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.calls = []

    def run_sync(self, agent, inp):
        self.calls.append(getattr(agent, "name", None))
        return _Result(self.outputs.pop(0))


def _checker(sequence):
    """direction_check_fn returning (choice, note) from a scripted sequence."""
    seq = iter(sequence)

    def fn(_package):
        return (next(seq), "test")

    return fn


# ---- pure helpers ------------------------------------------------------------

@pytest.mark.parametrize("text,expected", [
    ("all good, PASS but also VETO on X", "VETO"),
    ("verdict: PASS WITH FIXES", "PASS_WITH_FIXES"),
    ("PASS-WITH-FIXES", "PASS_WITH_FIXES"),
    ("PASS", "PASS"),
    ("", "UNCLEAR"),
])
def test_parse_verdict_priority(text, expected):
    assert mission.parse_verdict(text) == expected


def test_required_fixes_extracted_by_prefix():
    txt = "intro\n- Required: cite the TAM figure\n- Fix: add opt-out\n- nice polish\n- BLOCKING: confirm scope"
    fixes = mission.extract_required_fixes(txt)
    assert len(fixes) == 3


# ---- the product-kit control-flow branches ----------------------------------

def test_discover_stage_runs_commander(monkeypatch):
    # single iteration: one commander call (discover→strategise_shape→deliver) → PASS inspector
    runner = ScriptedRunner(["DISCOVER OUTPUT", "VERDICT: PASS"])
    monkeypatch.setattr(mission, "Runner", runner)
    d = mission.run_mission("goal")
    assert "delivered" in d and "residual_risk" not in d
    assert d["iteration"] == 1
    assert d["verdicts"][-1]["verdict"] == "PASS"
    # the commander_product agent was invoked for the discover stage
    assert runner.calls[0] == "commander_product"


def test_direction_check_1_steer_loops(monkeypatch):
    # iter 1: commander → DC-1 STEER (loops back to discover, increments iteration)
    # iter 2: commander → DC-1 PROCEED → DC-2 PROCEED → inspector PASS
    runner = ScriptedRunner(["OUTPUT1", "OUTPUT2", "VERDICT: PASS"])
    monkeypatch.setattr(mission, "Runner", runner)
    d = mission.run_mission("goal", dc1_fn=_checker(["STEER", "PROCEED"]))
    assert d["iteration"] == 2
    assert "delivered" in d
    assert d["direction_check_1"]["choice"] == "PROCEED"
    # no inspector ran in iter 1 (STEER skipped it), so only 1 verdict
    assert len(d["verdicts"]) == 1


def test_direction_check_2_steer_loops(monkeypatch):
    # iter 1, pass 1: commander → DC-1 PROCEED → DC-2 STEER (inner loop, no iteration bump)
    # iter 1, pass 2: commander re-run → DC-2 PROCEED → inspector PASS
    runner = ScriptedRunner(["OUTPUT1", "OUTPUT2", "VERDICT: PASS"])
    monkeypatch.setattr(mission, "Runner", runner)
    d = mission.run_mission("goal", dc2_fn=_checker(["STEER", "PROCEED"]))
    assert d["iteration"] == 1  # DC-2 steer does NOT increment the outer iteration counter
    assert "delivered" in d
    assert d["direction_check_2"]["choice"] == "PROCEED"
    assert len(d["verdicts"]) == 1


def test_iteration_cap_delivers_with_residual_risk(monkeypatch):
    # every iteration: commander → VETO; after MAX_ITERS → residual_risk
    outputs = []
    for _ in range(mission.MAX_ITERS):
        outputs += ["OUTPUT", "VERDICT: VETO"]
    runner = ScriptedRunner(outputs)
    monkeypatch.setattr(mission, "Runner", runner)
    d = mission.run_mission("goal")
    assert d["iteration"] == mission.MAX_ITERS
    assert "residual_risk" in d
    assert d["verdicts"][-1]["verdict"] == "VETO"


def test_pass_with_fixes_reruns_inspector(monkeypatch):
    # iter 1: commander → PASS_WITH_FIXES (loops with fixes)
    # iter 2: commander → PASS (delivered)
    runner = ScriptedRunner(["OUTPUT1", "VERDICT: PASS WITH FIXES", "OUTPUT2", "VERDICT: PASS"])
    monkeypatch.setattr(mission, "Runner", runner)
    d = mission.run_mission("goal")
    assert d["iteration"] == 2
    assert "delivered" in d and "residual_risk" not in d
    assert d["verdicts"][0]["verdict"] == "PASS_WITH_FIXES"
    assert d["verdicts"][1]["verdict"] == "PASS"
