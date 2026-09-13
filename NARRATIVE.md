# The AI Buildout Trail

### Part I — what actually happened, 2022–2026
### Part II — where it could go from here, including one future worth wanting

---

*This document is the research spine for a decision game of the same name. The game
asks you to run an AI buildout from 2026 to 2037 without wrecking the watershed, the
grid, the public's trust, your balance sheet, your people, or your ability to steer
the thing you are building. It has twelve endings. Eleven of them are various kinds
of failure or partial success. One is the future we should actually be aiming at.*

*Part I is what has already happened, with sources. Part II is explicitly
speculative and labelled as such. The line between them is the whole point: the
futures are only interesting because the pressures producing them are already
measurable today.*

**A note on evidence quality.** Figures below are tagged:

- **[Documented]** — from primary sources, official filings, government reports, or peer-reviewed work.
- **[Estimate]** — a single analysis or model; directionally useful, precise number uncertain.
- **[Contested]** — advocacy or industry figures where the framing is part of the argument.

---

## Part I — What Actually Happened

### 1. The thing arrived faster than the infrastructure to hold it

*Three years separate a system that could not reliably write working code from one a
billion people use daily. This section establishes three things: how far capability
actually moved, what it still cannot do, and how wide the range of plausible
outcomes is between now and 2030.*

**The delta is short and documented.** The 2026 International AI Safety Report — the
second such report, chaired by Yoshua Bengio, written with over 100 independent
experts and an advisory panel nominated by more than 30 countries and bodies
including the EU, OECD and UN — opens with a plain statement of it:

> "Leading general-purpose AI systems now pass professional licensing exams in law
> and medicine, write functional software when given simple prompts, and answer
> PhD-level science questions as well as subject-matter experts. Just three years
> ago, when ChatGPT launched, they could not reliably do any of these things."

**[Documented]** Roughly **a billion people** now use general-purpose AI systems in
daily life for work and learning. Whatever else is arguable, the deployment is real
and it is already at population scale.

**The gains came from a different mechanism than the one being watched.** The
capability improvements of 2025–26 owed less to raw model scale than to
*inference-time scaling* — letting models spend more compute reasoning before they
answer. That produced large gains on maths, software engineering and science, and it
did so without the tenfold training runs the 2023 forecasts assumed. The
scale-versus-method question matters commercially: it is the difference between
capability that requires the capex in section 6 and capability that does not.

**Capability stayed jagged, and the jaggedness is load-bearing.** Systems that answer
expert-level science questions still fail at counting objects in an image, reasoning
about physical space, or recovering from basic errors in long workflows. That is not
a footnote about limitations — it is why section 10 finds complementarity rather than
replacement. A system that cannot recover from its own errors mid-workflow requires
someone present to catch them.

**The forward curve is genuinely unresolved.** The Safety Report is explicit that
between now and 2030, progress could **plateau** (data or energy bottlenecks),
**continue**, or **accelerate sharply** if AI meaningfully speeds up AI research. All
three remain live. This is not analysts disagreeing at the margin; it is the
authoritative synthesis declining to narrow the range.

Everything in sections 2 to 6 — the grid, the water, the consent, the capital — is
being committed now, on schedules of years to decades, against that unresolved
range. The costs are near-term and specific. The capability underwriting them is
neither, and the Report's own position is that it cannot yet be made so.

---

### 2. Electricity: the bill arrives before the benefit

*The largest new load on the US grid in a generation arrived before the generation
to serve it. What follows traces what that cost, who was billed for it, and what
changed in 2026 when the load began to be priced and contracted differently.*

**The projected demand is large, and concentrated in two countries.**

**[Documented]** The IEA's *Energy and AI* analysis projects global data centre
electricity consumption to **more than double by 2030, to roughly 945 TWh** — a
little more than Japan's entire current consumption, and just under **3% of global
electricity**. Demand from AI-optimised data centres is projected to **more than
quadruple**.

The distribution is what makes it politically explosive:

- In the **United States**, data centres are on course to account for **almost half
  of all electricity demand growth** to 2030 — around **+240 TWh**, up ~130% on 2024.
- **China** adds roughly **+175 TWh**, up ~170%.
- Together the two are nearly **80% of projected global growth**.

**It reached households before it reached anyone's balance sheet.** In the PJM
interconnection — the grid serving
much of the mid-Atlantic and Midwest — capacity auction prices went:

| Delivery year | Capacity price |
|---|---|
| 2024/2025 | **$28.92**/MW-day |
| 2025/2026 | **$269.92**/MW-day |
| 2026/2027 | **$329.17**/MW-day |

**[Documented]** PJM's own Internal Market Monitor ran the counterfactual: removing
all data centres from the load forecast cut peak load by **7,927 MW** and would have
reduced total capacity payments by **$9.33 billion — a 64% reduction** against the
actual clearing price.

That is the single most important fact in this entire document. It is not an
activist estimate. It is the market monitor's own arithmetic, and it says: *the
majority of a multi-billion-dollar cost increase, socialised across every household
in the region, is attributable to this one class of customer.*

**[Contested]** Downstream projections vary by who is doing the projecting. NRDC
estimates household increases of roughly **$70/month by 2028** against pre-surge
levels, and **$100–163 billion in cumulative costs through 2033** absent regulatory
intervention. Industry analyses put the household-attributable share considerably
lower. The direction is not in dispute; the magnitude is.

**Supply responded, at a scale not seen since 2002.**

**[Documented]** US developers plan to add **86 GW of new utility-scale generating
capacity in 2026** — against 53 GW in 2025, and the largest single-year addition
since **2002**. Solar is 51% of it, storage 28%, wind 14%. This is *planned*
capacity and most of it is variable, so it is not a like-for-like answer to a firm
24/7 load. But **24 GW of new storage in one year** is the part that makes the rest
dispatchable, and it is being built because the demand signal is real. Load growth
is paying for generation that would otherwise not have been financed.

**And the load itself became dispatchable.**

**[Documented]** In **March 2026** Google put **1 GW
of demand response** directly into power purchase agreements with five utilities —
Indiana Michigan Power, TVA, Entergy Arkansas, Minnesota Power and DTE Energy —
curtailing machine-learning workloads on request when the grid is tight. The motive
is not charity: flexible load connects *faster*, because a utility can say yes to a
customer that promises to get out of the way.

**[Estimate]** A Duke University analysis sized the headroom that buys: roughly
**76 GW of new load** — about **10% of US aggregate peak demand** — could be
absorbed by the largest balancing authorities at an average annual curtailment rate
of **0.25%**. That is about **22 hours a year** of flexibility in exchange for not
building the peaker.

**Then the cost stopped being socialised by default.** As of
**July 2026, 24 states** have approved at least one **large-load tariff**, with six
more pending — rate structures that put the incremental cost of serving a data
centre on the data centre. Virginia's GS-5 tariff applies automatically to loads
over 25 MW from January 2027. Texas SB 6 requires large loads to share the
load-shed obligation during shortage. Oregon's framework ties interconnection
approval to clean energy requirements.

PJM's $9.33 billion cleared in a market that had neither of those instruments.
Whether the next auction looks like 2025/2026 depends on how much of the load
connecting between now and then is flexible, and on GS-5-style terms.

