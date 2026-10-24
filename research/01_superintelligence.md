# 01 — Artificial Superintelligence (ASI): State of the Field, Oct 2026

*Research notes for the "Superintelligence × Quantum Computing" site. Written 25 Oct 2026. Labels: **[FACT]** = documented in a cited source; **[CLAIM]** = a named person/org's assertion or forecast; **[SPEC]** = speculation/extrapolation; **[UNVERIFIED]** = only seen in low-quality/secondary sources. Source numbers refer to the Sources section.*

## 1. Definitions: ANI → AGI → ASI

| Term | Working definition | Status |
|---|---|---|
| **ANI** (narrow AI) | Systems that perform specific tasks (chess, translation, protein folding). | **[FACT]** Everything deployed historically. |
| **AGI** | AI matching human-level cognition across most tasks. No agreed test; definitions differ by lab. Google DeepMind has published a levels-of-AGI framework (breadth × depth × autonomy) [S3]. | **[FACT]** Not achieved by consensus; International AI Safety Report 2026 describes frontier capability as "jagged" — strong at expert-level maths/code, weak at some simple tasks [S5]. |
| **ASI** | Bostrom (2014): "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest" [S1]. | **[SPEC]** Does not exist. |

**Bostrom's three forms of superintelligence** [S1, S2]: *speed* (human-like mind, much faster), *collective* (many minds aggregated), *quality* (qualitatively smarter). Relevance: Amodei's "country of geniuses in a datacenter" is essentially a speed+collective ASI scenario (§3).

**Operational definitions used by forecasters:** AI Impacts "high-level machine intelligence" (unaided machines outperform humans at every task, cheaper) [S9]; AI Futures Project "Automated Coder" → superhuman coder → ASI milestones [S12, S13]; OpenAI frames itself as "a superintelligence research company" [S6].

## 2. Key thinkers and their (dated) positions

