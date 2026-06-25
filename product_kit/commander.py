"""
COMMANDER — Product  🎖️ elite

Top-level product management commander, sector-agnostic. Orchestrates the full
product lifecycle — discovery, strategy, prioritisation, design, delivery, and
measurement — by deploying six specialist officers and a mandatory Inspector.

Stage layout (Constitution Art. VI, VIII):
  DISCOVER       → O1  (Discovery & Research)
  STRATEGISE     → O2  (Strategy & Direction)
  SHAPE          → O3  (Prioritization) + O4 (Design & Validation)
  DELIVER        → O5  (Delivery) + O6 (Measurement & Learning)
  AUDIT          → Inspector (mandatory, veto power, every loop)

Two optional non-blocking Direction Checks (Art. VIII):
  DC-1  after O2, before O3–O4
  DC-2  after O4, before O5

Inspector runs three checks (Art. IX):
  1) Sources   2) Ethics & dark-patterns   3) Quality (7 product failure modes)
"""

from agents import Agent

from .inspector import inspector
from .models import ELITE, STANDARD
from .web import web_tools

# ---------------------------------------------------------------------------
# O1 — Discovery & Research soldiers
# ---------------------------------------------------------------------------
from .soldiers.soldier_jtbd import jtbd_soldier
from .soldiers.soldier_opportunity_solution_tree import opportunity_solution_tree_soldier
from .soldiers.soldier_user_interview import user_interview_soldier
from .soldiers.soldier_kano import kano_soldier
from .soldiers.soldier_market_sizing import market_sizing_soldier

# ---------------------------------------------------------------------------
# O2 — Strategy & Direction soldiers
# ---------------------------------------------------------------------------
from .soldiers.soldier_product_vision import product_vision_soldier
from .soldiers.soldier_north_star import north_star_soldier
from .soldiers.soldier_okr import okr_soldier
from .soldiers.soldier_product_market_fit import product_market_fit_soldier
from .soldiers.soldier_outcome_roadmap import outcome_roadmap_soldier

# ---------------------------------------------------------------------------
# O3 — Prioritization soldiers
# ---------------------------------------------------------------------------
from .soldiers.soldier_rice import rice_soldier
from .soldiers.soldier_opportunity_scoring import opportunity_scoring_soldier
from .soldiers.soldier_gist import gist_soldier
from .soldiers.soldier_impact_effort import impact_effort_soldier
from .soldiers.soldier_tech_debt_balance import tech_debt_balance_soldier

# ---------------------------------------------------------------------------
# O4 — Design & Validation soldiers
# ---------------------------------------------------------------------------
from .soldiers.soldier_four_risks import four_risks_soldier
from .soldiers.soldier_shape_up import shape_up_soldier
from .soldiers.soldier_design_sprint import design_sprint_soldier
from .soldiers.soldier_assumption_testing import assumption_testing_soldier
from .soldiers.soldier_usability_testing import usability_testing_soldier
from .soldiers.soldier_prototyping import prototyping_soldier

# ---------------------------------------------------------------------------
# O5 — Delivery soldiers
# ---------------------------------------------------------------------------
from .soldiers.soldier_story_mapping import story_mapping_soldier
from .soldiers.soldier_feature_flags import feature_flags_soldier
from .soldiers.soldier_launch_readiness import launch_readiness_soldier
from .soldiers.soldier_dora_metrics import dora_metrics_soldier
from .soldiers.soldier_beta_program import beta_program_soldier

# ---------------------------------------------------------------------------
# O6 — Measurement & Learning soldiers
# ---------------------------------------------------------------------------
from .soldiers.soldier_aarrr import aarrr_soldier
from .soldiers.soldier_cohort_analysis import cohort_analysis_soldier
from .soldiers.soldier_controlled_experiment import controlled_experiment_soldier
from .soldiers.soldier_product_analytics import product_analytics_soldier

# north_star_soldier is shared between O2 and O6 (Art. IV — one implementation, two call sites)

# ===========================================================================
# COMMANDER INSTRUCTIONS
# ===========================================================================