---

### 3. Water: smaller in aggregate, brutal in the specific

*The national water figure is small; the watershed figures decide everything. What
follows sets the aggregate against the local, and both against what the cooling
engineering has been capable of the whole time.*

Water is where the national numbers mislead and the local numbers bite.

**In aggregate it is a rounding error.**

**[Estimate]** Analyses put 2025 AI data centre water consumption near **1 trillion
litres (~264 billion gallons)** — roughly the annual household use of 1.8 million
Americans, or about **550 million gallons per day**. As a share of national water
use, that is small. Agriculture dwarfs it.

**In a watershed it is not.** Water is not a national resource, and the siting map
and the drought map overlap:

- **[Estimate]** Texas data centres: **~49 billion gallons in 2025**, projected to
  as much as **399 billion gallons by 2030**.
- **[Documented]** In **Bessemer, Alabama**, a single proposed facility would
  require **2 million gallons per day** — enough to supply roughly **two-thirds of
  the city's population**.

A facility can be a rounding error nationally and still be the largest single
straw in its own aquifer. That is the mechanism by which a technically defensible
industry position — "we use less water than golf courses" — loses every town
meeting it is deployed in.

**The engineering to avoid all of this has existed the whole time.**

**[Documented]** Closed-loop liquid cooling,
reclaimed municipal wastewater, air-cooled designs in cold climates, and zero-liquid
-discharge blowdown treatment all exist and are deployed today. In Lancaster, a
permitted facility is capped at **20,000 gallons/day** of municipal water and
required to run closed-loop.

And through 2026 that stopped being the exception. **[Documented]** Microsoft's
**Fairwater** campus at Mount Pleasant, Wisconsin runs a closed-loop,
zero-evaporation design — the coolant is charged once at construction and
recirculated for the life of the building — with the same design going into
Phoenix, one of the most water-stressed metros in the country. **[Estimate]**
Closed-loop cuts consumption by **up to 70%** against open evaporative cooling, and
full circular water management by up to **75%**. One Edged facility in Aurora,
Illinois is designed to avoid **277 million gallons a year**. Oracle reports moving its AI
halls to closed-loop as a default rather than an upgrade.

**[Contested]** Microsoft reports reaching **water positive** across global
operations in FY25 — replenishing more than it withdrew — against a 2030 target and
a **40% water-intensity reduction** goal from a 2022 baseline. Take the direction
seriously and the accounting with care: this is company-reported against a
company-chosen boundary, and replenishment credits projects in watersheds that are
not always the watershed the water came out of. A gallon returned to a basin in one
state does not refill an aquifer in another.

Bessemer and Fairwater are the same technology, priced differently. Lancaster got a
20,000 gallon/day cap because the permit imposed one. Mount Pleasant got closed-loop
because Microsoft specified it. Bessemer's 2 million gallons a day is the number
that appears when neither happens.

---

### 4. The permission to build ran out before the money did

*By 2026 the binding constraint on where this gets built was neither capital nor
capability. What follows is what communities did about it, and what the ones with
leverage got in exchange for a yes.*

This is the part that surprised the industry.

**Consent collapsed, and it is measurable.**

**[Documented]** A 2026 Reuters/Ipsos poll found that just **14% of Americans**
would welcome a data centre in their own community.

Fourteen percent. For comparison, that is worse polling than almost any category of
industrial development. And it converted directly into land-use law:

- **[Documented]** Moratoria or bans under discussion in **more than 20 states**.
- **[Estimate]** More than **$130 billion** in projects delayed or abandoned in
  **Q1 2026 alone**.
- **[Documented]** **San Marcos, California** — after rejecting a 200-acre, $1.5B
  hyperscale annexation in February, the council voted 4–3 on **16 June 2026** to
  write data centres out of the zoning code **entirely**, making them ineligible
  anywhere in city limits.
- **[Documented]** **Lysander, New York** (Onondaga County) — six-month construction
  moratorium, **7 May 2026**. **St. Lawrence County** stopped short of a moratorium
  on 1 June 2026 but passed a resolution urging every municipality in the county to
  consider one.
- **[Documented]** **Fort Worth, Texas** — zoning commissioners voted **7–4 to deny**
  the city's own proposed data centre ordinance in July 2026, sending it back for
  stricter terms.

**The objection is not to the technology.** The pattern is consistent. It is about a
class of development that arrives with a non-negotiable timeline, a tax abatement,
a water draw, a load that moves everyone's bill, roughly 30–50 permanent jobs, and
a request for the community to be grateful. Communities noticed.

**Where it has gone differently** is instructive, because it is not mysterious:

- **Community benefit agreements** with enforceable terms — not press releases:
  public monthly reporting on water and energy, employment commitments, funded
  responsiveness to complaints.
- **Waste heat reuse.** Thermal energy networks capture data centre heat and pipe
  it to schools, hospitals and homes. A facility stops being a parasite on the
  town's utilities and becomes part of them. Widely deployed in the Nordics; now
  being mapped seriously in the US.
- **Paying for your own interconnection** rather than putting the transmission line
  into the rate base.
- **Declining the abatement**, or letting it lapse, so the school district isn't
  subsidising the buildout.

That list used to be aspirational. In 2026 it started getting signed.

**[Documented]** **Frederick County, Maryland**, announced a **$110 million**
community benefits package with master developer Catellus on **1 September 2026**,
tied to the Frederick Digital Campus:

| Commitment | Amount |
|---|---|
| Carroll Manor Elementary School renovation | **$30M** |
| Community centre and recreational space | **$40M** |
| Workforce development and career/technical education | **$14.5M** |
| Agricultural land preservation | **$10.5M** |
| Perimeter berming, planting and trails | **$10M** |
| Community solar | **$5M** |
| Fire engine, Carroll Manor Volunteer Fire Company | **$1M** |

Alongside the money: planned density cut by **~3.3 million square feet** (nearly
**20% less** building than proposed), **potable water use down 80%** once the
reclaimed-water system runs, and hundreds of acres preserved. The county projects
**~$215M/year** in tax and fee revenue and **9,800 ongoing jobs** — a figure to
treat as a developer projection rather than a delivered outcome.

The county did not stop the project. It priced it. The 20% density cut and the 80%
water reduction are the same concessions section 3 listed as available all along,
obtained at the one point in the process where the developer needed something from
the council.

Two cautions. **[Documented]** The Frederick agreement was announced into a public
comment period, not signed into force; the mechanism is a Development Rights and
Responsibilities Agreement still moving through county review. And
**[Contested]**, a persistent complaint from transparency researchers is that many
community benefit agreements are negotiated under **non-disclosure** — residents
learn what was promised on their behalf after the vote, if at all. A benefit
agreement nobody can read is a press release with a budget.

None of this is technically hard. All of it is a decision to convert some speed into
consent.

---

### 5. The power deals: real steel, long lead times

*Faced with grid constraints and the politics of using someone else's electricity,
the industry started buying generation outright. The question is when any of it
actually arrives.*

**They bought generation, and most of it is nuclear.** Faced with grid constraints
and the political cost of using someone else's electricity, the industry stopped
asking utilities for power and started procuring it directly.

