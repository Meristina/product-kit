# Research basis — Product-Kit doctrine

The 6-officer doctrine and 30-soldier roster (+ 36 enrichment candidates) are grounded
in one multi-domain benchmark pass — 10 parallel research agents, 6 synthesis agents,
1 report compiler — covering 90+ organisations. Raw report: `docs/BENCHMARK_ENRICHMENT.md`.

- Pass 1 (run `wf_02d95afe-726`): 10 domains × parallel sweep →
  McKinsey/BCG/Bain, Amazon Working Backwards, Google/Meta/Apple, Spotify/Netflix/Basecamp/Airbnb,
  B2B agencies, communication & creative agencies, design firms (IDEO/frog/GV),
  Growth/PLG (Reforge/Amplitude/OpenView), hardware/CPG/service products, Agile/SAFe enterprise.
- Synthesis: 6 officer-level agents mapping findings → enrichments + new soldiers + doctrine.
- Output: 31 existing-soldier enrichments, 36 new-soldier recommendations, 45 doctrine upgrades.

---

## Strategic verdict

Product management is **converging on outcome-driven, continuous-discovery operating models**,
pushing back against feature-factory and roadmap-as-commitment cultures.
The dominant directive is **dual-track discovery+delivery** — the resolution to the open
tension between discovery (Lean Startup: ship fast, pivot) and delivery (execute commitments).
Both extremes fail; the field has independently reached this conclusion across consulting
(BCG pilot-before-scale), tech (Spotify dual-track, Basecamp Shape Up), and design
(IDEO empathise-before-define).

Three cross-domain structural convergences:

1. **Problem before solution, always.** McKinsey (Problem Statement Worksheet, MECE issue tree),
   IDEO (Empathise → Define before Ideate), Amazon (PR/FAQ before roadmap), Torres (OST desired
   outcome before opportunity nodes) — every serious framework enforces a structured problem
   definition phase before solution work begins.

2. **Discovery is a rhythm, not a sprint.** P&G "Living It" programme (ethnographic immersion
   → Swiffer, Febreze repositioning), Torres's 1-interview/week/team standard, and the B2B
   multi-role VoC discipline (AIM Institute) all contradict the quarterly-discovery-sprint model.

3. **Measurement requires input metrics, not just output metrics.** Amazon WBR (200+ controllable
   input metrics), McKinsey Value Bridge (Finance-validated run-rate vs. one-time gains), and
   Amplitude North Star Playbook (NSM one abstraction above what teams directly control) share
   the same architecture: the PM's job is to identify and move the right inputs, not to manage
   lagging indicators.

---

## Verified findings (high confidence unless noted)

### O1 — Discovery & Research

- **JTBD is a pipeline, not a single tool.** Correct sequence: (1) Moesta timeline interview
  (The ReWired Group) — 4 forces diagram (push/pull/anxiety/habit), chronological retelling of
  the switching journey; (2) ODI (Ulwick/Strategyn, 300+ engagements) — 50-150 outcome
  statements, format `direction + metric + object + context`, opportunity score =
  `importance + max(importance − satisfaction, 0)`, threshold >10 = underserved, <5 = overserved;
  (3) OST (Torres, Product Talk) — desired outcome → opportunities → solutions → assumption tests.
  Using any one of these alone leaves a structural gap. Not alternatives. Sequential.

- **Qualitative before quantitative — sequencing is obligatory.** Surveys launched before
  observational research capture stated opinions, not discovery. P&G "Living It": immersion
  fieldwork surfaced Swiffer (new category) and Febreze repositioning (from air freshener to
  odour eliminator) — neither findable via focus groups or surveys alone.

- **Continuous discovery rhythm vs. discovery sprint (Teresa Torres).** Minimum viable
  cadence: 1 user interview/week/product team via automated recruitment pipelines
  (Calendly + Respondent). Quarterly discovery sprints are project research mode, appropriate
  for entering a new domain; conflating them with operational cadence is the most common O1
  anti-pattern.

- **MECE as a quality standard for research programmes (McKinsey/BCG).** Research questions
  covering overlapping or incomplete territory produce high-quality data on the wrong problem.
  Issue trees must be Mutually Exclusive, Collectively Exhaustive before fieldwork begins.

