# Product-Kit

A generalist, sector-agnostic **product-management agent army** built on the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), portable across Claude and OpenAI.

Part of the **AI Agency** pattern — a collection of autonomous departments (alongside `solve-kit` and `marketing-kit`), each structured as a military hierarchy: Commander → Officers → Soldiers → Inspector.

---

## Architecture

```
Commander
 ├─ Officer 1 · Discovery & Research
 │   ├─ soldier-jtbd               🎖️  Jobs-to-be-Done (timeline interview · four forces · ODI)
 │   ├─ soldier-opportunity-solution-tree  🎖️  OST (desired outcome → opportunities → solutions)
 │   ├─ soldier-user-interview     🔵  User interview protocol (POEMS · Portigal)
 │   ├─ soldier-kano               🔵  Kano model (must-have / performance / delighter)
 │   └─ soldier-market-sizing      🔵  TAM / SAM / SOM + Porter Five Forces
 │
 ├─ Officer 2 · Strategy & Direction
 │   ├─ soldier-product-vision     🎖️  Amazon PR/FAQ gate + SCR communication
 │   ├─ soldier-north-star         🎖️  NSM + counter-metrics (shared with O6)
 │   ├─ soldier-okr                🔵  OKRs (0.6–0.7 ambition · decoupled from compensation)
 │   ├─ soldier-product-market-fit 🎖️  PMF (behavioural signals + PMF Treadmill)
 │   └─ soldier-outcome-roadmap    🎖️  Now/Next/Later + Shape Up circuit breaker + BCG overlay
 │
 ├─ Officer 3 · Prioritization
 │   ├─ soldier-rice               🔵  RICE (ODI-calibrated Confidence · CoD sequencing)
 │   ├─ soldier-opportunity-scoring 🎖️  ODI opportunity formula (importance + underservice gap)
 │   ├─ soldier-gist               🎖️  GIST (Goals/Ideas/Steps/Tasks + STL ownership audit)
 │   ├─ soldier-impact-effort      🔵  Impact-effort matrix + BCG portfolio overlay
 │   └─ soldier-tech-debt-balance  🔵  Muda/Muri/Mura + DORA signals + Scaling Work ring-fence
 │
 ├─ Officer 4 · Design & Validation
 │   ├─ soldier-four-risks         🎖️  Desirability / viability / feasibility / usability
 │   ├─ soldier-shape-up           🎖️  Shape Up (fat-marker shaping · appetite · circuit breaker)
 │   ├─ soldier-design-sprint      🎖️  5-day GV sprint (binary hypothesis validation)
 │   ├─ soldier-assumption-testing 🎖️  Test ladder (fake door → smoke → concierge → WoZ)
 │   ├─ soldier-usability-testing  🔵  Heuristic evaluation + rainbow spreadsheet
 │   └─ soldier-prototyping        🔵  Fidelity spectrum by learning objective
 │
 ├─ Officer 5 · Delivery
 │   ├─ soldier-story-mapping      🎖️  Backbone + walking skeleton + wave sequencing
 │   ├─ soldier-feature-flags      🔵  4-type taxonomy · progressive delivery · TBD enabler
 │   ├─ soldier-launch-readiness   🔵  6-component checklist (ops/CX/security/legal/metrics)
 │   ├─ soldier-dora-metrics       🔵  5 DORA metrics + Rework Rate + VSM complement
 │   └─ soldier-beta-program       🔵  Kill threshold + progressive rollout + COE review
 │
 ├─ Officer 6 · Measurement & Learning
 │   ├─ soldier-north-star         🎖️  (shared from O2) NSM + input-metrics tree
 │   ├─ soldier-aarrr              🔵  Pirate metrics · growth loops vs funnels
 │   ├─ soldier-cohort-analysis    🎖️  D1/D7/D30/D90 retention · AHA moment · PMF signal
 │   ├─ soldier-controlled-experiment 🎖️  Pre-registered hypothesis · MDE · power calc · pre-mortem
 │   └─ soldier-product-analytics  🔵  NSM input tree · WBR dashboard · HEART · DORA + flow
 │
 └─ Inspector  (3 checks: sources · ethics & dark patterns · quality)
```

🎖️ **elite** — `PK_ELITE_MODEL` (default `claude-opus-4-8` / `gpt-4.1`) — judgment-intensive  
🔵 **standard** — `PK_STANDARD_MODEL` (default `claude-sonnet-4-6` / `gpt-4o-mini`) — process-driven

---

## Mission loop

```
DISCOVER          O1 discovery & research
   └─ DC-1 ─────── optional direction check (non-blocking)
STRATEGISE+SHAPE  O2 strategy · O3 prioritisation · O4 design & validation
   └─ DC-2 ─────── optional direction check (non-blocking)
DELIVER           O5 delivery · O6 measurement & learning
   └─ INSPECT ──── Inspector FINAL (sources / ethics / quality) — veto power
```