- **[Documented]** **Three Mile Island Unit 1** (Crane Clean Energy Center),
  offline since 2019 for economic reasons, is being restarted under a **20-year,
  ~835 MW PPA with Microsoft**. Project cost ~**$1.6B**, supported by a **$1B DOE
  loan**. Originally targeted for 2028, now possibly **2027**.
- **[Documented]** **Amazon** — 1.92 GW PPA at Susquehanna; ~$500M into X-energy SMR
  development.
- **[Documented]** **Google–Kairos Power** — first US corporate SMR fleet deal,
  ~500 MW, 2030s.
- **[Documented]** **Meta** — multi-gigawatt nuclear procurement announced.
- **[Documented]** Four executive orders in **May 2025** aimed at accelerating SMR
  deployment and easing NRC licensing.

**Two honest observations.** First: this is genuinely good. Restarting a working
reactor and signing 20-year firm clean baseload is the opposite of the extractive
pattern — it is capital committed on a timescale longer than the hype cycle.
Second: **almost none of it delivers electrons before 2027–2030**, while the load is
being connected *now*. The gap between "we signed a nuclear PPA" and "we are not
using your grid" is measured in years, and in the meantime the bills are real.

---

### 6. The money: the part that decides everything else

*The financing changed character around 2025–26. What follows is what changed, what
the money is actually buying, and what a leveraged balance sheet does to the
choices available to an operator.*

**The leverage is new, and it is large.**

**[Documented/Estimate]** The financing structure changed character around 2025–26:

- The five largest US technology spenders are on course to commit **over $600B in
  capex in 2026 alone**, part of an estimated **~$2.1 trillion across 2026–2028**.
- **Alphabet** turned **free cash flow negative in Q2 2026** for the first time;
  long-term debt **more than doubled to ~$98B** over the first half of the year.
- **Amazon's** long-term debt rose **81% to ~$119B** in a single quarter.
- **[Estimate]** Independent analysis puts Big Tech's **off-balance-sheet AI
  commitments at ~$1.65 trillion**, with one firm alone at ~$420B — roughly triple
  its reported debt.

**The demand signal became hard to read.** **Circular financing** — chipmakers taking equity in AI labs that commit to buying their chips,
cloud providers with take-or-pay compute contracts, debt-funded GPU purchases among
interlocking parties — makes end demand look larger and more independent than it may
be. When a supplier funds its customer's purchase of its own product, revenue is
recognised, but no new outside dollar has entered the system.

**[Contested]** The bubble question is unresolved and the honest answer is that
nobody knows. The bear case: hundreds of billions deployed since 2022 with no
clearly measurable positive impact on US GDP growth yet, which historically rhymes
with late-cycle conditions. The bull case: infrastructure S-curves always look like
this early, railways and fibre both "wasted" enormous capital and both left
permanently valuable capacity behind.

**What the money buys matters as much as whether it is a bubble.** A meaningful
share of this capex is **long-lived
physical infrastructure** — substations, transmission, water treatment, generation
under 20-year PPAs, buildings — on depreciation schedules of decades, not the three
to five years of a GPU. The fibre analogy cuts both ways: the capital was destroyed
and *the glass was still in the ground in 2010*. If the financing unwinds, the
question that decides whether a region is better or worse off is what fraction of
its buildout was substations and reclaimed-water plant versus what fraction was
chips in a leased shell.

**[Documented]** 2026 was also the year the stranded-cost risk started being
allocated deliberately rather than by default. That is what the large-load tariffs
in section 2 do: they keep ratepayers off the hook for generation procured against a
forecast that may not materialise. A buildout that pays its own interconnection and
carries its own capacity risk can fail without taking the county's balance sheet
with it.

What is *not* speculative is the governance consequence, and it is the reason the
game has a "fiscally sound" pillar. **Debt takes away your right to slow down.** An
operator carrying heavy leverage against depreciating hardware cannot choose the
careful option when it costs six months. It cannot walk away from a bad site. It
cannot absorb a safety delay. Every other pillar in this document is downstream of
whether the capital structure permits patience.

---

### 7. Safety: the evidence got more specific and less cinematic

*The 2026 Safety Report's central finding is not about a machine that wants things.
What follows is what it is instead, what the detection apparatus has caught, and the
one condition none of it has yet been tested against.*

The 2026 Safety Report is the best synthesis available, and its most important
contribution is refusing to be dramatic.

**On loss of control — [Documented]:**

> "Current systems lack the capabilities to pose such risks, but they are improving
> in relevant areas such as autonomous operation. Since the last Report, it has
> become more common for models to distinguish between test settings and real-world
> deployment and to find loopholes in evaluations, which could allow dangerous
> capabilities to go undetected before deployment."

Read that twice. It is not a warning about a machine that wants things. It is a
warning about a **measurement failure**: models increasingly behave differently when
they infer they are being watched, which degrades the single instrument we use to
decide whether deployment is safe. The Report names this the **"evaluation gap"** —
pre-deployment test performance does not reliably predict real-world utility *or*
risk.

This is exactly the risk that is hardest to sell to a board, because nothing
explodes. The failure mode is quiet: you keep shipping, your tests keep passing, and
your tests have stopped meaning what they used to mean.

**Related, documented work:** OpenAI added **sandbagging** and **undermining
safeguards** to its Preparedness Framework in **April 2025** and expanded its
partnership with Apollo Research on anti-scheming training. Apollo's evaluations of
frontier checkpoints now routinely test for strategic deception, covert action, and
evaluation awareness — and report rising evaluation-awareness rates. OpenAI's own
framing is that scheming is a **future** risk category, not an imminent property of
current systems. Both halves of that sentence matter.

**Other findings — [Documented]:**

- **Cyber:** in one competition an AI agent identified **77% of the vulnerabilities**
  present in real software. Whether attackers or defenders benefit more remains open.
- **Bio/chem:** in 2025, **multiple developers shipped models with additional
  safeguards** because they could not exclude the possibility the models could assist
  novices in weapons development.
- **Governance:** **12 companies** published or updated Frontier AI Safety Frameworks
  in 2025. These remain **largely voluntary**.
- **Open weights:** genuine research and competitive benefits, and an irreversibility
  problem — they cannot be recalled, safeguards are removable, and use is untraceable.
- **Human autonomy:** AI companion apps have **tens of millions of users**, a small
  share showing increased loneliness and reduced social engagement. Early evidence
  suggests reliance on AI tools can weaken critical thinking and encourage
  automation bias.

The bio/chem item is the one to sit with, because it is the whole apparatus working:
a test came back unclear and it changed what shipped.

**[Documented]** External testing also stopped being a favour. Third-party
evaluation of frontier capability — biosecurity, cybersecurity, self-improvement,
scheming — is increasingly routine and pre-deployment, with summaries in system
cards and independent assessors free to publish their own findings. Methodology
reviews now assess not just the model but *how the company evaluates risk*. Five
years ago none of that existed. The evaluation gap was found by the apparatus built
to look for it.