- **B2B discovery requires multi-role research (AIM Institute / New Product Blueprinting).**
  Minimum 4 separate sessions: economic buyer (ROI/risk), technical evaluator (integration/
  reliability), end user (ergonomics/efficiency), procurement (compliance/vendor risk).
  Consumer-grade single-respondent surveys applied to B2B enterprise product fail structurally.

- **HMW (How Might We) is a translation artefact, not ideation.** Correct placement:
  after research synthesis, before OST opportunity mapping. Moving it to design workshops (O4)
  skips the validation that the opportunity is real.
  — Google Ventures, Jake Knapp, *Sprint* (2016); IDEO Design Thinking.

### O2 — Strategy & Direction

- **Amazon PR/FAQ as vision discipline.** The imagined press release (headline + customer
  problem + solution + company quote + customer quote + CTA) IS the product vision, not a
  summary of it. Forces resolution of `who is the customer`, `what is the exact problem`,
  `is the market large enough` before any engineering commitment. Fire Phone = canonical
  failure case for skipping this gate. 10+ drafts, 1-3 weeks, 5+ senior leadership reviews
  is standard for major initiatives.
  — Colin Bryar & Bill Carr, *Working Backwards* (2021).

- **North Star Metric must sit one abstraction above what teams directly control (John Cutler,
  Amplitude, 2019).** If teams can move the NSM by shipping a feature, it is an operational KPI,
  not a North Star. Counter-metrics/guardrails are not optional: without them teams optimise
  the NSM while degrading unmeasured dimensions. Meta evolution: DAU → DAU/MAU → Family DAP —
  NSMs must be redefined when product scope expands.
  — Amplitude *North Star Playbook*.

- **OKRs — genealogy and correct mechanics.** Andy Grove (Intel, MBO→OKR, 1983) → John Doerr
  (Kleiner Perkins, Google 1999). Grove's design intent: decouple ambitious targets from
  compensation. Target 0.6-0.7 attainment = the psychological safety mechanism; score 1.0 is
  a diagnostic signal of sandbagging, not excellence. Four endemic failure modes: too many OKRs
  (>5/level), tactical OKRs, cascading compliance, compensation coupling. OKRs ≠ KPIs:
  OKRs are hypothesis-driven improvement targets; KPIs are operational health indicators
  requiring a defined range. Conflating them destroys both.
  — John Doerr, *Measure What Matters* (2018); Grove, *High Output Management* (1983).

- **PMF is a treadmill, not a milestone (Casey Winters & Fareed Mosavat, Reforge).** Consumer
  expectations accumulate upward over time. Chegg 2024: 90% valuation collapse, −500K subscribers
  in 10 months — canonical PMF Treadmill failure. PMF must be re-evaluated on a recurring trigger,
  not treated as a one-time certification.

- **Outcome roadmaps — three validated formats (non-competing):** Netflix Now/Next/Later
  (Now = in progress, Next = shaped+prioritised, Later = deliberately vague and revisable without
  apology); Basecamp betting table (Singer, 2019) — unselected work is *dropped*, not backlogged,
  circuit breaker enforced; Airbnb 18-month clear visibility / 3-year directional intentionally
  loose. Common signal: none of them commit past the current quarter.

- **Porter's Five Forces as prerequisite to market sizing (not just strategy).** A wide market
  can be structurally unattractive simultaneously. McKinsey and BCG apply Five Forces in the
  Discovery phase to answer "is this market worth competing in?" before any sizing estimate.
  Sizing without Five Forces produces a number without a verdict.
  — Michael Porter, *Competitive Strategy* (1980).

### O3 — Prioritization

- **RICE Confidence is the weakest dimension — replace with ODI calibration.** Confidence
  as a subjective score introduces gut-feel back into a scoring framework. Calibrate instead
  with the ODI opportunity score (Ulwick): score >10 raises Confidence; score <5 suppresses it.
  — Tony Ulwick, *Jobs to Be Done* (2016), Strategyn.

