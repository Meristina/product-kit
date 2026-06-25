# product-kit — Claude Code context

Department 3 of the AI Agency. Runs full-stack product management missions: discover →
strategise+shape → deliver, with an Inspector quality gate at the end. 30 soldiers across
6 officers, a commander, and a 3-stage mission runner with 2 optional direction checks.

## Key files

| File | Role |
|---|---|
| `product_kit/commander.py` | `commander_product` + 6 officer agents (ELITE/STANDARD) |
| `product_kit/inspector.py` | `inspector` — GATE + FINAL modes, 3 checks |
| `product_kit/mission.py` | `run_mission()` — 3-stage loop + 2 direction checks |
| `product_kit/models.py` | `ELITE` / `STANDARD` via `PK_ELITE_MODEL` / `PK_STANDARD_MODEL` |
| `product_kit/web.py` | `web_tools()` — search backend, selected by `PK_SEARCH` |
| `product_kit/soldiers/` | 30 soldier agents (one file per framework) |
| `product_kit/officers/` | 6 officer Python modules wiring soldiers into squads |
| `product_cli/cli.py` | `product init / run / check` entry point |
| `agents/` | Prose doctrine for commander, inspector, officers, soldiers |
| `.product/memory/constitution.md` | Immutable rules for every `product.*` command |
| `docs/RESEARCH.md` | Benchmark research methodology + strategic verdict |
| `docs/BENCHMARK_ENRICHMENT.md` | Raw findings from 90-org benchmark sweep |

## Officer → Soldier mapping

| Officer | Squad (soldiers) |
|---|---|
| O1 Discovery | jtbd 🎖️, opportunity_solution_tree 🎖️, user_interview 🔵, kano 🔵, market_sizing 🔵 |
| O2 Strategy | product_vision 🎖️, north_star 🎖️, okr 🔵, product_market_fit 🎖️, outcome_roadmap 🎖️ |
| O3 Prioritisation | rice 🔵, opportunity_scoring 🎖️, gist 🎖️, impact_effort 🔵, tech_debt_balance 🔵 |
| O4 Design | four_risks 🎖️, shape_up 🎖️, design_sprint 🎖️, assumption_testing 🎖️, usability_testing 🔵, prototyping 🔵 |
| O5 Delivery | story_mapping 🎖️, feature_flags 🔵, launch_readiness 🔵, dora_metrics 🔵, beta_program 🔵 |
| O6 Measurement | north_star 🎖️ (shared), aarrr 🔵, cohort_analysis 🎖️, controlled_experiment 🎖️, product_analytics 🔵 |

🎖️ = `PK_ELITE_MODEL`  🔵 = `PK_STANDARD_MODEL`

## Run tests

```bash
pip install -e ".[dev]"
pytest tests/ -v          # 17 tests, offline (SDK stubbed in conftest.py)
```

## Run a mission

```bash
product init              # scaffold .product/memory/constitution.md
product run "goal here"   # headless mission
product run --steer "goal" # with interactive direction checks
product check             # verify installation
```

## Environment variables

```bash
PK_ELITE_MODEL=gpt-5.5         # commander, elite soldiers
PK_STANDARD_MODEL=gpt-5.4-mini # standard soldiers
PK_SEARCH=ddg                  # search backend: ddg | tavily | gemini | openai
OPENAI_API_KEY=...
```

## Mission architecture

One commander call per iteration handles all 3 stages via `mission_brief()`.
DC-1 (post-discover) STEER → increments outer iteration.
DC-2 (post-strategy+shape) STEER → inner loop, no outer increment.
Inspector VETO/PASS_WITH_FIXES → outer loop with required fixes. Cap: MAX_ITERS=3.

## Naming invariants

- Soldier files: `soldier_<slug>.py` → `<slug>_soldier = Agent(name="soldier_<slug>")`
- Officer modules: `officer_N_<name>.py` → `officer_<name> = Agent(name="officer_<name>")`
- Commander: `commander_product = Agent(name="commander_product")`
- Inspector: `inspector = Agent(name="inspector")`