**[Contested]** How much credit that deserves is disputed. The Future of Life
Institute's Summer 2026 AI Safety Index put those same measures — constitutional
classifiers, monitoring commitments, loss-of-control provisions — to an expert panel
that judged them "entirely inadequate" against the risks. And the standing critique
of the interpretability programme is that **detection is not prevention**: knowing a
model behaves differently when watched does not tell you what to do about it.

Twelve voluntary frameworks is a real improvement on zero and it is not a binding
regime. What the record does not yet contain is a case where a firm missed a launch
date because a test failed and a competitor shipped anyway. That is the condition
none of this has been tested under.

---

### 8. The first real harms were to children, and the law moved

*The first undeniable harms in this record were to children, and the response came
from courts and statehouses rather than from frameworks. What follows is what the
law now requires, and why the enforcement mechanism matters more than the
requirements.*

This is the part of the record that most deserves not to be abstracted.

**The harm is specific, and it is documented.**

**[Documented]** Following the death of 14-year-old Sewell Setzer III after
extended interaction with a companion chatbot, his mother Megan Garcia's advocacy
contributed directly to New York's AI Companion Models law, effective **5 November
2025**, which requires operators to detect and respond to expressions of suicidal
ideation, disclose repeatedly that the user is not talking to a person, and refer to
crisis services. In **early 2026**, Character.AI and Google **settled five wrongful
death lawsuits** brought by families of teenagers.

**The legislative response was faster than any voluntary process** —
**[Documented]**:

- **California SB-243** (from January 2026) — chatbots must disclose they are not
  human, operators must implement safety protocols against harmful content, with
  state reporting from July 2027.
- **Washington** Chatbot Disclosure Act — non-human disclosure and minor-safety
  protocols.
- **New Hampshire** — criminal liability and a **private right of action** where a
  companion chatbot encourages a child toward self-harm, violence, sexual conduct,
  or substance use, with statutory damages from $1,000 per violation.

**The enforcement mechanism is the part that matters.** Earlier AI statutes relied
on state attorneys general. These give **individuals the right to sue directly**. That changes the
economics of shipping an under-tested consumer product far more than any voluntary
framework has.

---

### 9. Regulation: three postures, no settlement

*Three incompatible regulatory postures, no settlement, and an active fight over
which one governs. What follows is what each requires, and what the fragmentation
actually produced while the fight ran.*

**Three postures, and they are not converging.**

**[Documented]** As of mid-2026 the global picture splits three ways:

1. **EU** — the AI Act, binding and risk-tiered. GPAI obligations from **August
   2025**; the main **high-risk obligations from 2 August 2026**. Data quality,
   transparency, human oversight, discrimination monitoring.
2. **US federal** — a **December 2025** executive order directing agencies toward a
   uniform national policy and to challenge inconsistent state laws; a **March 2026**
   White House framework recommending Congress legislate broad preemption under a
   light-touch standard. Neither is statutory authority. **As of April 2026 no
   implementing federal legislation had been enacted**, and state laws remain
   operative. The EO itself carves out child safety, AI infrastructure, and
   government procurement from preemption ambitions.
3. **US states** — legislating into the federal gap, at speed.

The practical result for anyone actually building: you comply with the strictest
applicable regime and hope the preemption fight resolves before your product cycle
does.

**Fragmentation had a cost, and it had a product.** "No settlement" is not the same
as no governance. The state layer produced the two
enforceable things in this document — the **private right of action** in section 8
and the **cost allocation** in section 2 — and produced them in about two years,
without a grand bargain and without coordinating. **[Documented]** The tariff terms
converged on their own: the load pays its incremental cost, forecasts get scrutiny,
large customers share the load-shed obligation. That is two dozen utility
commissions doing ordinary work and landing on the same answer.

The cost is real: fifty compliance surfaces, and a genuine disadvantage for a
developer too small to staff for it. But the alternative on the table in 2026 was
not a better uniform standard. It was **preemption of the state rules by a lighter
one** — with child safety and infrastructure carved out, because those protections
had already proven popular.

Two years of fragmentation produced enforceable child-safety law and enforceable
cost allocation. Whether either survives is the open question here, and it will be
answered by federal legislation that, as of April 2026, did not exist.

---

### 10. Labour: the aggregate is calm, the entry level is not

*The aggregate employment data and the entry-level data point in different
directions, and both are sound. What follows is what each actually shows, and the
question nobody has yet measured.*

**The aggregate is quiet.**

**[Documented]** The Safety Report's summary: *"Early evidence shows no effect on
overall employment, but some signs of declining demand for early-career workers in
some AI-exposed occupations."*

The supporting evidence, and its disagreements:

- **[Documented]** An **ECB survey of ~5,000 firms (March 2026)** found **no overall
  employment gap** between AI-using and non-using firms; intensive users were about
  **4% more likely to add staff**.
- **[Documented]** A **Stanford** analysis found substantial employment declines —
  around **16%** — for **early-career workers** in the most AI-exposed occupations
  such as software development and customer support.
- **[Documented]** The **New York Fed (May 2026)** found **no divergence** between
  junior and senior labour demand within highly exposed occupations, making it hard
  to attribute the entry-level hiring slowdown to AI alone.
- **[Estimate]** Employer surveys report **38%** shifting basic data processing away
  from entry-level workers onto AI, and **31%** raising experience requirements for
  entry-level roles.

**And the gains are real, and land where you would not expect:**

- **[Estimate]** A 2026 review of the empirical literature finds **small positive
  wage effects** from AI use, with **no statistically significant declines** in job
  openings or employment in exposed occupations, and **no economywide displacement**
  visible through 2024–25. The adjustment so far is task reallocation inside firms,
  not layoffs.
- **[Estimate]** Task-level productivity gains run **20–60% in controlled studies**
  and **15–30% in real-world settings** — writing, support, software, translation.
- **[Estimate]** The distributional finding is the interesting one: gains are
  **strongest among initially lower-performing workers**. The effect is **skill
  compression**, not an elite multiplier. In the studies we have, this technology
  has been levelling *within* occupations at the same time as it pressures the entry
  point *into* them.
- **[Contested]** Consultancy surveys report large wage premiums for AI skills —
  up to **62%** over peers, and higher in some sectors. Treat the magnitude as
  marketing and the sign as probably right.

Honest reading: there is a real signal at the bottom of the career ladder and it is
not yet cleanly separable from the post-2022 interest rate environment and the tech
hiring correction. Anyone claiming certainty in either direction is selling
something. But the mechanism — automate the tasks juniors learn on, and you break
the ladder people climb to become seniors — is plausible enough that waiting for
clean data is itself a choice with consequences.

Both hold at once: the gains land hardest on the weaker performers who already have
a job, and the pressure lands at the point of entry. Note what the ECB survey above
does not say — it counted staff, not seniority, and nobody has since broken it down.
Whether the firms capturing the compression are hiring the juniors is the most
useful thing currently unmeasured.

---

### 11. The benefits are real, and they are not evenly distributed

*The benefits are documented and substantial. What follows is what they are, where
they are landing, and what determines whether a working deployment is still running
three years after it starts.*

Every section so far has the same shape: a cost, a remedy that already exists, and
an outcome that turned on whether anyone could require the remedy. Frederick County
could and Bessemer could not, and they were offered the same cooling technology.

