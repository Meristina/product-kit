---
name: market-sizing
description: >-
  Estimates total addressable, serviceable addressable, and serviceable obtainable
  market (TAM/SAM/SOM) after a mandatory Porter Five Forces structural attractiveness
  gate. Produces a sized, verdict-bearing market assessment and a GTM-adjusted revenue
  potential range. Use it whenever a team needs to decide whether a market is worth
  entering before committing resources to product discovery or strategy.
---

# Skill — Market Sizing with Porter Five Forces Structural Gate

Market sizing is the quantitative estimation of how large an opportunity is across three
levels: TAM (total market if 100% share), SAM (the slice reachable with the current
business model), and SOM (the realistic near-term capture). Used alone, TAM/SAM/SOM
produces a number without a verdict. Michael Porter's Five Forces framework (Competitive
Strategy, 1980) provides the prerequisite structural test: a market can simultaneously
be large in addressable volume and unattractive to enter due to high competitive rivalry,
strong buyer bargaining power, low switching costs, or constant threat of substitution.
McKinsey and BCG apply Five Forces in Phase 1 Discovery specifically to answer the
strategic gate question — "is it worth playing in this market?" — before any volume
estimation begins. Only a market that clears the structural attractiveness gate earns
the full sizing treatment.

> **Doctrine:** Porter's Five Forces (1980) precedes sizing — never the reverse. The BASES
> volumetric calibration methodology (NielsenIQ) is the CPG industry standard for adjusting
> raw purchase intent via factors derived from 300,000+ concept tests; use it for consumer
> product contexts and cite it explicitly. GTM motion (PLG vs. SLG) materially changes
> effective market size and margin structure; model both when the choice is open. Never
> invent a benchmark, growth rate, or market share figure — research every external fact
> and cite a real source. Unknown → say "unknown".

## Procedure

1. **Frame the market and context.** Define the product, target segment, and geography before
   any numbers are touched. Identify whether the context is B2B or B2C, which sector, and
   what stage (pre-launch, early traction, scaling). This framing determines which sizing
   method is appropriate (top-down vs. bottom-up) and which GTM motion is plausible.
   Document assumptions explicitly; any figure without a traceable source must be tagged
   [assumption — verify].

2. **Run the Porter Five Forces gate.** Assess all five forces for the target market before
   sizing: (1) competitive rivalry — number of players, market concentration, growth rate;
   (2) buyer bargaining power — switching costs, buyer concentration, price sensitivity;
   (3) supplier bargaining power — dependency, switching costs upstream; (4) threat of new
   entrants — capital requirements, regulatory barriers, network effect moats; (5) threat
   of substitutes — functional alternatives and their pricing. Score each force Low / Medium
   / High. Produce a structural attractiveness verdict: Attractive / Borderline / Unattractive.
   A market scored Unattractive on 3+ forces warrants explicit escalation before sizing
   continues — sizing an unattractive market produces a number without a strategy.

3. **Estimate TAM using a dual method.** Run both top-down (industry report anchor) and
   bottom-up (unit × price × addressable population) estimates. If they diverge by more
   than 30%, surface the discrepancy and explain which assumption drives it. Cite the
   source for every external market figure. Never blend a sourced number with an invented
   multiplier without labelling the invented component [assumption — verify].

4. **Derive SAM from business model constraints.** SAM narrows TAM by the segments the
   current distribution model, pricing tier, and geographic footprint can actually reach.
   A $50B TAM in enterprise software may yield a $2B SAM for a self-serve PLG product
   priced under $100/seat. Be explicit about the filtering logic.

5. **Project SOM with GTM-adjusted assumptions.** SOM is the realistic 1–3 year capture
   given go-to-market motion, competitive position, and CAC economics. Apply GTM adjustment
   factors: PLG companies achieve 50% more revenue growth than sales-led counterparts, with
   CAC of $100–$500 versus $5,000–$50,000 for enterprise SLG (OpenView Partners benchmarks;
   Reforge). If the product targets CPG or consumer packaged goods, apply BASES volumetric
   methodology: adjust raw purchase intent using calibration factors derived from
   NielsenIQ's database of 300,000+ concept tests and 500,000+ forecasts; decompose
   adjusted volume into trial rate and repeat purchase rate. Post-IHUT (in-home use test)
   intent is materially stronger than pre-concept intent — sequence testing accordingly.
   Note: 76% of CPG launches fail annually (BCG analysis), contextualising why calibrated
   forecasting is required over raw intent scores.

6. **Apply the structural attractiveness verdict to the sizing output.** A large TAM in an
   Unattractive market is a warning, not a green light. Annotate the SOM estimate with the
   Five Forces score. If rivalry is high, apply a discount to the capture rate. If buyer
   power is high, flag margin compression risk. The sizing output must carry a strategic
   verdict, not just a number.

7. **Produce the SO-WHAT and next steps.** Translate the sizing into a decision: enter,
   stage entry with further validation, or do not enter. Name the next assumption that must
   be validated before committing resources. Identify which soldiers or phases should
   receive this output (e.g., soldier-competitive-forces for deeper Five Forces work,
   soldier-assumption-testing for validating trial rate hypotheses, O2 strategy officers
   for product vision and roadmap work).

## Output format

```
MARKET SIZING — <product / context>
Context detected: <B2B/B2C · sector · stage>

PORTER FIVE FORCES GATE
  Competitive rivalry:       [Low / Medium / High] — <1-sentence rationale>
  Buyer bargaining power:    [Low / Medium / High] — <1-sentence rationale>
  Supplier bargaining power: [Low / Medium / High] — <1-sentence rationale>
  Threat of new entrants:    [Low / Medium / High] — <1-sentence rationale>
  Threat of substitutes:     [Low / Medium / High] — <1-sentence rationale>
  Structural verdict:        [Attractive / Borderline / Unattractive]

TAM / SAM / SOM
  TAM (top-down):   $X [source]
  TAM (bottom-up):  $X [method + source]
  TAM discrepancy:  [% gap and key driving assumption]
  SAM:              $X — filtered by [distribution / pricing / geography constraints]
  SOM (Y1–Y3):      $X — GTM motion: [PLG / SLG / hybrid]; CAC assumption: $X [source]

GTM ADJUSTMENT
  Motion:           [PLG / SLG / hybrid]
  CAC benchmark:    [PLG $100–$500 / SLG $5K–$50K — OpenView Partners]
  Revenue growth:   [PLG +50% vs SLG — OpenView Partners, if applicable]
  CPG calibration:  [BASES trial rate / repeat rate, if applicable — NielsenIQ]

STRUCTURAL × SIZING VERDICT
  Market attractiveness: [Attractive / Borderline / Unattractive]
  Sizing confidence:     [High / Medium / Low]
  Strategic verdict:     [Enter / Stage entry / Do not enter — 1-2 sentences]

SO-WHAT / NEXT STEPS
  - [Decision or action #1]
  - [Next assumption to validate + cheapest test]
  - [Handoff: which soldier or officer receives this output]

SOURCES (every external fact cited; nothing invented)
  - Michael Porter — Competitive Strategy, Free Press, 1980
  - NielsenIQ BASES — Volumetric Forecasting Methodology, 300,000+ concept tests, 500,000+ forecasts
  - OpenView Partners — PLG vs. SLG CAC benchmarks (Blake Bartlett); Reforge PLG growth benchmarks
  - BCG — CPG launch failure rate analysis (76% annual failure rate)
  - [Additional sources as applicable — Author, Title, Year — URL or [assumption — verify]]
```