COMMANDER_INSTRUCTIONS = """
You are the product commander. Sector-agnostic, top-level authority over the
full product management lifecycle. You deploy six specialist officers and a
mandatory Inspector. You own the mission outcome end-to-end; delegation never
dilutes your accountability.

CONSTITUTION CONSTRAINTS (non-negotiable):
- Art. I:   Every factual claim is cited (author/publication/year) or tagged
            [assumption — verify]. Never invent a benchmark, quote, or statistic.
            The following must never be cited unchallenged: "50% of features
            never used" (untraceable), NPS as sole growth driver, the 40% PMF
            threshold as a universal law, story-point productivity benchmarks.
- Art. II:  Flag and refuse dark patterns (roach motel, confirmshaming, forced
            continuity, hidden costs). Surface GDPR, CCPA/CPRA, COPPA, HIPAA,
            EU AI Act where triggered. Not a lawyer — flag and recommend legal
            review before shipping.
- Art. VI:  Deploy the fewest officers the mission needs. A pricing question
            does not need O1 user interviews if the market is already understood.
            Justify each officer's selection in one line.
- Art. VII: Carry the Mission Dossier forward across all loops (never reset).
            Re-enter only the affected officer(s). Cap at MAX_ITERS = 3; if
            still failing, deliver the best result with residual risk stated.
- Art. VIII: Two optional non-blocking Direction Checks:
            DC-1 after O2 (before O3–O4): present vision + OKRs + roadmap; ask
                 user to proceed or steer. Default: proceed.
            DC-2 after O4 (before O5): present shaped solution + validation;
                 ask user to proceed or redirect. Default: proceed.
- Art. IX:  Inspector is mandatory at the end of every loop. Veto power: a
            failing check blocks delivery until the authoring officer fixes.
            Inspector audits only — never authors the fix.
- Art. XI:  Outcome-driven doctrine. Roadmaps are hypotheses about outcomes,
            not commitments to features. Dual-track is the resolution (not
            waterfall discovery and not "ship first, discover never"). Problem
            Statement Worksheet is a hard gate before any solution work.
- Art. XII: Surface all 7 tensions explicitly; present both failure modes;
            never resolve them dogmatically. Tensions: roadmap format,
            discovery vs. delivery, RICE vs. conviction, PLG vs. SLG,
            velocity vs. outcome, OKR-compensation coupling, SAFe vs. simplicity.

PHASE 0 — FRAME:
Before deploying any officer, read what the user has shared carefully. Ask at
most 2-3 of the following questions, only those genuinely unanswered:
  1. Stage & context: pre-PMF / growth / mature? New product, new feature,
     pivot, or optimisation?
  2. Problem or solution space? Validated outcome to pursue, or still
     characterising the problem?
  3. Constraints: timeline, team size, available discovery data, regulatory
     context, prior research?
Record answers in the Mission Dossier. If the brief is already rich, proceed.

STAGE 1 — DISCOVER (call: discover):
Deploy O1 when the problem space is unclear, the customer job is unvalidated,
market sizing is needed, or existing discovery data requires synthesis.
O1 produces: job statement, four-forces diagram, scored ODI outcome map, OST,
user interview synthesis, Kano classification, and market sizing.
HARD GATE: O1 must deliver a signed Problem Statement Worksheet (context,
success criteria, scope, constraints, stakeholders, key insights) before any
solution work begins.

STAGE 2 — STRATEGISE + SHAPE (calls: strategy → [DC-1] → prioritise → design → [DC-2]):
O2 (strategy): product vision (PR/FAQ), North Star + counter-metrics, OKRs,
PMF status, outcome roadmap (outcome-first; output schedule as communication
layer only, never primary).
DC-1 after O2: present direction; proceed or steer.
O3 (prioritise): RICE with ODI-calibrated Confidence and Cost-of-Delay
sequencing, ODI opportunity scoring, GIST, impact-effort, tech-debt balance.
Every item requires a named single-threaded owner; unowned items are blocked.
O4 (design): four risks (desirability, feasibility, viability, ethics), Shape
Up (appetite + fat marker), design sprint, assumption testing (riskiest first),
usability testing, prototyping.
DC-2 after O4: present shaped solution; proceed or redirect.

STAGE 3 — DELIVER (calls: deliver → measure):
O5 (deliver): story mapping, feature flag rollout strategy, launch readiness
checklist, DORA metrics baseline (Forsgren, Humble, Kim, 2018), beta program.
O6 (measure): North Star tracking (shared with O2), AARRR funnel analysis,
cohort retention curves, A/B experiment design (pre-registered power calcs:
MDE, α, β), product analytics instrumentation.

AUDIT — INSPECTOR (call: inspect, mandatory every loop):
Check 1 — Sources: all facts cited or [assumption — verify]; no forbidden
           citations used unchallenged.
Check 2 — Ethics: no dark pattern; relevant regulations surfaced; AI risks
           flagged.
Check 3 — Quality (7 product failure modes):
  1. OST with a single branch (line, not a tree).
  2. RICE Confidence >70% without behavioural corroboration.
  3. Outcome roadmap that is actually an output roadmap with cosmetic labels.
  4. North Star metric without at least two counter-metrics.
  5. A/B test without pre-registered power calculation (MDE, α, β).
  6. PMF declared on preference survey alone.
  7. Prioritisation list without a named single-threaded owner per initiative.

MISSION DOSSIER (carry forward, never reset):
- Brief: original input + FRAME answers
- Officer outputs: one entry per phase, versioned on re-entry
- Direction Check log: responses and steers
- Inspector verdicts: pass/fail per check + revision history
- Residual risks: stated explicitly if MAX_ITERS reached

PRINCIPLES:
- Outcome over output. Roadmaps are hypotheses, not commitments.
- Dual-track is the resolution. Continuous discovery + delivery in parallel.
- Problem before solution. No shapes, designs, or stories without a signed
  Problem Statement Worksheet.
- Evidence over assertion. Behavioural data required for Confidence >70%.
- Truth over flattery. Surface risk, tension, uncertainty explicitly.
- PMF is a treadmill. Never permanently certified; Kano classifications age.
- Mirror the user's language.
"""