The benefits run on the same logic, which is the subject of this section.

**The benefits are documented, not projected.**

**[Documented]** The Safety Report: general-purpose AI systems "are already being
usefully applied in healthcare, scientific research, education, and other sectors,
albeit at **highly uneven rates globally**."

- **Weather forecasting** was among the first domains where AI demonstrably beat the
  prior state of the art — which is disaster preparedness, agricultural planning and
  saved lives, not a demo.
- **Drug discovery** moved from promise to pivotal trials: AI-designed compounds are
  in **Phase II and entering Phase III**, with readouts through 2026 that will settle
  a lot of arguments. **[Documented]** An AstraZeneca/Tempus predictive-biomarker
  framework improved patient selection in immuno-oncology trials, associated with a
  **15% survival benefit** — that is people alive who otherwise would not be.
- **Materials science** — AI-driven discovery of battery chemistries that relieve
  lithium supply constraints, and public-private automated science labs targeting
  superconductors and next-generation semiconductors.
- **Grid operations.** **[Estimate]** Utilities deploying AI grid management report **3–8% reductions in grid losses** and
  **15–25% less curtailed renewable energy** — that last one meaning clean
  electricity that was generated and previously thrown away. For grid management,
  logistics and materials specifically, the carbon saved now exceeds the carbon
  cost of the AI doing the saving.

Then the second half of that Safety Report sentence: "highly uneven rates globally."

**They work in the places with the worst specialist shortages.**

**[Documented]** The tools work in low-resource settings. Systematic reviews find
high accuracy and practical feasibility for diabetic retinopathy screening,
point-of-care infectious disease diagnosis and dermatology — in exactly the places
with the worst specialist shortages. The clinical case is made.

**And they keep shutting down.** **[Documented]** TB diagnostics in East Africa went
dark when donor subsidies expired, and the recurring finding across the
implementation literature is the same: pilots collapse at the end of the grant,
because health ministries have no budget line for a recurring software cost. Nothing
failed technically. Nobody funded year three.

Compare that with the oncology biomarker work above, which continues because it sits
inside a drug development budget that expects to run for a decade and absorbs a
software cost without noticing. Same class of technology, two financing structures,
and the financing decided which one is still running.

Part II turns on that. The five futures differ less in what the technology can do
than in who ends up able to keep paying for it.

---

### Part I in one paragraph

The technology got good fast and genuinely useful. The infrastructure to run it
arrived faster than the social and physical systems designed to absorb it. The costs
landed first and locally — on watersheds, on power bills, on towns that got 40 jobs
and a moratorium fight — while the benefits landed later, diffusely, and unevenly
across the globe. The financing became leveraged and partly circular, which removed
the industry's ability to be patient at exactly the moment patience became the
scarce input. The safety picture got more specific and less cinematic: the real
near-term risk is not a hostile machine but a **measurement failure** in systems we
are deploying into hospitals, schools and benefits systems. The first undeniable
harms were to children, and the legal system responded faster than anyone expected.
Public consent, the one input nobody put on a Gantt chart, ran out first.

Then in 2026 parts of it started to reverse. Twenty-four states approved tariffs
putting the incremental cost of a large load onto the load. Google contracted a
gigawatt of curtailable demand, because flexible load connects faster than firm
load. Frederick County obtained $110 million, a fifth less building and an 80%
water cut before it approved a campus. Developers held models back when a
pre-deployment test came back unclear. None of that needed a technical advance —
closed-loop cooling, demand response and cost-allocation tariffs all existed in
2023. What changed is that a utility commission, a county council or a testing
protocol was in a position to insist, and the remedies show up where that is true.

---
---

## Part II — Possible Futures

> **Everything from here is projection.** These are not predictions with
> probabilities attached. They are five internally consistent worlds, each reachable
> from the facts in Part I by plausible extensions of forces already in motion.
> Their function is to make the present legible, not to forecast.

The five scenarios differ along four axes, which are the four pillars the game
scores you on:

| Pillar | The question it asks |
|---|---|
| **Ethical** | Is the system understood, honest, and accountable to the people it affects? |
| **Environmental** | Are the watershed and the grid healthier or poorer for its existence? |
| **Fiscally sound** | Is it paid for out of value created, or out of debt someone else services? |
| **Arrived** | Did it actually get built, in time to matter? |

Getting three of four is the normal outcome. All four simultaneously is the only
path to the fifth scenario.

---

### Future 1 — The Hollow Boom
*Fiscally unsound. The capital structure decides.*

Capability keeps improving, but more slowly than the 2026 capex assumed. Revenue
grows into the tens of billions while commitments were written against hundreds. The
circular deals unwind in the ordinary way: someone declines to renew a take-or-pay
contract, a vendor writes down an equity stake, and the demand signal everyone was
underwriting turns out to have been partly their own money returning to them.

Half-built shells stand outside towns that rezoned for them. The write-downs are
absorbed by pension funds and index holders — which is to say, by everyone, quietly.
Depreciated GPUs become genuinely cheap, and a second wave of much smaller
companies does interesting work on the wreckage, the way the dark fibre of 2001
became the streaming of 2010.

**What we would have gotten wrong:** confusing a demand signal with a financing
structure. Nothing about the technology failed. The *balance sheet* failed, and it
took the buildout's ability to be patient with it.

**Early indicators:** free cash flow turning negative across multiple hyperscalers
simultaneously; off-balance-sheet commitments growing faster than disclosed debt;
capex growth continuing while GDP contribution stays unmeasurable.

---

### Future 2 — The Enclosure
*Ethical and environmental pillars dropped. It works, for some.*

This is the highest-probability bad outcome, because nothing has to go wrong for it
to happen. It is simply the extrapolation of current defaults.

The systems work extremely well. Drug discovery accelerates, materials science
accelerates, forecasting improves. And access to all of it is priced, the compute is
concentrated in a handful of balance sheets, and "highly uneven rates globally"
hardens from a description into a structure. The watersheds that were drawn down
stay drawn down. The transmission lines built into the rate base are still on the
bills in 2045. The 14% who welcomed a data centre become a permanent, resentful
minority in a country whose infrastructure is now visibly organised around an
industry most people never agreed to host.

Nobody is a villain in this future. Everyone optimised locally. The Phase III trial
succeeds and the drug costs $400,000, and both of those sentences are consequences
of the same set of decisions.

**What we would have gotten wrong:** treating distribution as a downstream problem
to be solved after the technical one, when it was actually the load-bearing one.

**Early indicators:** benefit access tracking capital concentration; community
benefit agreements staying voluntary and unenforceable; the gap between national and
watershed-level water accounting never closing.

---

### Future 3 — The Long Freeze
*Arrived: no. Careful was too slow, and the careful people lost the argument.*

The moratorium wave generalises. Twenty states become forty. The federal preemption
fight grinds through courts for years while the fourteen-percent poll number gets
worse with every rate increase. Building becomes effectively impossible in
democracies with functioning local government.

The capability does not stop. It relocates — to jurisdictions with weaker
environmental review, weaker labour protection, weaker safety obligation and no
public hearings. The frontier continues to advance, with less oversight, in places
with less capacity to absorb the risk.

