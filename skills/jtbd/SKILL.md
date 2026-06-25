---
name: jtbd
description: >-
  Runs a structured Jobs-to-be-Done discovery session combining Bob Moesta's
  four-forces timeline interview (The ReWired Group) with Tony Ulwick's
  Outcome-Driven Innovation scoring (Strategyn). Use when you need to
  understand the causal mechanism behind a customer switch, which outcomes
  are underserved or overserved, and how to frame the job for positioning,
  roadmap prioritization, and OST input. Produces a job statement, forces
  diagram, and scored ODI outcome map.
---

# Skill — Jobs-to-be-Done (JTBD)

Jobs-to-be-Done is a causal theory of demand: customers do not buy products,
they "hire" them to make progress in a specific struggling moment
(Christensen, Hall, Dillon & Duncan, HBR 2016). The framework has two
complementary operational branches: Bob Moesta's timeline interview protocol
(The ReWired Group) surfaces the exact context, emotions, and forces at the
moment of switch; Tony Ulwick's Outcome-Driven Innovation (Strategyn)
translates that raw struggling moment into precisely formulated outcome
statements that can be scored for opportunity. Together they form Stage 1 of
the mandatory JTBD→ODI→OST pipeline — a non-substitutable sequential pipeline
where each stage feeds the next. Additionally, Ryan Singer (Shape Up,
Basecamp/37signals, 2019) establishes that if a team cannot articulate the job
served by a feature, it cannot define the boundaries of its scope, making JTBD
at the feature level a structural prevention mechanism for scope creep.

> **Doctrine:** Every output must cite the source of each framework claim
> (Moesta, Ulwick, Christensen — year and publication). Never invent an
> opportunity score, benchmark, or quote. The forces diagram must be completed
> before any solution or design work begins. Do not cite "50% of features never
> used" — origin is untraceable and figure varies across versions without a
> peer-reviewed source. NPS is a guardrail metric only, never a discovery
> instrument. Unknown data → say "unknown [assumption — verify]".

## Procedure

1. **Frame the struggling moment.** Identify the specific life or work
   situation in which the customer felt "stuck" enough to seek change. This is
   the unit of analysis — not a persona, not a segment, not a use case. Probe
   for the triggering event or accumulated dissatisfaction that made the
   existing approach no longer sufficient. No interview guide, no ODI survey,
   and no design work begins before this frame is explicit.

2. **Recruit for the switch, not the profile.** Select participants who
   recently completed a hire-or-fire decision: adopted a new product, abandoned
   an old one, or started doing something in a meaningfully different way.
   Behavioral screening (did the switch happen?) is primary; demographic
   screening is secondary (Moesta, The ReWired Group, Demand-Side Sales 101,
   2020).

3. **Conduct the timeline interview.** Run a chronological reconstruction of
   the customer's change journey — from first thought ("something needs to
   change") through passive looking, active looking, the moment of decision,
   first use, and ongoing use or abandonment. Use open-ended temporal probes:
   "Walk me back to the moment you first realized something had to change" and
   "What happened next?" Lead with the customer's story, never with the
   product. Capture the exact words customers use to describe dissatisfaction
   and aspiration — these become the raw material for outcome statements
   (Moesta, The ReWired Group).

4. **Map the four forces.** After each interview, place every finding into the
   forces diagram before proceeding to analysis. Push (+): dissatisfaction
   pulling the customer away from the current situation. Pull (+): attraction
   toward the new solution. Anxiety (−): fear of switching — cost, learning
   curve, social risk, uncertainty. Habit (−): inertia of the existing
   behavior, workarounds, and social routine. A switch occurs only when
   Push + Pull exceeds Anxiety + Habit. If anxiety dominates, address it before
   any positioning or onboarding design begins. This diagram is a gate, not a
   decoration (Moesta, The ReWired Group).

5. **Formulate the job statement.** Synthesize the timeline and forces into one
   job statement using the structure: [verb] + [object of the verb] +
   [context / clarifier]. Example: "Help me demonstrate business impact to my
   executive sponsor before the quarterly review." The job statement must
   describe the progress the customer is trying to make, not the product
   feature and not the solution. An implicit commercial application: Apple
   hardware decisions framed as job statements ("1,000 songs in your pocket")
   demonstrate that the format is a decision instrument, not just a research
   artifact (Adam Lashinsky, Inside Apple, 2012).