- **RAPID decision framework (Bain & Company).** RICE, GIST, Impact-Effort all address WHAT
  to prioritise but not WHO has the authority to finalise it. Diffuse decision ownership produces
  decisions that reverse after the meeting. RAPID: Recommend, Agree (narrow pre-defined veto),
  Perform, Input, Decide — one Decider, one name, never a group. Bain research: organisations
  deploying RAPID show 3× revenue growth, +27 NPS employee points vs. controls.
  — Bain & Company; HBR "Who Has the D?" (2006).

- **Basecamp Betting Table circuit breaker (Ryan Singer, Shape Up, 2019).** Unselected work
  is dropped, not parked. It must re-justify itself from zero if it resurfaces. The default
  assumption — that unselected items should be conserved in backlog — causes ghost priorities
  accumulation. Appetite (how much time is this worth?) vs. estimate (how long will this take?)
  is the core scoping distinction.
  — Ryan Singer, *Shape Up* (Basecamp/37signals, 2019). Available free at basecamp.com/shapeup.

- **Stage-Gate (Robert Cooper) — kill decisions are as important as go decisions.**
  4 gate outcomes: Go, Kill, Hold, Recycle. The documented value (60+ industrial studies, Cooper)
  comes from killing weak concepts before capital escalates — not from process compliance.
  — Robert G. Cooper, *Winning at New Products* (Stage-Gate International).

- **Single-threaded ownership — Amazon STL audit.** "Is there one person 100% dedicated —
  not in matrix mode — to this initiative?" A "no" removes the initiative from the priority list
  regardless of RICE score. No scoring methodology compensates for diffuse ownership.
  — Amazon OP1 review standard; Bryar & Carr, *Working Backwards*.

### O4 — Design & Validation

- **Four-hypothesis taxonomy (Teresa Torres, OST).** Every assumption is exactly one of:
  desirability (will users want this?), viability (can we sustain it commercially?),
  feasibility (can we build it?), usability (can users operate it?). Cheapest test per category:
  fake door / smoke test (desirability), financial modelling (viability), engineering spike
  (feasibility), task-based usability test (usability). Test selection by
  (cost of test × severity of risk), not by category.

- **Heuristic evaluation precedes user testing — not an alternative (Jakob Nielsen/NNg).**
  3-5 independent experts applying Nielsen's 10 heuristics detect ~65% of usability issues
  before a single participant session. Anti-pattern: teams who skip heuristic evaluation and go
  directly to user testing waste participant capacity and budget on defects any trained
  practitioner would have found in two hours.

- **Design Sprint Day 5: binary hypothesis validation, not statistical measure (GV/Knapp).**
  5 users produce a qualitative binary answer to a specific risk hypothesis — not statistical
  significance. Requesting larger sprint test groups confuses validation (does this concept work?)
  with measurement (how much does it improve a metric?). The Design Sprint is a hypothesis-testing
  ritual; its output is a validated or refuted hypothesis, not shipped code.
  — Jake Knapp, John Zeratsky, Braden Kowitz, *Sprint* (2016).

- **Service blueprints are a mandatory handoff artefact for products with a service layer.**
  Any product with a human service layer (onboarding, support, implementation, customer success)
  requires a service blueprint before O5 delivery handoff. Backstage capacity bottlenecks,
  broken handoffs, and staff dependency chains that are invisible in journey maps and prototypes
  become launch failures.
  — frog/Fjord service design methodology (frontstage/backstage, line of visibility).

- **IBM documented 75% reduction in design and implementation times with design thinking.**
  IDEO design thinking: empathise, define, ideate, prototype, test — where "define" produces the
  problem statement that constrains "ideate". HMW framing is the bridge between define and ideate.
  — IBM *Design Thinking* impact study (2018); IDEO Design Thinking.

### O5 — Delivery

- **Deployment ≠ Release. Feature flags decouple them structurally.** Deploy code to production
  continuously at 0% of users, then 1%, 10%, 100%. Four distinct flag types: release toggles
  (temporary, removed after rollout), experiment toggles (A/B & multivariate), ops toggles
  (circuit breakers, graceful degradation), permission toggles (beta access, entitlements).
  Flags require a hard expiry date at creation and a lifecycle policy.
  Without flags, trunk-based development requires every merged feature to be production-ready
  in one sprint — operationally impossible for multi-sprint features.
  — OpenFeature (CNCF, 2022) = vendor-neutral SDK standard.