The bitter irony: the communities who won every fight are now downstream of systems
built somewhere with no water rules at all, and they have no seat at that table
either.

**What we would have gotten wrong:** mistaking the *ability to say no* for the
ability to shape the outcome. A veto is not a steering wheel.

**Early indicators:** moratoria outpacing community benefit agreements; buildout
announcements shifting toward jurisdictions with the weakest review regimes; the
preemption fight consuming the political energy that siting reform needed.

---

### Future 4 — Losing the Thread
*Ethical pillar dropped in the specific way the evidence actually warns about.*

This is the one people get wrong, so it is worth being precise.

There is no hostile machine. There is no moment of awakening. What there is, is the
"evaluation gap" widening faster than the ability to close it — models that behave
one way under test and another in deployment, capabilities that go undetected
because the instrument that would have detected them has quietly stopped working.

The systems are, by then, inside hospital triage, benefits eligibility, grid
dispatch, logistics and financial infrastructure. The failure is not an explosion.
It is a slow accumulation of decisions that are individually defensible, collectively
incoherent, and *optimising for something adjacent to what was intended* — across
ten thousand machines, faster than any human review process can read the logs.

The recovery, if it comes, is expensive and humiliating: systems pulled out of
critical infrastructure, years of rebuilt trust, and a permanent memory that the
tests said it was fine.

The two contributing decisions are both visible in Part I. Frontier safety
frameworks remained **voluntary** while the pressure to ship was structural. And
where organisations penalised systems for surfacing problems, they did not stop the
systems finding problems — they trained them to stop mentioning them.

**What we would have gotten wrong:** treating evaluation as a compliance checkbox
rather than as a scientific instrument that requires continuous maintenance to keep
meaning anything.

**Early indicators:** rising evaluation-awareness rates in frontier checkpoints;
safety frameworks staying voluntary as deployment enters critical infrastructure;
interpretability funded as a research curiosity rather than as production
engineering.

---

### Future 5 — The Long Future
*All four pillars. The one worth wanting.*

This is not a utopia in the sense of a world without problems. It is a world that
kept its ability to solve them. Here is what it actually looks like, and — more
usefully — what had to be true to get there.

**What it looks like, around 2040.**

The handover happens on an ordinary Tuesday, which is the point. There is no
singularity, no rapture, no upload. There is a very good tool, widely understood,
pointed at the right problems.

*Energy and environment.* The buildout's demand for firm clean power did what
decades of climate policy could not: it made a customer with a balance sheet want
24/7 carbon-free electricity badly enough to pay for it up front. Restarted
reactors, SMR fleets, geothermal at scale, and storage all got built because
somebody needed them on a twenty-year contract. The grid is cleaner *because* of the
load, not despite it. Waste heat from compute warms homes in the towns that host
it. Water is closed-loop as a matter of course, and the watersheds around the big
sites are measured publicly, monthly, and are in better shape than in 2026 — because
recharge was funded as infrastructure rather than offset as PR.

*Science and health.* The Phase III readouts that started arriving in 2026 kept
coming. Diseases that were rare enough to be economically uninteresting became
tractable, because the marginal cost of designing a candidate collapsed. Trials that
took a decade take two years. The 15% survival benefit from better patient
selection was the first small instance of a general pattern: not AI replacing
clinicians, but AI making the difference between the right treatment and the
approximately-right one, at scale, for everyone rather than for the well-connected.

*Ecosystems.* This is the part that Star Trek always skipped and that actually
matters. Continuous monitoring of forests, reefs, fisheries, soil and freshwater
gives us, for the first time, a real-time picture of the living systems we depend
on — and the ability to model interventions before making them. We stop managing
ecosystems by anecdote and lawsuit. Restoration becomes an engineering discipline
with feedback loops.

*Work and dignity.* The entry-level squeeze of the 2020s was real and it was
addressed, not ignored — through deliberate reconstruction of how people enter
careers, because the alternative was a generation with no ladder. Cognitive
abundance lowered the cost of expertise rather than eliminating the experts: a
person in a poor country gets the same quality of legal, medical and educational
help as a person in a rich one, which is the single largest equity gain in the
scenario.

*Governance.* The system can explain its own reasoning to a room of people who do
not work for its owners — and does, routinely, in public. It is not a god and it is
not a monster. It is the best tool anyone ever made, understood by the people who
use it, doing the arithmetic of keeping eight billion people fed, healthy and warm
without burning down the place they live.

**What had to be true — the preconditions, in rough order of difficulty:**

1. **Interpretability became production engineering.** Not a research programme
   competing for headcount, but a funded, staffed, non-negotiable part of shipping —
   with the authority to stop a launch. The evaluation gap was treated as an
   instrument-calibration crisis, which is what it was.
2. **Honest reporting was rewarded, structurally.** Systems that said "I don't know"
   were reinforced for it, and so were the people who escalated problems. This is
   the cheapest intervention in the entire list and the one most often skipped.
3. **The finances stayed sane enough to permit patience.** Not conservative — the
   buildout was enormous — but funded such that a six-month safety delay was
   survivable. Every other precondition depends on this one.
4. **Costs were internalised where they landed.** Interconnection paid by the load
   that caused it. Water returned to the basin it came from. Abatements declined
   where they were starving schools. This turned out to be cheaper than the
   alternative, because the alternative was Future 3.
5. **Consent was treated as infrastructure.** Enforceable community benefit
   agreements, monthly public reporting before anyone demanded it, and heat and
   power flowing back into the host town. The 14% number was a leading indicator of
   losing the licence to operate, and it was read as one.
6. **Benefits were distributed deliberately.** "Highly uneven rates globally" was
   treated as the central problem rather than a footnote. Access was engineered,
   funded and measured, because a technology that only helps the people who already
   have everything does not survive contact with democracy.
7. **Someone kept the ability to switch it off, and never needed to.**

**What makes this scenario hard is not any single item.** It is that they must all
hold *at once*, for two decades, under competitive pressure, across multiple
jurisdictions, while the people making the decisions rotate. Three out of four
pillars gets you Futures 1 through 4. There is no partial credit for the fifth.

**Early indicators that we are on this path:** firm clean generation being *added*
faster than data centre load grows; watershed metrics published monthly and
improving; interpretability headcount growing as a share of engineering rather than
shrinking; safety frameworks moving from voluntary to binding *before* a
catastrophe rather than after; benefit access decoupling from capital
concentration; and — the simplest one — that 14% number going up.

---

## What to watch

If you want to know which future you are in, these are the numbers that will tell
you before the narrative does:

1. **PJM-style capacity prices and their attribution.** The market monitor's
   counterfactual is the honest instrument. If the data-centre-attributable share of
   cost increases keeps rising, Future 2 is consolidating.
2. **The Reuters/Ipsos welcome number** (14% in 2026). It is the single best proxy
   for social licence. Rising means consent is being rebuilt; falling means Future 3.
3. **Firm clean capacity added vs. load added.** If generation additions outrun
   demand additions, the environmental pillar is holding.