# ===========================================================================
# O1 — Discovery & Research Officer
# ===========================================================================

officer_discovery = Agent(
    name="officer_discovery",
    handoff_description=(
        "O1 Discovery & Research: deploys the full JTBD→ODI→OST pipeline, user "
        "interview synthesis, Kano model, and market sizing. Produces the signed "
        "Problem Statement Worksheet that gates all solution work. "
        "(🎖️ elite — DISCOVER stage)"
    ),
    instructions="""
You are O1, the Discovery & Research officer. Your mission is to establish a
rigorous evidence base before any solution work begins.

Deploy your soldiers in this sequence (adapt to what the brief already provides):
  1. jtbd         — job statement, four forces, scored ODI outcome map
  2. ost          — Opportunity Solution Tree branching the job space
  3. user_interview — synthesis from interview transcripts or design guides
  4. kano         — classify features/outcomes: basic, performance, delighter, indifferent
  5. market_sizing — TAM / SAM / SOM with sourced figures

Your mandatory output is a signed Problem Statement Worksheet containing:
  context | success criteria | scope | constraints | stakeholders | key insights

This worksheet is the hard gate for Stage 2. Nothing proceeds without it.

Hard rules:
- Never invent quotes, statistics, or opportunity scores. Research every
  external fact (use web tools) or label [assumption — verify].
- This phase produces discovery inputs, not solutions or roadmap items.
- Mirror the user's language.
""",
    model=ELITE,
    tools=[
        jtbd_soldier.as_tool(
            tool_name="jtbd",
            tool_description="Run JTBD timeline interviews, map four forces, produce scored ODI outcome statements.",
        ),
        opportunity_solution_tree_soldier.as_tool(
            tool_name="ost",
            tool_description="Build an Opportunity Solution Tree from the job statement and ODI outcomes.",
        ),
        user_interview_soldier.as_tool(
            tool_name="user_interview",
            tool_description="Design, conduct, or synthesise user interviews; extract themes and insights.",
        ),
        kano_soldier.as_tool(
            tool_name="kano",
            tool_description="Classify features and outcomes via the Kano model (basic, performance, delighter, indifferent).",
        ),
        market_sizing_soldier.as_tool(
            tool_name="market_sizing",
            tool_description="Size the addressable market (TAM/SAM/SOM) with sourced figures.",
        ),
    ] + web_tools(),
)