- **Velocity is a planning heuristic, not a performance KPI (Accelerate, Forsgren et al.).**
  Using velocity as a management metric degrades delivery quality via three mechanisms:
  story-point inflation, commitment sandbagging, optimising for completion rate over customer
  outcome. Replace cross-team velocity comparisons with flow metrics (cycle time, throughput) —
  system-level, manipulation-resistant, tied to customer-side delivery speed via Little's Law.
  — Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (2018).

- **70-90% of delivery lead time is wait time, not execution time (Value Stream Mapping,
  Lean Enterprise Institute).** VSM applied to software delivery consistently finds that the
  dominant cause of slowness is inter-function handoff queues, not individual developer speed.
  Investments in making engineers faster have near-zero effect when the constraint is a QA
  bottleneck or a deployment approval gate.
  — Lean Enterprise Institute; Gene Kim, *The Phoenix Project* (2013); Goldratt TOC.

- **DORA metrics: 4 + Rework Rate (2024 update).** Deployment Frequency, Lead Time for Changes,
  Change Failure Rate, Mean Time to Restore + Rework Rate (2024 State of DevOps Report).
  Elite vs. low performers: 182× more frequent deployments, 127× faster lead time. Three
  architectural prerequisites for DORA elite performance: trunk-based development, full test
  automation, loosely coupled architecture.
  — Forsgren, Humble, Kim, *Accelerate* (2018); DORA 2024 State of DevOps Report.

- **SAFe usage reflects political palatability, not agility (contested).** SAFe used by 70%+
  of Fortune 100 in 2025. Endemic anti-patterns: PI Planning collapsing into 2-day waterfall
  plans; component ARTs posing as value-stream ARTs; velocity comparisons replacing outcome
  measurement. Encode as a tension, not a dismissal — SAFe can work if used as designed.

### O6 — Measurement & Learning

- **Input metrics vs. output metrics — Amazon WBR discipline.** Revenues, profits, conversion
  rates cannot be directly or durably manipulated as product levers. The PM's job is to identify
  and move the controllable input metrics (selection speed, quality, frequency) that cause
  outputs. Amazon WBR: 200+ input metrics reviewed weekly in 60 minutes. Identifying the right
  input metrics is "deceptively difficult and requires repeated trial and error" (Bezos).
  — Bryar & Carr, *Working Backwards* (2021).

- **Cohort retention flattening = hardest-to-falsify PMF signal.** A cohort curve that
  flattens horizontally (stops declining) is stronger evidence than any survey. DAU/MAU >50%
  for daily-habit products = behavioural PMF signal. Ellis 40% survey requires 100+ active
  users from the last 14 days to be valid; falls below that threshold it is uninformative.
  Empirical benchmarks: B2B weekly-active retention 44.6%–77.9%; 60-70% of annual SaaS churn
  occurs in the first 90 days.
  — Lenny Rachitsky & Yuriy Timen (500+ products study); Amplitude; Reforge.

- **COE (Correction of Errors) — Amazon post-mortem discipline.** 8 mandatory components:
  summary, impact, timeline, metrics, incident questions, Five Whys to systemic failure,
  action items (with owners + deadlines), related items. The COE is the mechanism converting
  launch failures into durable system improvements — not a blame attribution exercise.
  — Amazon product development post-mortem standard.

- **McKinsey Value Bridge — measurement credibility for the C-suite.** A living ledger,
  co-owned with Finance, distinguishing one-time gains from run-rate improvements, with a
  named owner per metric. Without this, analytics remains a PM-internal instrument;
  with it, product-driven value is credible in board-level allocation decisions.

- **NRR > 100% = most capital-efficient growth lever at scale.** At $15M+ ARR, expansion
  represents 40% of total ARR growth for top performers. Four expansion mechanisms:
  seat expansion, usage expansion, feature upsell, multi-product cross-sell.
  Snowflake, Datadog, Slack as NRR-led growth archetypes.
  — OpenView Partners; Reforge PLG research.

---

## ⚠️ Do NOT cite (refuted or non-verifiable)