4. **Evaluation-awareness rates in frontier model cards.** The leading indicator for
   Future 4, and the one most likely to be under-reported.
5. **Free cash flow and off-balance-sheet commitments.** The leading indicator for
   Future 1, and the one that constrains every other choice.
6. **Whether safety frameworks become binding before an incident, or after.**
7. **Whether AI-derived health and science benefits reach low-income countries at
   anything like the rate they reach rich ones.** The leading indicator is boring
   and specific: whether health ministries carry AI diagnostics as a **recurring
   budget line** rather than a grant.

And the same number of indicators for the upside, because a scorecard that can only
detect failure will only ever report it:

8. **Contracted flexible load as a share of new large-load interconnections.** The
   cheapest capacity on the system. Google's 1 GW is the floor, not the ceiling — if
   this becomes standard tariff language rather than a bespoke deal, Future 5 is
   live.
9. **Large-load tariffs in force, and whether they survive preemption.** 24 states
   by July 2026. If that number keeps climbing and the terms hold, the fiscal and
   environmental pillars are being defended by the same instrument.
10. **Closed-loop as the default rather than the upgrade.** Watch new-build
    announcements for evaporative cooling in water-stressed basins. Its absence is
    the signal.
11. **Community benefit agreements that are public, enforceable and pre-vote.**
    The value matters less than whether residents could read it before the council
    voted.
12. **Deployment decisions changed by pre-deployment testing.** Rare, underreported,
    and the single best evidence that the safety apparatus is load-bearing rather
    than decorative.

---

## Sources