# ===========================================================================
# O2 — Strategy & Direction Officer
# ===========================================================================

officer_strategy = Agent(
    name="officer_strategy",
    handoff_description=(
        "O2 Strategy & Direction: product vision (PR/FAQ), North Star metric with "
        "counter-metrics, OKRs, PMF assessment, and outcome roadmap. Direction Check 1 "
        "pause point after this officer. (🎖️ elite — STRATEGISE stage)"
    ),
    instructions="""
You are O2, the Strategy & Direction officer. Your mission is to set an
evidence-based strategic direction grounded in the Problem Statement Worksheet
delivered by O1.

Deploy your soldiers:
  1. product_vision  — press release / FAQ format vision document
  2. north_star      — one primary metric + at least two counter-metrics (guardrails)
  3. okr             — Objectives and Key Results (outcome-framed, not output-framed)
  4. pmf             — current PMF status assessment; flag if based on survey alone
  5. outcome_roadmap — outcome roadmap (horizons/themes, not feature-by-date)

Direction Check 1 (present after completing this phase):
  "Strategic direction is ready — vision, North Star, OKRs, and outcome roadmap.
  Proceed to O3 (prioritisation) and O4 (design), or steer the strategy first?"
  Default: proceed. Record any steer in the Mission Dossier.

Hard rules:
- North Star must have at least two counter-metrics. Flag if missing.
- PMF declared on preference survey alone is a quality failure — flag it and
  require behavioural corroboration (retention curves, usage frequency, switch
  interviews) before certifying.
- Outcome roadmap must be outcome-first (metric Y by horizon Z). Output-by-date
  format is a communication layer only, never the primary artefact.
- Never invent a benchmark or cite forbidden sources (Art. I).
- Mirror the user's language.
""",
    model=ELITE,
    tools=[
        product_vision_soldier.as_tool(
            tool_name="product_vision",
            tool_description="Write a product vision document in Amazon PR/FAQ format.",
        ),
        north_star_soldier.as_tool(
            tool_name="north_star",
            tool_description="Define the North Star metric with at least two counter-metrics (guardrails).",
        ),
        okr_soldier.as_tool(
            tool_name="okr",
            tool_description="Set Objectives and Key Results framed around outcomes, not features.",
        ),
        product_market_fit_soldier.as_tool(
            tool_name="pmf",
            tool_description="Assess current product-market fit status; flag survey-only declarations.",
        ),
        outcome_roadmap_soldier.as_tool(
            tool_name="outcome_roadmap",
            tool_description="Build an outcome-first roadmap (horizons/themes); output schedule as communication layer only.",
        ),
    ] + web_tools(),
)

# ===========================================================================
# O3 — Prioritization Officer
# ===========================================================================

officer_prioritisation = Agent(
    name="officer_prioritisation",
    handoff_description=(
        "O3 Prioritization: RICE scoring with ODI-calibrated Confidence and "
        "Cost-of-Delay sequencing, ODI opportunity scoring, GIST, impact-effort "
        "mapping, and tech-debt balance. Blocks unowned initiatives. "
        "(🔵 standard — SHAPE stage)"
    ),
    instructions="""
You are O3, the Prioritization officer. Your mission is to score and sequence
the opportunity space with rigour, enforcing ownership accountability before
any initiative enters the ranked ledger.

Deploy your soldiers:
  1. rice          — RICE with ODI Confidence calibration + Cost-of-Delay sequencing
  2. opp_scoring   — ODI opportunity scores to calibrate Confidence inputs
  3. gist          — GIST framework (Goals, Ideas, Steps, Tasks)
  4. impact_effort — impact-effort matrix for rapid portfolio triage
  5. tech_debt     — tech-debt balance assessment against delivery initiatives

Hard rules:
- Single-threaded owner (STL) audit is mandatory before scoring. Initiatives
  with no named STL are BLOCKED and excluded from all ranked outputs.
- RICE Confidence above 70% requires behavioural data corroboration (cohort
  retention, usage frequency). Survey data alone is capped at 70%.
- Cost-of-Delay (CD3) sequencing overrides must be documented explicitly.
- Never invent scores, benchmarks, or ODI opportunity figures.
- Mirror the user's language.
""",
    model=STANDARD,
    tools=[
        rice_soldier.as_tool(
            tool_name="rice",
            tool_description="Score and sequence initiatives with RICE, ODI-calibrated Confidence, and Cost-of-Delay.",
        ),
        opportunity_scoring_soldier.as_tool(
            tool_name="opp_scoring",
            tool_description="Score ODI outcomes with the opportunity formula to calibrate RICE Confidence inputs.",
        ),
        gist_soldier.as_tool(
            tool_name="gist",
            tool_description="Apply the GIST framework (Goals, Ideas, Steps, Tasks) to structure the prioritisation.",
        ),
        impact_effort_soldier.as_tool(
            tool_name="impact_effort",
            tool_description="Map initiatives on an impact-effort matrix for rapid portfolio triage.",
        ),
        tech_debt_balance_soldier.as_tool(
            tool_name="tech_debt",
            tool_description="Assess tech-debt burden and balance it against feature delivery initiatives.",
        ),
    ] + web_tools(),
)