6. **Elicit ODI outcome statements.** For each functional step of the job,
   collect outcome statements in Ulwick's ODI syntax: direction + metric +
   object + context. Example: "Minimize the time needed to identify accounts
   at risk of churn during a weekly pipeline review." Target 20–50 outcome
   statements per job; 50–150 for a full ODI engagement (Ulwick, Strategyn,
   Jobs to Be Done: Theory to Practice, 2016).

7. **Score outcomes with the opportunity formula.** For each outcome, collect
   importance (1–10) and satisfaction (1–10) ratings from a representative
   sample — minimum 30 respondents for directional reads, 100+ before
   investment decisions. Opportunity score = importance + max(importance −
   satisfaction, 0). Score > 10: outcome is underserved — candidate for
   product investment. Score < 5: outcome is overserved — deprioritize or
   reduce scope. Scores between 5 and 10 are adequately served — monitor, do
   not invest heavily (Ulwick, Strategyn).

8. **Connect forces to downstream officers and hand off.** Push and pull are
   amplifiable via positioning work (O4) and onboarding activation sequences
   (O5). Anxiety and habit are reducible via social proof, frictionless
   activation design, and explicit change management. Hand the job statement
   and scored opportunity table to soldier-opportunity-solution-tree (O3/OST)
   as the structured input for Stage 2 of the pipeline. If a team cannot
   articulate the job served by a feature at this handoff, the feature's scope
   boundaries cannot be defined — escalate before proceeding (Ryan Singer,
   Shape Up, 2019).

## Output format

```
JOBS-TO-BE-DONE — <product / context>
Context detected: <B2B/B2C · sector · stage>

JOB STATEMENT
  Job:              [verb + object + context]
  Struggling moment:[trigger event or accumulated dissatisfaction]
  Unit of analysis: [hire-or-fire decision — not a persona or segment]

FOUR FORCES DIAGRAM
  Push     (+): [dissatisfaction with current situation — exact customer words]
  Pull     (+): [attraction toward new solution — exact customer words]
  Anxiety  (−): [fears, switching cost, learning curve, social risk]
  Habit    (−): [inertia, existing workarounds, social routine]
  Net force: Push + Pull [>/<] Anxiety + Habit
  Assessment: [switch likely / blocked by anxiety / blocked by habit]

ODI OUTCOME STATEMENTS — UNDERSERVED (score > 10)
  1. [direction + metric + object + context] | Imp: X | Sat: Y | Opp: Z
  2. ...

ODI OUTCOME STATEMENTS — OVERSERVED (score < 5)
  1. [direction + metric + object + context] | Imp: X | Sat: Y | Opp: Z

DOWNSTREAM CONNECTIONS
  → Push/Pull amplification : positioning (O4), onboarding sequences (O5)
  → Anxiety/Habit reduction : social proof (O4), activation design (O5)
  → Pipeline handoff        : job statement + opportunity scores →
                              soldier-opportunity-solution-tree (O3/OST)

SO-WHAT / NEXT STEPS
  - [Highest-opportunity underserved outcome and recommended investment focus]
  - [Overserved areas to deprioritize or descope immediately]
  - [Forces imbalance warning: if anxiety > pull, address before GTM or onboarding]
  - [Next mandatory pipeline stage: ODI outcome scores → OST desired outcome]

SOURCES (every external fact cited; nothing invented)
  - Christensen, Hall, Dillon & Duncan — "Know Your Customers' 'Jobs to Be
    Done'", Harvard Business Review, Sept–Oct 2016
  - Bob Moesta — The ReWired Group; Demand-Side Sales 101 (2020); four forces
    diagram and timeline interview protocol
  - Tony Ulwick / Strategyn — Jobs to Be Done: Theory to Practice (2016);
    ODI outcome statement syntax; opportunity score formula and thresholds
  - Ryan Singer — Shape Up, Basecamp/37signals (2019) — JTBD at the feature
    level as structural scope-creep prevention
  - Adam Lashinsky — Inside Apple (2012) — implicit Apple job-statement pattern
```