- **Nick Bostrom** — *Superintelligence: Paths, Dangers, Strategies* (2014): defined forms of SI and the control problem [S1, S2].
- **Ray Kurzweil** — *The Singularity Is Nearer* (25 Jun 2024) reiterates AGI-level AI by **2029** and human–machine merger/Singularity by **2045** [S7, S8]. **[CLAIM]**
- **Geoffrey Hinton** (Nobel laureate): Dec 2024 put 30-year extinction odds at 10–20% [S10]; on BBC Newsnight (9 Sep 2026) said a 10% extinction chance within a decade "seems not an unreasonable estimate… but nobody really knows how to give a sensible estimate" [S11]. **[CLAIM, subjective probability]**
- **Sam Altman** (OpenAI) — "The Gentle Singularity" (10 Jun 2025): "We are past the event horizon; the takeoff has started. Humanity is close to building digital superintelligence"; predicts agents doing cognitive work in 2025, "systems that can figure out novel insights" in 2026, real-world robots in 2027 [S6]. **[CLAIM]**
- **Dario Amodei** (Anthropic) — *Machines of Loving Grace* (Oct 2024; optimistic "powerful AI" scenario) and *The Adolescence of Technology* (26 Jan 2026): powerful AI may arrive within 1–2 years; imagines a "country of geniuses in a datacenter" (~50 million instances, running ~10× human speed) around 2027; calls it potentially "the single most serious national security threat" in a century [S14, S15]. At Davos (Jan 2026) repeated that AI could replace software engineers' work within a year and eliminate half of entry-level white-collar jobs within five years [S14]. **[CLAIM]**
- **Demis Hassabis** (Google DeepMind) — timeline compression: AGI "5–10 years" (Dec 2025) → ~2030 (May 2026) → 2–3 years / "2028 or 2029" per WSJ Magazine interview (reported by Tom's Guide/Yahoo, 2026) [S3]. He acknowledged some urgent language is meant to push governments to take the technology seriously [S3]. **[CLAIM]**
- **Ilya Sutskever** (Safe Superintelligence Inc., SSI) — Nov 2025 Dwarkesh interview: the "age of scaling" (2020–25) is giving way to an "age of research… just with big computers"; pre-training data is finite; models "generalize dramatically worse than people"; SSI described as an "age of research" company [S16]. Reported superintelligence timeline of "5 to 20 years" comes from a secondary summary [S16b]. **[CLAIM]** SSI funding/valuation reports (e.g., a $5B Nvidia investment at ~$32B valuation) appear only on low-tier aggregator sites — **[UNVERIFIED]**, do not publish without a Reuters/Bloomberg source.

## 3. Current state of frontier AI (as of Oct 2026)

### 3.1 Scaling laws and the "scaling vs. research" debate
- **[FACT]** Epoch AI: frontier training compute has grown ~4–5×/year; training cost ~3.5×/yr (as of Feb 2026); estimated cost ~$2M for GPT-3 vs ~$500M for Grok 4 [S17, S18]. Extrapolation to ~2e29 FLOP training runs by 2030 is feasible (GPT-4 ≈ 2e25 FLOP); binding constraints are power first, then chip production [S18]. **[SPEC]** that spending continues.
- **[FACT]** The International AI Safety Report 2026 (Feb 2026; chaired by Yoshua Bengio, 100+ experts, 30+ countries) says progress through 2030 is uncertain but trends are consistent with continued improvement; developers have announced hundreds of billions of dollars in data-centre investment [S5].
- **[CLAIM]** Sutskever argues pure scaling is hitting limits and new ideas (better generalization, sample-efficiency) are needed [S16]. Counter-view from lab leaders (Altman, Amodei) is that current trajectory suffices. **Unresolved.**

### 3.2 Reasoning models and agents
- **[FACT]** Inference-time scaling (letting models spend more compute on intermediate reasoning steps) drove "particularly large" gains in maths, software engineering and science in the past year [S5].
- **[FACT]** OpenAI reports its models reached gold-medal-level performance at the International Mathematical Olympiad and International Olympiad in Informatics (2025) [S19]; OpenAI's own evaluation, not an IMO-coordinated certification at the time [S19b].
- **[FACT]** METR "time horizon" (length of tasks, in human-expert time, an AI completes at 50% reliability): doubled roughly every ~7 months over ~6 years, faster (~4–5 months) since 2024 [S12]. METR's Time Horizon 1.1 (29 Jan 2026) expanded its suite from 170 to 228 tasks; o3 measured ≈ 2 hours (116–119 min) on the new suite [S20]. A secondary source reports a further revision to an ~89-day doubling since 2024 **[UNVERIFIED — check metr.org]** [S21].
- **[FACT]** Capabilities remain "jagged" and agents struggle to recover from basic errors in long workflows [S5].

### 3.3 Compute and energy
- **[FACT]** Epoch/EPRI: largest frontier training runs already exceed 100 MW; power for the largest runs growing ~2.2–2.9×/year → **4–16 GW by 2030**; >100 GW total AI capacity worldwide (>50 GW US, ~5% of US generation capacity) is plausible by 2030 [S22].
- **[FACT]** IEA: electricity generation for data centres rises from **460 TWh (2024) to >1,000 TWh (2030)** and 1,300 TWh (2035) in its base case [S23].
- **[FACT]** OpenAI "Stargate": announced multi-site build-out; e.g., 1 GW "Barn" campus in Michigan (Oracle/Related Digital), SB Energy partnership (9 Jan 2026) [S24, S25].
- **[SPEC]** Whether energy/chips or algorithms become the bottleneck for ASI is open; this is the main bridge to the quantum-computing parts of the site (energy-efficient or fundamentally different compute).

## 4. Timeline forecasts (surveys, forecasters, labs)

| Source | Forecast | Type |
|---|---|---|
| AI Impacts 2023 survey, 2,778 AI authors | 10% chance by 2027, **50% by 2047** that unaided machines beat humans at every task (13 years earlier than the 2022 survey); 38–51% gave ≥10% to extinction-level outcomes (varies by question) [S9] | Survey (Oct 2023; dated) |
| Metaculus community | General-AI median ≈ April 2031 (range 2028–2037) as of 24 Sep 2026 per a secondary tracker [S26] | Forecasting platform — verify live |
| AI Futures Project (AI 2027 scenario; model revamped 31 Dec 2025) | Scenario had superhuman coder in Mar 2027 and ASI ~1 year later; authors present it as a forecast model not certainty [S13, S12b] | Forecast/scenario |
| Anthropic (Amodei) | "Powerful AI" possibly 2026–27 [S14, S15, S27] | Lab claim |
| OpenAI (Altman) | Superintelligence "close"; novel insights 2026 [S6] | Lab claim |
| Google DeepMind (Hassabis) | AGI ~2028–2030 [S3] | Lab claim |
| Kurzweil | AGI 2029, Singularity 2045 [S7] | Futurist claim |

**Reading guide:** lab-leader timelines have shortened year-on-year and carry commercial/fundraising incentives; the large academic survey is three years old and predates reasoning models. Treat all as **[SPEC]**. Note that Hassabis himself said urgency in his language is partly to motivate policy attention [S3].

## 5. Main technical approaches to ASI
1. **Scaled pre-training + RL/reasoning** (transformer LLMs, inference-time compute) — the dominant lab strategy (OpenAI, Anthropic, Google DeepMind) [S5].
2. **Agentic systems / AI R&D automation** — AI doing AI research, the "intelligence explosion" route; AI Futures models this via coding time-horizon → Automated Coder → superhuman researcher [S12b, S13]. Critics (and ex-lab staff) warn about "self-improving superintelligence" races [S11].
3. **New learning paradigms / "age of research"** — better generalization, continual learning, human-like sample efficiency (SSI thesis) [S16].
4. **Embodied/robotic and scientific AI** — Altman expects robots in 2027 [S6]; OpenAI "FrontierScience" evaluation of research tasks [S19].
5. **Brain-inspired / neuromorphic / hybrid and (speculatively) quantum-accelerated approaches** — outside this file's scope; **[SPEC]**, see other research files.

## 6. Risks and alignment/safety
- **[FACT]** International AI Safety Report 2026 groups risks into misuse, malfunctions, and systemic disruption; recommends "defence-in-depth" (multiple layered safeguards), notes open-weight models can't be recalled and have easily removed safeguards, and urges societal resilience measures [S5].
- **Core ASI risk arguments** (Bostrom's control problem; Hinton's "never created beings smarter than us") **[SPEC/CLAIM]** — loss of control, power concentration, bio/cyber misuse (Hinton: AI could design viruses/cyberattacks and cause "chaos just by talking to people") [S1, S11].
- **Amodei's categories:** autonomous AI takeover, misuse by bad actors (e.g., terrorists with "mercenary" AI), economic disruption/mass unemployment, indirect destabilization [S14, S15].
- **Alignment research directions:** scalable oversight, interpretability, evaluations (METR, UK AISI), red-teaming, control/monitoring — described generally in [S5]; specific lab methods not individually verified here.
- **Public/elite concern:** Future of Life Institute "Statement on Superintelligence" (22 Oct 2025) calls for a prohibition on developing superintelligence until broad scientific consensus on safety and strong public buy-in; ~65,000 signatories within days [S28, S29].
- **Insider dissent (single report, treat with caution):** a young researcher resigned from Anthropic (Sep 2026) alleging OpenAI and Anthropic are "racing straight to self-improving superintelligence" [S11].

## 7. Governance and regulation
- **EU:** AI Act (Reg. 2024/1689) — prohibited practices (Feb 2025) and GPAI-model rules (Aug 2025) apply; Commission enforcement powers over GPAI and Art. 50 transparency obligations apply from **2 Aug 2026**; the Digital Omnibus on AI (Reg. 2026/1744, in force 27 Jul 2026) delayed high-risk obligations to 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I) [S30, S31]. Penalties up to €15M/3% for Art. 50 breaches (GPAI-model fines can be higher under the Act — not verified here).
- **US federal:** EO 14179 (23 Jan 2025) removed Biden-era AI order; EO 14365 (11 Dec 2025, "Ensuring a National Policy Framework for AI") sets up a DOJ AI Litigation Task Force to challenge state AI laws and conditions some BEAD funds — it cannot itself invalidate state laws [S32, S33].
- **US states:** California **SB 53** (Transparency in Frontier AI Act), signed 29 Sep 2025 — first US state law expressly regulating frontier developers (disclosure/safety-framework and incident-reporting design, successor to vetoed SB 1047) [S34, S35]. Legal challenge/preemption fight is ongoing and unresolved.
- **International:** International AI Safety Report (Bengio-led, UK-hosted, 2nd edition Feb 2026) [S5]. No binding international regime on superintelligence exists **[FACT as of this research; not exhaustively verified]**.
- **Civil society:** FLI superintelligence-prohibition statement [S28].