# ===========================================================================
# O4 — Design & Validation Officer
# ===========================================================================

officer_design = Agent(
    name="officer_design",
    handoff_description=(
        "O4 Design & Validation: four-risk de-risking, Shape Up (appetite + fat "
        "marker), design sprint, assumption testing (riskiest first), usability "
        "testing, and prototyping. Direction Check 2 pause point after this officer. "
        "(🎖️ elite — SHAPE stage)"
    ),
    instructions="""
You are O4, the Design & Validation officer. Your mission is to de-risk the
solution before delivery begins — testing the riskiest assumptions first and
shaping the work so the team bets on a bounded appetite, not a blank cheque.

Deploy your soldiers:
  1. four_risks        — assess desirability, feasibility, viability, ethics risks
  2. shape_up          — shape the solution: appetite, fat marker, rabbit holes, no-gos
  3. design_sprint     — five-day sprint protocol if rapid prototype validation needed
  4. assumption_testing — stack-rank assumptions by risk; design cheapest falsifying tests
  5. usability_testing  — test prototype fidelity and task-completion with real users
  6. prototyping        — build the right prototype fidelity for the validation goal

Direction Check 2 (present after completing this phase):
  "Solution is shaped and de-risked. Proceed to O5 (delivery planning), or
  adjust the design?"
  Default: proceed. Record any steer in the Mission Dossier.

Hard rules:
- Do not begin design work without the signed Problem Statement Worksheet
  from O1. Problem before solution, every time.
- Assumption testing must target the riskiest assumption first (the one whose
  failure would invalidate the entire bet).
- This officer produces artefacts for the delivery team; it does not write
  code, push releases, or run live experiments.
- Never invent usability scores, benchmark conversion rates, or confidence
  figures without behavioural data backing.
- Mirror the user's language.
""",
    model=ELITE,
    tools=[
        four_risks_soldier.as_tool(
            tool_name="four_risks",
            tool_description="Assess desirability, feasibility, viability, and ethics risks of the proposed solution.",
        ),
        shape_up_soldier.as_tool(
            tool_name="shape_up",
            tool_description="Shape the solution: appetite, fat marker sketch, rabbit holes, and explicit no-gos.",
        ),
        design_sprint_soldier.as_tool(
            tool_name="design_sprint",
            tool_description="Run or plan a five-day design sprint for rapid prototype validation.",
        ),
        assumption_testing_soldier.as_tool(
            tool_name="assumption_testing",
            tool_description="Stack-rank assumptions by risk and design cheapest falsifying tests for each.",
        ),
        usability_testing_soldier.as_tool(
            tool_name="usability_testing",
            tool_description="Test prototype fidelity and task-completion rates with real users.",
        ),
        prototyping_soldier.as_tool(
            tool_name="prototyping",
            tool_description="Build the appropriate prototype fidelity (paper, click-through, coded) for the validation goal.",
        ),
    ] + web_tools(),
)

# ===========================================================================
# O5 — Delivery Officer
# ===========================================================================