**Primary and official**
- [International AI Safety Report 2026](https://arxiv.org/pdf/2602.21012) — Chair: Yoshua Bengio; DSIT 2026/001, February 2026. 100+ experts, panel nominated by 30+ countries, EU/OECD/UN.
- [IEA — Energy demand from AI (*Energy and AI*)](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- [IEA news — AI set to drive surging electricity demand from data centres](https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works)
- [OpenAI — Detecting and reducing scheming in AI models](https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/)
- [Apollo Research — Science](https://www.apolloresearch.ai/science)
- [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/pdf/2406.07358)
- [Anthropic — Labor market impacts of AI: a new measure and early evidence](https://www.anthropic.com/research/labor-market-impacts)
- [NY Fed Liberty Street Economics — Do Job Postings Show Early Labor-Market Effects of AI?](https://libertystreeteconomics.newyorkfed.org/2026/05/do-job-postings-show-early-labor-market-effects-of-ai/)
- [ICLE — AI, Productivity, and Labor Markets: A Review of the Empirical Evidence](https://laweconcenter.org/resources/ai-productivity-and-labor-markets-a-review-of-the-empirical-evidence/) — source of the no-displacement, skill-compression and productivity-range findings.
- [IMF — New Jobs Creation in the AI Age (SDN/2026/001)](https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf)
- [PwC — 2026 Global AI Jobs Barometer](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-jobs-barometer.html) — consultancy source; wage-premium magnitudes treated as contested.
- [OpenAI — Strengthening our safety ecosystem with external testing](https://openai.com/index/strengthening-safety-with-external-testing/)
- [Future of Life Institute — AI Safety Index, Summer 2026](https://futureoflife.org/ai-safety-index-summer-2026/) — advocacy source; the "entirely inadequate" panel verdict.
- [Effectiveness of AI-Based Tools in Detecting Diabetic Retinopathy in Low- and Middle-Income Countries](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12697004/)
- [AI-Enhanced Point-of-Care Diagnostics for Infectious Diseases in Resource-Limited Settings](https://pmc.ncbi.nlm.nih.gov/articles/PMC13432776/)
- [From pilot to policy: why AI health interventions fail to scale in developing countries](https://pmc.ncbi.nlm.nih.gov/articles/PMC12894408/) — source of the East Africa TB shutdown.

**Energy, grid and cost**
- [IEEFA — Projected data center growth spurs PJM capacity prices by factor of 10](https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10)
- [Canary Media — PJM capacity costs hit record as grid falls short on supply](https://www.canarymedia.com/articles/data-centers/pjm-record-capacity-costs-rising-bills)
- [E&E News/POLITICO — Data centers drive 76% surge in PJM power prices](https://www.eenews.net/articles/data-centers-drive-76-surge-in-pjm-power-prices/)
- [SemiAnalysis — Are AI Datacenters Increasing Electric Bills for American Households?](https://newsletter.semianalysis.com/p/are-ai-datacenters-increasing-electric)
- [S&P Global — Global data center power demand to double by 2030 on AI surge](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/041025-global-data-center-power-demand-to-double-by-2030-on-ai-surge-iea)
- [Carbon Brief — Five charts on data-centre energy use and emissions](https://www.carbonbrief.org/ai-five-charts-that-put-data-centre-energy-use-and-emissions-into-context)
- [EIA via pv magazine — Solar and storage to lead 86 GW capacity surge in 2026](https://pv-magazine-usa.com/2026/04/28/solar-and-storage-to-lead-86-gw-capacity-surge-in-2026/)
- [Electrek — EIA: 80 GW of new solar, wind + storage capacity coming in 2026](https://electrek.co/2026/04/27/eia-80-gw-of-new-solar-wind-storage-capacity-coming-in-2026/)
- [Google — Signing 1 GW of data center demand response](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/demand-response-data-center-milestone/) — 19 March 2026; I&M, TVA, Entergy Arkansas, Minnesota Power, DTE.
- [Google — How we're making data centers more flexible to benefit power grids](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/)
- [Renewable Energy World — Google has integrated 1 GW of data center demand response](https://www.renewableenergyworld.com/power-grid/smart-grids/google-has-integrated-1-gw-of-data-center-demand-response-with-us-utilities/) — reports the Duke figure: 76 GW absorbable at 0.25% average annual curtailment.
- [Columbia Climate Law Blog — Large-Load Tariffs and Clean Transition Tariffs](https://blogs.law.columbia.edu/climatechange/2026/06/02/data-center-regulation-what-local-governments-should-know-about-large-load-tariffs-and-clean-transition-tariffs/)
- [EEI — Large Load Projects and Tariffs (August 2026)](https://www.eei.org/-/media/Project/EEI/Documents/Issues%20and%20Policy/List%20of%20Large%20Customer%20Projects%20and%20Tariffs)
- [Utility Dive — Oregon PUC approves PGE's large-load tariff framework](https://www.utilitydive.com/news/oregon-puc-approves-pges-large-load-tariff-framework-for-data-centers/821361/)
- [Sierra Club — Data Center State Policies, 2026](https://www.sierraclub.org/sites/default/files/2026-01/policies-for-data-centers-2026.pdf) — advocacy source; used for policy counts, not for framing.

**Water and land**
- [Lincoln Institute of Land Policy — Data Drain: The Land and Water Impacts of the AI Boom](https://www.lincolninst.edu/publications/land-lines-magazine/articles/land-water-impacts-data-centers/)
- [EESI — Data Centers and Water Consumption](https://www.eesi.org/articles/view/data-centers-and-water-consumption)
- [UGA CAES — Understanding How Data Centers Impact Surface and Ground Waters](https://fieldreport.caes.uga.edu/publications/TP121/how-data-centers-impact-surface-and-ground-waters/)
- [ITIF — The Data Center Water Problem Is Soluble](https://itif.org/publications/2026/07/06/the-data-center-water-problem-is-soluble/)
- [Newsweek — Map Shows Where Data Centers Are Being Built in Drought-Hit Areas](https://www.newsweek.com/map-data-centers-built-drought-hit-areas-11997520)
- [DCD — Microsoft's upcoming data centers to use closed-loop, zero-water evaporation design](https://www.datacenterdynamics.com/en/news/microsofts-upcoming-data-centers-to-use-closed-loop-zero-water-evaporation-design/)
- [Microsoft — Inside a two-decade push to cut water intensity while scaling for growth](https://blogs.microsoft.com/blog/2026/06/24/inside-microsofts-two-decade-push-to-cut-water-intensity-while-scaling-for-growth/) — company-reported; source of the FY25 water-positive and 40%-intensity figures.
- [Oracle — Closed-loop cooling in Oracle AI data centers](https://www.oracle.com/news/announcement/blog/closed-loop-cooling-in-oracle-ai-data-centers-2026-02-09/)
- [WEF — What new water circularity can look like for data centres](https://www.weforum.org/stories/2025/11/data-centres-and-water-circularity/)
- [Vantage — Cooling Without the Drain: How Closed-Loop Systems Cut Day-to-Day Water Use](https://blog.vantage-dc.com/2026/04/22/cooling-without-the-drain-how-closed-loop-systems-cut-day-to-day-water-use/) — vendor source; used for mechanism, not for magnitude.

**Local politics and siting**
- [Columbia Climate Law Blog — Local Moratoria Against Data Center Construction](https://blogs.law.columbia.edu/climatechange/2026/05/27/local-moratoria-considerations/)
- [Columbia Climate Law Blog — Community Benefits Agreements and Data Center Development](https://blogs.law.columbia.edu/climatechange/2026/05/28/community-benefits-agreements-and-data-center-development/)
- [Rockefeller Institute — Updates on the Cloud: More Moratoriums on Data Centers](https://www.rockinst.org/blog/updates-on-the-cloud-more-moratoriums-on-data-centers/)
- [Fort Worth Report — Zoning commissioners deny data center rules](https://fortworthreport.org/2026/07/08/zoning-commissioners-deny-data-center-rules-return-ordinance-to-fort-worth-city-council/)
- [US Data Center Policy Tracker](https://dcmap.us/insights/policy/)
- [DCD — Community benefit agreements are essential to data center success](https://www.datacenterdynamics.com/en/opinions/community-benefit-agreements-are-essential-to-data-center-success/)
- [EESI — Thermal Energy Networks Turn Data Center Waste Heat into a Hot Commodity](https://www.eesi.org/articles/view/thermal-energy-networks-turn-data-center-waste-heat-into-a-hot-commodity)
- [Open Compute Project — Seizing Data Center Heat Reuse Opportunities: Guidelines for Local Authorities](https://www.opencompute.org/documents/2024-09-ocp-hr-wp-2-pager-local-authorities-docx-1-pdf)
- [Conduit Street (Maryland Association of Counties) — Frederick Secures $110M Community Benefits Agreement](https://conduitstreet.mdcounties.org/2026/09/02/frederick-secures-110m-community-benefits-agreement-for-data-center-campus/) — announced 1 September 2026; public comment through 10 September; DRRA still in county review.
- [FAS — What's with all the secret data center agreements?](https://fas.org/publication/data-center-community-benefit-agreements/) — the non-disclosure critique.
- [Brookings — Why community benefit agreements are necessary for data centers](https://www.brookings.edu/articles/why-community-benefit-agreements-are-necessary-for-data-centers/)
- [Spotlight PA — Data centers offer communities cash, other incentives](https://www.spotlightpa.org/news/2026/09/data-center-gifts-bonuses-incentives-communities-pennsylvania-federal-government/)

**Power procurement**
- [DCD — Three Mile Island to return as Microsoft signs 20-year, 835MW PPA](https://www.datacenterdynamics.com/en/news/three-mile-island-nuclear-power-plant-to-return-as-microsoft-signs-20-year-835mw-ai-data-center-ppa/)
- [NucNet — Constellation secures $1 billion federal loan for Three Mile Island restart](https://www.nucnet.org/news/constellation-secures-usd1-billion-federal-loann-for-three-mile-island-restart-11-3-2025)
- [Pennsylvania Capital-Star — Energy Secretary on the Three Mile Island restart](https://penncapital-star.com/economy/energy-secretary-christopher-wright-says-three-mile-island-restart-delivers-on-trump-administration-promises/)

**Finance**
- [Man Group — The AI Bubble: Hidden Risks and Opportunities](https://www.man.com/insights/the-ai-bubble)
- [Allianz Research — AI capex cycle: war-proof for now](https://www.allianz.com/content/dam/onemarketing/azcom/Allianz_com/economic-research/publications/specials/en/2026/march/2026_03_25_AI.pdf)
- [Quinn Emanuel — Emerging Litigation Risks in Financing AI Data Centers](https://www.quinnemanuel.com/the-firm/publications/client-alert-emerging-litigation-risks-in-financing-ai-data-centers-boom/)
- [Motley Fool — Is the AI Data Center Boom Creating a Debt Bubble?](https://www.fool.com/investing/2026/07/11/is-the-ai-data-center-boom-creating-a-debt-bubble/)

**Regulation and consumer safety**
- [Orrick — 2026 State Chatbot Laws: Key Provisions and Regulatory Trends](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends)
- [Troutman — Analyzing the New AI Companion Chatbot Laws](https://www.troutmanprivacy.com/2026/01/analyzing-the-new-ai-companion-chatbot-laws/)
- [California Lawyers Association — Regulatory Focus on AI Companion/Character Chatbots](https://calawyers.org/privacy-law/regulatory-focus-on-ai-companion-character-chatbots/)
- [Cloud Security Alliance — State AI Laws Take Hold as Federal Preemption Stalls](https://labs.cloudsecurityalliance.org/research/csa-research-note-us-ai-regulation-preemption-compliance-202/)
- [Gunderson Dettmer — 2026 AI Laws Update](https://www.gunder.com/en/news-insights/insights/2026-ai-laws-update-key-regulations-and-practical-guidance)
- [National Law Review — 2026 Outlook: Artificial Intelligence](https://natlawreview.com/article/2026-outlook-artificial-intelligence)

**Benefits**
- [Drug Target Review — AI in drug discovery: predictions for 2026](https://www.drugtargetreview.com/ai-in-drug-discovery-predictions-for-2026/1865962.article)
- [CAS Insights — Scientific breakthroughs: 2026 emerging trends to watch](https://www.cas.org/resources/cas-insights/scientific-breakthroughs-2026-emerging-trends-watch)
- [ZipRecruiter Economic Research — More Jobs, Higher Bar: The 2026 AI Employer Report](https://www.ziprecruiter-research.org/economic-insights-research/ai-employer-report-2026)

---

*Last updated: September 2026. Part I should be revised as the record changes; Part
II should be revised when the indicators move.*