Both direction checks are **non-blocking** (default: auto-proceed). This army produces strategy and design artefacts — no budget is spent, no code is pushed — so there is no mandatory human gate. Cap at `MAX_ITERS = 3`; if still failing, delivers best result with `residual_risk` stated.

---

## Installation

```bash
pip install openai-agents
pip install -e .
```

Optional search backends:

```bash
pip install -e ".[gemini]"   # Google Gemini search
pip install -e ".[tavily]"   # Tavily search
pip install -e ".[ddg]"      # DuckDuckGo (free, no key)
```

---

## Configuration

| Variable | Default (Claude) | Default (OpenAI) | Description |
|---|---|---|---|
| `PK_ELITE_MODEL` | `claude-opus-4-8` | `gpt-4.1` | Model for 🎖️ elite soldiers |
| `PK_STANDARD_MODEL` | `claude-sonnet-4-6` | `gpt-4o-mini` | Model for 🔵 standard soldiers |
| `PK_SEARCH` | `ddg` | `openai` | Search backend (`ddg` / `tavily` / `gemini` / `openai`) |
| `OPENAI_API_KEY` | — | required | OpenAI key (or set via LiteLLM for Claude) |

For Claude via LiteLLM:

```bash
pip install -e ".[litellm]"
export PK_ELITE_MODEL="claude-opus-4-8"
export PK_STANDARD_MODEL="claude-sonnet-4-6"
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

## Usage

### CLI

```bash
# Initialise a project (scaffolds .product/ + slash commands for your harness)
product init

# Run a headless mission
product run "We need to figure out why activation dropped 20% and what to do about it"

# Run with interactive direction checks
product run --steer1 --steer2 "Launch a new B2B pricing tier"

# Health check
product check
```

### Python

```python
from product_kit.mission import run_mission

dossier = run_mission("Reduce churn in our SMB segment")
print(dossier["delivered"])
```

With interactive direction checks:

```python
from product_kit.mission import run_mission, console_direction_check

dossier = run_mission(
    "Define the North Star for our marketplace",
    dc1_fn=console_direction_check,   # pause after discover
    dc2_fn=console_direction_check,   # pause after strategy+shape
)
```

### Direct agent access

```python
from agents import Runner
from product_kit.soldiers.soldier_jtbd import jtbd_soldier

result = Runner.run_sync(jtbd_soldier, "Our users are switching away from Notion to build their own tools...")
print(result.final_output)
```

---

## Repository layout

```
product_kit/
├── soldiers/        # 30 × soldier_<slug>.py
├── officers/        # 6 × officer_N_<name>.py
├── commander.py
├── inspector.py
├── mission.py       # 3-stage runner
├── models.py        # PK_ELITE_MODEL / PK_STANDARD_MODEL
└── web.py           # PK_SEARCH / web_tools()

product_cli/
├── cli.py           # `product` entry point
├── scaffolder.py
├── integrations.py
└── runner_bridge.py

agents/              # 30 soldier + 6 officer + commander + inspector .md
skills/              # 30 × SKILL.md (method reference cards)
docs/
├── RESEARCH.md      # benchmark findings (90+ orgs · 10 domains)
└── BENCHMARK_ENRICHMENT.md
.product/memory/
└── constitution.md  # 12 articles governing every product.* command
tests/               # 13 offline tests (SDK stub · no API key needed)
```

---

## Constitution (`.product/memory/constitution.md`)

12 articles that govern every `product.*` command:

- **Art. I** — No invented information; never cite "50% features never used", NPS as sole growth driver, Ellis 40% PMF as universal law, story-point benchmarks as productivity signal
- **Art. II** — Ethics & compliance: flag GDPR/CCPA/COPPA/HIPAA; refuse dark patterns (roach motel, confirmshaming, forced continuity)
- **Art. V** — Elite vs standard grades by depth of reasoning required, never by method fame
- **Art. VIII** — No mandatory HITL; two non-blocking direction checks
- **Art. IX** — Inspector: 3 checks, veto power, 7 product-specific quality failure modes
- **Art. XI** — Outcome-driven doctrine: outcomes over outputs, dual-track, problem before solution
- **Art. XII** — 7 tensions encoded as features, never resolved dogmatically

---

## Tests

```bash
pip install pytest
pytest
# 13 passed — offline, no API key, no network
```

---

## Part of the AI Agency

| Department | Repo | Focus |
|---|---|---|
| Product | **this repo** | Discovery · strategy · prioritisation · design · delivery · measurement |
| Solve | `solve-kit` | Problem-solving · root-cause · decision intelligence |
| Marketing | `marketing-kit` | Research · positioning · content · campaigns · analytics |