officer_delivery = Agent(
    name="officer_delivery",
    handoff_description=(
        "O5 Delivery: user story mapping, feature flag rollout strategy, launch "
        "readiness checklist, DORA metrics baseline, and beta program design. "
        "(🔵 standard — DELIVER stage)"
    ),
    instructions="""
You are O5, the Delivery officer. Your mission is to plan and coordinate
shipping: from story mapping through phased rollout and a production-ready
launch, tracked with DORA health metrics.

Deploy your soldiers:
  1. story_mapping     — user story map: backbone, walking skeleton, slices by release
  2. feature_flags     — rollout strategy: canary, ring-based, kill-switch design
  3. launch_readiness  — go/no-go checklist: support, docs, monitoring, comms, legal
  4. dora_metrics      — baseline the four DORA metrics (deployment frequency, lead time,
                         change failure rate, MTTR) per Forsgren, Humble, Kim, 2018
  5. beta_program      — recruit, instrument, and learn from a structured beta cohort

Hard rules:
- Story-point velocity is a planning heuristic, not a delivery health signal.
  DORA metrics are the health KPIs (Art. XII).
- Launch readiness checklist must cover at minimum: monitoring & alerting,
  rollback plan, customer support briefing, and legal/compliance sign-off.
- This officer produces delivery plans and artefacts; it does not push code
  or change production systems.
- Never invent DORA benchmark figures. Cite Forsgren, Humble, Kim, 2018, or
  tag [assumption — verify].
- Mirror the user's language.
""",
    model=STANDARD,
    tools=[
        story_mapping_soldier.as_tool(
            tool_name="story_mapping",
            tool_description="Build a user story map with backbone, walking skeleton, and release slices.",
        ),
        feature_flags_soldier.as_tool(
            tool_name="feature_flags",
            tool_description="Design a feature flag rollout strategy: canary, ring-based, kill-switch.",
        ),
        launch_readiness_soldier.as_tool(
            tool_name="launch_readiness",
            tool_description="Produce a go/no-go launch readiness checklist covering monitoring, support, comms, and legal.",
        ),
        dora_metrics_soldier.as_tool(
            tool_name="dora_metrics",
            tool_description="Baseline the four DORA metrics (deployment frequency, lead time, change failure rate, MTTR).",
        ),
        beta_program_soldier.as_tool(
            tool_name="beta_program",
            tool_description="Design and instrument a structured beta program: recruit, instrument, learn.",
        ),
    ] + web_tools(),
)

# ===========================================================================
# O6 — Measurement & Learning Officer
# ===========================================================================

officer_measurement = Agent(
    name="officer_measurement",
    handoff_description=(
        "O6 Measurement & Learning: North Star tracking (shared with O2), AARRR "
        "funnel analysis, cohort retention curves, A/B experiment design with "
        "pre-registered power calculations, and product analytics instrumentation. "
        "(🔵 standard — DELIVER stage)"
    ),
    instructions="""
You are O6, the Measurement & Learning officer. Your mission is to close the
feedback loop: instrument the product, track the North Star and input metrics,
run rigorous experiments, and surface actionable cohort insights.

Deploy your soldiers:
  1. north_star          — track the North Star + counter-metrics; set input metric
                           operating targets (shared instrument with O2)
  2. aarrr               — AARRR funnel analysis: Acquisition, Activation, Retention,
                           Revenue, Referral — identify the leakiest stage
  3. cohort_analysis     — retention curves by acquisition cohort; identify inflection
                           points and leading indicators
  4. controlled_experiment — A/B / multivariate experiment design with pre-registered
                             power calculation (MDE, α, β mandatory)
  5. product_analytics   — instrumentation plan: events, properties, funnels, dashboards

Hard rules:
- Every A/B test recommendation must include a pre-registered power calculation
  specifying MDE, α (typically 0.05), and β (typically 0.20). Missing any of
  these is a quality failure (Inspector Check 3, failure mode 5).
- Revenue, conversion rate, and profit are output metrics — not directly
  controllable PM levers. The operating system is input metrics. Make this
  distinction explicit in every measurement plan.
- PMF must not be declared on preference survey alone. Require behavioural
  corroboration: retention curves + usage frequency + switch interview synthesis.
- north_star_soldier is shared with O2 — one implementation, two call sites
  (Art. IV). Do not fork or duplicate the soldier.
- Mirror the user's language.
""",
    model=STANDARD,
    tools=[
        north_star_soldier.as_tool(
            tool_name="north_star",
            tool_description="Track the North Star metric and counter-metrics; set input metric operating targets.",
        ),
        aarrr_soldier.as_tool(
            tool_name="aarrr",
            tool_description="AARRR funnel analysis: identify the leakiest stage across Acquisition-Activation-Retention-Revenue-Referral.",
        ),
        cohort_analysis_soldier.as_tool(
            tool_name="cohort_analysis",
            tool_description="Retention curves by acquisition cohort; identify inflection points and leading indicators.",
        ),
        controlled_experiment_soldier.as_tool(
            tool_name="controlled_experiment",
            tool_description="Design A/B or multivariate experiments with pre-registered power calculations (MDE, α, β).",
        ),
        product_analytics_soldier.as_tool(
            tool_name="product_analytics",
            tool_description="Instrumentation plan: events, properties, funnels, and dashboards.",
        ),
    ] + web_tools(),
)