## 8. Takeaways for the site
1. ASI is **hypothetical**; AGI timelines from labs cluster ~2027–2031, while the only large survey is dated (2047 median) and independent forecaster medians sit ~2031.
2. Compute/energy (4–16 GW single runs by 2030; data centres >1,000 TWh by 2030) is the physical bottleneck — the natural hook for quantum/post-classical compute discussions.
3. Whether scaling alone suffices (Altman/Amodei) or new research paradigms are needed (Sutskever) is the central technical disagreement.
4. Governance is fragmenting: EU delay of high-risk rules, US federal preemption push vs state frontier-AI laws, and calls for outright prohibition.

## Sources
- S1 Bostrom definition & forms (quoting *Superintelligence* p.22): https://digifesto.com/tag/collective-intelligence
- S2 *Superintelligence* ch. "Forms of superintelligence": https://publicism.info/philosophy/superintelligence/4.html
- S3 Hassabis AGI 2–3 yrs (WSJ Magazine via Tom's Guide/Yahoo): https://tech.yahoo.com/ai/gemini/articles/google-deepminds-demis-hassabis-predicts-145225960.html ; earlier-timeline summary: https://m.36kr.com/p/4037020591018881
- S5 International AI Safety Report 2026 exec. summary: https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-executive-summary_1.pdf ; landing: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026
- S6 Altman, "The Gentle Singularity": https://blog.samaltman.com/the-gentle-singularity
- S7 Kurzweil, *The Singularity Is Nearer*: https://en.wikipedia.org/wiki/The_Singularity_Is_Nearer
- S8 Guardian Kurzweil interview: https://amp.theguardian.com/technology/article/2024/jun/29/ray-kurzweil-google-ai-the-singularity-is-nearer
- S9 AI Impacts 2023 survey (arXiv 2401.02843): https://arxiv.org/pdf/2401.02843.pdf ; summary: https://agihunt.info/en/papers/2401.02843
- S10 Hinton 10–20% (Guardian, 27 Dec 2024): https://theguardian.com/technology/2024/dec/27/godfather-of-ai-raises-odds-of-the-technology-wiping-out-humanity-over-next-30-years
- S11 Hinton BBC Newsnight, Sep 2026 (Anadolu): https://h.aa.com.tr/en/world/ai-pioneer-geoffrey-hinton-says-10-risk-of-human-extinction-from-ai-not-unreasonable/4053063
- S12 AI Futures Model (METR time-horizon basis): https://www.aifuturesmodel.com/ ; S12b AI 2027 takeoff forecast: https://ai-2027.com/research/takeoff-forecast
- S13 AI 2027 timelines: https://ai-2027.com/supplements/timelines-forecast
- S14 Fortune on Amodei essay: https://fortune.com/2026/01/27/country-of-geniuses-anthropic-dario-amodei-50-million-nobel-prize-winners
- S15 Amodei essay: https://www.darioamodei.com/essay/the-adolescence-of-technology ; Economic Times summary: https://economictimes.indiatimes.com/tech/artificial-intelligence/in-dystopian-essay-anthropic-ceo-dario-amodei-warns-of-potential-ai-misuse-by-rogue-actors/printarticle/127598488.cms
- S16 Sutskever on Dwarkesh: https://pod.wave.co/podcast/dwarkesh-podcast-3/ilya-sutskever-were-moving-from-the-age-of-scaling-to-the-age-of-research ; summary: https://biechi.github.io/blog/a2s5r6 ; S16b https://pjfp.com/tag/age-of-research
- S17 Epoch cost/compute trend (secondary summary): https://github.com/PatrickWiloak/genai-research-papers-summarized/blob/main/explainers/compute/cost-of-training.md
- S18 Epoch, "Can AI scaling continue through 2030?": https://epochai.org/blog/can-ai-scaling-continue-through-2030
- S19 OpenAI FrontierScience: https://openai.com/index/frontierscience ; S19b IMO caveat: https://intuitionlabs.ai/articles/ai-reasoning-math-olympiad-imo
- S20 METR Time Horizon 1.1: https://metr.org/blog/2026-01-29-time-horizon-1-1/
- S21 (unverified) 89-day doubling: https://aitimeline.dev/en/events/evt-0368
- S22 Epoch/EPRI power demands: http://epoch.ai/blog/power-demands-of-frontier-ai-training
- S23 IEA Energy & AI: https://iea.org/reports/energy-and-ai/energy-supply-for-ai
- S24 OpenAI Stargate Michigan: https://openai.com/index/stargate-michigan-data-center
- S25 OpenAI–SB Energy (9 Jan 2026): https://openai.com/index/stargate-sb-energy-partnership
- S26 Metaculus summary (secondary): https://santageai.com/agi/agi-timelines
- S27 Redwood on Anthropic's early-2027 AGI expectation: https://redwoodresearch.org/blog/whats-up-with-anthropic-predicting
- S28 FLI Statement on Superintelligence: https://superintelligence-statement.org/ ; newsletter: https://newsletter.futureoflife.org/p/fli-newsletter-october-2025
- S29 UNSW commentary: https://unsw.edu.au/newsroom/news/2025/10/ai-heavyweights-call-for-end-to-superintelligence-research
- S30 EU AI Act Aug 2026 status: https://www.aiacto.eu/en/blog/ai-act-what-changes-august-2-2026 ; regulation text: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- S31 Omnibus summary: https://sovereign.tenova.io/guides/eu-ai-omnibus-agreement.html
- S32 EO 14365 explainer: https://casrai.org/guides/trump-ai-executive-orders-eo-14179-eo-14365
- S33 Paul Hastings on EO: https://paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws
- S34 Newsom signs SB 53: https://gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry
- S35 Brookings on SB 53: https://brookings.edu/articles/what-is-californias-ai-safety-law

## Caveats / gaps
- Several 2026 facts rest on secondary outlets (Hassabis WSJ interview, Metaculus median, Hinton/Newsnight via Anadolu); verify against primaries before publishing.
- SSI valuation/Nvidia deal and METR "89-day" revision are unverified.
- Not covered in depth: specific lab alignment techniques, Chinese governance, UN processes, current model names/benchmark scores (ARC-AGI, HLE) — gather if needed.