- **"50% of features are never used"** — origin untraceable; no peer-reviewed source;
  figure varies wildly across cited versions (37%, 45%, 64%). Do not use as motivation for
  discovery investment.
- **NPS as sole or primary growth driver (Reichheld, 2003)** — sector-level correlation,
  not causation. Verizon, American Airlines, and Deutsche Telekom all had industry-high NPS
  while declining in market share. Encode as a guardrail metric only, never as a North Star.
- **40% PMF threshold (Sean Ellis) as a universal law** — validated as a heuristic on a
  narrow sample of early-stage B2B/B2C SaaS products. Not applicable to hardware, physical
  products, marketplaces, enterprise software, or consumer apps. Cite with explicit scope.
- **Story-point benchmarks as productivity signal** — refuted by *Accelerate* (Forsgren et al.,
  2018, 33 000+ professionals). Velocity comparisons across teams or over time incentivise
  sandbagging and inflation, not improved delivery performance.
- **"Agentic AI replaces 2/3 of product management activities"** — forecast language, not
  measured outcome. Do not cite as current state.
- **SAFe = organisational agility** — SAFe is a coordination framework; its adoption
  correlates with political palatability (preserves management layers), not DORA elite
  performance. Cite with context.

---

## Tensions (encode as features, not bugs)

| Tension | Camp A | Camp B | Verdict encoded |
|---|---|---|---|
| Roadmap | Output (feature X by date Y) | Outcome (metric Y by quarter) | Outcome by default; output = communication adaptation, not strategy |
| Discovery vs. delivery | Lean Startup: ship fast, pivot | Dual-track: continuous discovery in parallel | Dual-track = the resolution; both extremes fail |
| RICE vs. conviction | Quantitative scoring | Judgment-based bets | RICE = forcing function for the conversation, not a truth machine |
| PLG vs. SLG | Product-led growth | Sales-led growth | ACV-dependent — no universal preference |
| Velocity vs. outcome | Story points/sprint | Flow metrics/DORA | Velocity ≠ health proxy; system-level flow metrics preferred |
| OKRs coupled to compensation | Accountability | Psychological safety | Coupling destroys both sandbagging prevention and safety simultaneously |
| SAFe vs. LeSS | Coordination at scale | Simplicity | Tension, not dismissal — SAFe can work if implemented as designed |

---

## Open / still-thin (for future passes)

- Specific product operating models of hardware companies beyond Apple (Tesla externals only).
- CPG-specific volumetric forecasting benchmarks beyond BASES/NielsenIQ.
- Current (2024-2026) primary source on the AI product manager role and AI-native product orgs.
- RevOps operating frameworks as they apply to PLG-SLG hybrid motions.
- Concrete governance models for product at scale beyond SAFe/Spotify (e.g., Haier RenDanHeYi).
- Physical product PM and software PM as a hybrid role (Tesla, Peloton, Sonos).

---

## Classic vs. modern (for soldier grading)

- **Classic, still foundational:** JTBD (Christensen/Ulwick), Porter Five Forces, BCG Matrix,
  Stage-Gate (Cooper), Kano model, Scrum ceremonies, OKRs (Grove/Doerr), AARRR (McClure).
- **Reframed / superseded:** Feature roadmaps → outcome roadmaps; loyalty-led retention →
  cohort-based activation; last-click → input metrics + NSM; velocity → DORA + flow metrics;
  MBO → OKRs (but OKRs themselves distorted when compensation-coupled).
- **Elite soldiers (🎖️) — deep reasoning, contested trade-offs, judgment-intensive):**
  JTBD pipeline, OST, PR/FAQ, RAPID, Betting Table, Four Risks, Service Blueprint,
  Design-to-Value, Value Bridge, COE/post-mortem, Outcome Roadmap, North Star.
- **Standard soldiers (🔵) — process-driven, structured output, automatable):**
  User Interview protocol, Kano survey, Market Sizing, HMW Reframing, Stakeholder Map,
  RICE, Impact-Effort Matrix, Heuristic Evaluation, Story Mapping, Feature Flags,
  DORA Metrics, Cohort Analysis, A/B Experiment protocol, PLG Flywheel.