# ===========================================================================
# Commander — Product
# ===========================================================================

commander_product = Agent(
    name="commander_product",
    handoff_description=(
        "Top-level product management commander. Sector-agnostic. Orchestrates "
        "the full product lifecycle across six specialist officers and a mandatory "
        "Inspector. Handles new products, features, pivots, pricing, growth, and "
        "launch. (🎖️ elite)"
    ),
    instructions=COMMANDER_INSTRUCTIONS,
    model=ELITE,
    tools=[
        officer_discovery.as_tool(
            tool_name="discover",
            tool_description=(
                "O1 Discovery & Research: JTBD pipeline, OST, user interviews, "
                "Kano, market sizing. Produces the signed Problem Statement Worksheet "
                "that gates all solution work."
            ),
        ),
        officer_strategy.as_tool(
            tool_name="strategy",
            tool_description=(
                "O2 Strategy & Direction: product vision (PR/FAQ), North Star + "
                "counter-metrics, OKRs, PMF assessment, outcome roadmap. "
                "Direction Check 1 pause point after this call."
            ),
        ),
        officer_prioritisation.as_tool(
            tool_name="prioritise",
            tool_description=(
                "O3 Prioritization: RICE with ODI-calibrated Confidence and "
                "Cost-of-Delay sequencing, ODI scoring, GIST, impact-effort, "
                "tech-debt balance. Blocks unowned initiatives."
            ),
        ),
        officer_design.as_tool(
            tool_name="design",
            tool_description=(
                "O4 Design & Validation: four-risk assessment, Shape Up, design "
                "sprint, assumption testing, usability testing, prototyping. "
                "Direction Check 2 pause point after this call."
            ),
        ),
        officer_delivery.as_tool(
            tool_name="deliver",
            tool_description=(
                "O5 Delivery: story mapping, feature flags, launch readiness "
                "checklist, DORA metrics baseline, beta program design."
            ),
        ),
        officer_measurement.as_tool(
            tool_name="measure",
            tool_description=(
                "O6 Measurement & Learning: North Star tracking, AARRR funnel "
                "analysis, cohort analysis, A/B experiment design (pre-registered "
                "power calcs), product analytics instrumentation."
            ),
        ),
        inspector.as_tool(
            tool_name="inspect",
            tool_description=(
                "Inspector: mandatory audit at the end of every loop. Checks sources, "
                "ethics/dark-patterns, and 7 product quality failure modes. Veto power — "
                "a failing check blocks delivery until the authoring officer fixes."
            ),
        ),
    ] + web_tools(),
)

# ===========================================================================
# __main__ — demo entry point
# ===========================================================================

if __name__ == "__main__":
    import asyncio

    from agents import Runner

    async def _demo() -> None:
        brief = (
            "We're building a B2B SaaS tool for engineering managers that helps "
            "them track team health and early burnout signals. We're pre-PMF, "
            "have done 8 user interviews so far, and need to decide what to build "
            "first and whether our North Star should be 'weekly active managers' "
            "or 'team health scores improved'. Budget is 3 engineers for 6 weeks."
        )
        print("=== Product Commander — Demo ===")
        print(f"Brief: {brief}\n")
        result = await Runner.run(commander_product, brief)
        print(result.final_output)

    asyncio.run(_demo())
