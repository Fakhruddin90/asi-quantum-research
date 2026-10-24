# Superintelligence × Quantum Computing: The Relationship

*Research note 03 — written Oct 2026. Evidence tags: **[P]** peer-reviewed/primary source read this session; **[V]** vendor/press claim; **[B]** background knowledge (well-established, not re-fetched this session). Items I could not verify are flagged.*

## TL;DR

- **Superintelligence does not depend on quantum computing.** Every frontier AI system today runs on classical silicon (GPUs/TPUs). No credible roadmap to AGI/ASI requires a quantum computer.
- **The traffic runs mostly one way: AI → quantum.** AI is already useful for building quantum computers (error-correction decoding, code discovery, circuit optimization, calibration). Quantum → AI speedups remain mostly theoretical and have been repeatedly narrowed by classical "dequantization".
- **The most concrete real-world link is security, and it runs through cryptography, not intelligence.** Shor's algorithm threatens RSA/ECC regardless of AI; AI mostly changes the *offence/defence tempo* around it.
- **Shared infrastructure is real but is about plumbing**: GPUs are becoming the control/decoding/simulation layer of quantum computers (NVIDIA CUDA-Q, NVQLink).

---

## 1. Quantum for AI

### 1.1 Quantum machine learning (QML): claimed speedups vs. what survived

- **The promise.** Algorithms such as HHL (linear systems), quantum PCA, quantum recommendation systems and quantum SVMs were advertised as exponentially faster than classical ML. [B]
- **Dequantization (Ewin Tang).** In 2018 Tang gave a *classical* algorithm for recommendation systems that matches the Kerenidis–Prakash quantum algorithm up to polynomial slowdown, removing what had been "one of the strongest candidates for provably exponential speedups in quantum machine learning." The key insight: the quantum algorithm assumed fast quantum state preparation (QRAM-style access); give a classical algorithm the analogous ℓ2 *sample-and-query* access and the exponential gap collapses. Follow-ups dequantized PCA, low-rank regression, supervised clustering and a general "sampling-based low-rank matrix arithmetic" framework (Chia, Gilyén, Li, Lin, Tang, Wang). The qPCA follow-up states its title result bluntly: the exponential speedup holds *only because of its state-preparation assumptions*. [P] (arXiv 1807.04271, 1811.00414, 1910.06151)
  - Scope of the lesson: dequantization applies to *low-rank / well-conditioned linear-algebra* QML. It does **not** refute quantum advantage for all ML, but it removed the headline "exponential speedup on classical data" cases.
- **Data-loading / QRAM bottleneck.** Aaronson's "Read the fine print" (Nature Physics 2015) [B] lists input, output, conditioning and "compared to what classical baseline" caveats. Loading N classical numbers into amplitudes needs either O(N) time or a QRAM whose hardware cost/energy/error-correction overhead is itself ~O(N) physical resources; 2026 papers still describe data-loading as "a fundamental headwind relative to classical methods" [P] (arXiv 2610.03700 "Scalable Passive QRAM"). For ML on today's data-set sizes (billions of tokens), reading the data once already dominates.
- **Power of data.** Huang, Broughton, …, McClean (Nat. Commun. 2021) showed that with enough training data, classical models can match quantum models on many datasets; quantum advantage requires specially structured, quantum-native problems. [P]
- **Where quantum learning advantage is genuinely proven:** when the *data itself is quantum* (experiments on quantum systems). Huang et al., *Science* 2022, "Quantum advantage in learning from experiments," proved exponential advantage for a quantum learner with quantum memory on certain physical-property-learning tasks. [P] That is learning about quantum physics, not training language models.
- **Variational QML (the NISQ-era approach).** Training is hampered by barren plateaus; a 2025 Nature Communications perspective argues that provable absence of barren plateaus often implies classical simulability (Cerezo et al.). LANL work reached a similar conclusion for some models. [P] Net: the "quantum neural net on today's hardware beats a classical one" claim lacks credible evidence.
- **Reality check on hybrid claims.** An example from the literature: adding a quantum circuit to a chemistry neural network gave slightly better accuracy, but the authors noted the improvement was not reproducible on a noiseless simulator and may reflect hardware noise (as summarized by PostQuantum.com's taxonomy). [V/secondary — unverified in the primary preprint]

### 1.2 Quantum sampling & optimization

- Quantum sampling (e.g., from hard distributions) is where *beyond-classical* demonstrations happen (random circuit sampling, 2019 onward), but the sampled distributions are not useful ML models. [B]
- Optimization (QAOA, annealing): no broadly accepted evidence of an end-to-end speedup over best classical heuristics on practical instances. Grover-type quadratic speedups are real in theory but are eaten by error-correction overhead on realistic clock speeds. [B] Treat vendor "optimization advantage" claims as unproven.

### 1.3 Quantum-accelerated training / linear algebra

- Training transformers is dominated by dense matrix multiplication on massive classical datasets with massive parameter counts. The quantum linear-algebra primitives (HHL, QSVT) need QRAM, high condition-number tolerance, and *readout of full vectors* — three assumptions that mostly fail for LLM training. No credible path to quantum-accelerated frontier model training exists today. [B, supported by 1.1]
- A 2026 audit of "can quantum fix AI's energy problem" (blog, non-peer-reviewed) reaches a similar conclusion; treat as opinion. [secondary]

### 1.4 Is quantum *needed* for AGI/ASI? (Penrose vs. mainstream)

- **Penrose–Hameroff Orch-OR** claims human cognition relies on quantum gravity-induced collapse in microtubules and is non-computable, hence AGI via classical computation is impossible. [B]
- **Mainstream view:** (a) Tegmark's decoherence estimate (Phys. Rev. E 2000) put microtubule coherence times far too short for neural-timescale computation; Hameroff et al.'s rebuttal (Phys. Rev. E 2002) disputes the parameters, and the dispute is not settled by consensus-level experiment, but the weight of neuroscience evidence is that neurons operate classically (spikes, synaptic chemistry). [P] (arXiv quant-ph/0005025; PRE 65, 061901) (b) Penrose's Gödel-based non-computability argument is widely regarded as flawed by logicians. (c) Empirically, classical LLM scaling has delivered olympiad-level maths/coding without any quantum component. [B]
- **Verdict on this question:** no evidence that quantum physics is required for general intelligence. Even if brains used quantum effects, that would not imply silicon intelligence needs them; and ASI doesn't need to replicate brains.

---

## 2. AI for Quantum

This is the direction with the strongest, most concrete evidence.

### 2.1 ML for quantum error-correction (QEC) decoding
- **AlphaQubit** (Google DeepMind + Google Quantum AI, *Nature* 635, 834–840, Nov 2024): a recurrent transformer decoder for the surface code. It beat other state-of-the-art decoders on real Sycamore data for distance-3 and distance-5 codes, stayed ahead on simulated data up to distance 11, uses soft-readout/leakage information, and generalized from 25 training rounds to simulated 100,000 rounds. [P]
- **Honest limits (stated by Google):** it is "still too slow to correct errors in a superconducting processor in real time" (checks occur ~1 million times/sec), and training on millions of qubits needs more data-efficient methods. [P]
- AlphaQubit has since been used as a benchmark decoder in follow-on architecture work (e.g., a Google/DeepMind/MIT modular hyperbolic-code paper, arXiv 2610.03682, reported via secondary summary; claims ~30× lower qubit overhead *in simulation*). [secondary; treat as unreviewed preprint]
- IBM's Nov 2025 announcement claimed real-time-capable, classical (non-AI) decoding at ~10× speedup — evidence that *classical algorithmic* decoders remain the competitor/realistic path to real-time. [V]

### 2.2 AI discovery of codes, circuits, encodings (2026 wave)
- **IBM (Jun 2026):** LLM-guided evolutionary search quickly found 465 distinct candidate QEC codes; open-sourced. IBM itself says the practical potential of top candidates is still to be investigated. [V] (arXiv 2606.02418)
- **qBraid + Google AlphaEvolve (Jun 2026):** reported fermion-to-qubit encodings at code distance 5 for dense molecular Hamiltonians (previous known: 3), claiming 4–5× fewer data qubits for fault-tolerant chemistry. [V/secondary, preprint]
- **Harvard/QuEra with Anthropic authors (Oct 2026, arXiv 2610.22367):** an LLM-in-the-loop evolutionary framework with an independent verifier found circuits with fewer Toffoli gates and qubits than state of the art in 7 of 8 tasks (numerics, chemistry, optimization, simulation, number theory) and a new reversible modular-inversion architecture. [P-preprint]
- **Phasecraft (Oct 2026, arXiv 2610.31352):** AI agents automating quantum circuit optimization. [preprint, abstract only]
- **RL compilation:** reinforcement-learning agents for compiling to neutral-atom move synthesis and trapped-ion circuits (arXiv 2506.05536, 2307.05744). [P-preprint]
- Calibration/control: ML-based qubit tuning and pulse optimization is widely published and being productized; I did not verify specific 2026 results this session. [B]

### 2.3 Chemistry & materials
- The prime quantum-computing application (simulating strongly correlated electrons) is exactly where AI *competes* with quantum: neural-network potentials and neural quantum states keep raising the classical bar. A 25–100-logical-qubit chemistry perspective (JCTC 2026) frames what fault-tolerant machines could add. [P] Hybrid "AI + quantum" drug-discovery pipelines are mostly roadmaps today. [secondary: arXiv 2603.17790]
- Google's **Quantum Echoes** (OTOC, *Nature*, Oct 2025) is the best case for "verifiable" quantum advantage; Google claims 13,000× over a leading supercomputer on a benchmark and points to NMR Hamiltonian learning as a path to application. The NMR application was a proof-of-principle, not yet beyond-classical for a useful molecule. [P/V] NVIDIA is credited as a collaborator.
- ⚠ A syncflo.xyz article about "Willow-Alpha" simulating catalysts appeared in searches; I could not corroborate it with a primary source and **did not use it**.

---

## 3. Shared infrastructure

- **GPU–quantum integration.** NVIDIA's **NVQLink** (announced 28 Oct 2025) is an open architecture connecting QPU controllers to GPU supercomputers for real-time QEC/control; supports 17 QPU builders, 5 controller builders and 9 US national labs. [V] A Qblox integration (Oct 2026) reports round-trip latency under 4 µs on NVIDIA RTX PRO 6000 Blackwell. [V]
- **CUDA-Q Logical** (14 Sep 2026): orchestration layer for fault-tolerant application design; Fermilab reports a 7× design-cycle speedup (5 months → 3 weeks); Sandia's QUOPS benchmark added. [V] NVIDIA/Jülich also announced a 104-qubit magic-state-cultivation simulation on JUPITER (GTC Berlin, Oct 2026). [V]
- **Why this matters for the thesis:** the GPU is the *infrastructure of AI* and also the *infrastructure around quantum*. Quantum computers will, for the foreseeable future, be accelerators attached to classical AI-era supercomputers — not replacements for them. The classical side (decoding, calibration, simulation) is a growing workload for the same hardware that trains AI.
- **Energy/compute constraints.** IEA estimated data-centre use at ~415 TWh in 2024, and hyperscaler capex exceeded $400B in 2025 with a further ~75% rise expected in 2026 (IEA, *Key Questions on Energy and AI*). [P] A common pitch is "quantum will fix AI's energy bill". Evidence doesn't support it: quantum machines need cryogenics/control electronics and large classical decoding stacks, and no known quantum algorithm replaces the bulk of transformer compute. [B/secondary]
- **Hardware status (Oct 2026), for context:** Google demonstrated magic state cultivation on Willow, ~40× error reduction (*Science*, 15 Oct 2026) — still a small-scale demo. [P/V] Quantinuum reports 99.9995% logical fidelity on Helios and targets fault-tolerant "Apollo" by 2029. [V] IBM targets Starling (fault-tolerant, 2029). [V] A 2026 *Nature* critique questions Microsoft's Majorana 1 claims. [P] Fault-tolerant machines with useful scale do not yet exist.

---

## 4. Security

- **Shor vs. public-key crypto.** Shor's algorithm breaks RSA, DH and elliptic-curve crypto; symmetric crypto/hashes are only quadratically weakened by Grover (AES-256 stays OK). [B]
- **Cost estimates keep falling.** Gidney (Google, May 2025): RSA-2048 could be factored in under a week with <1 million noisy qubits (0.1% gate error, 1 µs cycle), versus 20 million in 2019 — a ~20× cut, driven by algorithmic/error-correction improvements. [P] (arXiv 2505.15917). Current machines have O(100) physical qubits at useful quality; the gap is still ~4 orders of magnitude.
- **When?** The Global Risk Institute's 2025 expert survey (26 experts): a cryptographically relevant quantum computer is "quite possible (28–49%)" within 10 years and "likely (51–70%)" within 15. [P] Expert opinion, not a measurement.
- **Harvest-now-decrypt-later (HNDL).** Adversaries can store encrypted traffic today for decryption later; relevant to data with long secrecy lifetimes (state secrets, health, IP). Public evidence of specific large-scale harvesting is mostly inference by agencies and commentators. [B]
- **PQC response.** NIST finalized FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA) in Aug 2024; HQC selected as backup KEM in March 2025; NIST IR 8547 sets the transition (as I recall the draft: deprecate quantum-vulnerable algorithms by 2030, disallow by 2035 — verify against the final text). NSA's CNSA 2.0 requires new NSS acquisitions to be quantum-resistant starting 2027. Several articles also cite a June 2025 US executive order on migration. [P/B; dates for 8547 not re-verified]
- **ASI + quantum for cybersecurity — the honest framing:**
  1. *Advanced AI is already a cyber-capability story with no quantum needed.* A Cloud Security Alliance note (Sep 2026) reports OpenAI classified "GPT-6 Astra" as "Critical" for cyber under its Preparedness Framework, with OpenAI's self-reported 100% on ExploitBench; the CSA stresses those numbers are unreplicated self-evaluations. [secondary/vendor — treat cautiously] Independent benchmarks of autonomous multi-step attacks (arXiv 2603.11214; ZeroDayBench 2603.02297) show the same direction. [P-preprint]
  2. *Quantum is a separate, slower, cryptographic break* that hits key exchange and signatures — the foundations of PKI. If both mature, the combination is dangerous mainly through **speed of exploitation, search for implementation flaws in PQC code (side channels, bad migrations), and the AI-assisted design of more efficient Shor implementations.** Evidence that AI is already shrinking quantum-factoring resource counts: the Oct 2026 LLM-driven circuit paper above explicitly lists modular inversion and number-theory primitives — the building blocks of factoring and elliptic-curve attacks — as targets. This is plausible acceleration of the threat, but I found no AI-discovered improvement that changes Gidney's headline numbers. [preprint]
  3. *Defence benefits too.* AI can accelerate crypto-inventory, migration tooling and PQC implementation verification. Migration complexity — not cryptanalysis — is the bottleneck for most organizations.
  4. *Not a "break everything" scenario.* AI does not break math; a lattice or hash break would require new mathematical results. A superintelligence might find such results, but that is speculative either way.

---

## 5. Convergence scenarios and risks

1. **Decoupled (most likely near-term).** ASI-class AI progresses on GPUs; quantum matures on its own timeline (fault tolerance claimed ~2029–2033 by IBM/Quantinuum/Google). They meet only in infrastructure and security.
2. **AI accelerates quantum (plausible, already starting).** AI-found codes, circuits, decoders and compilers shrink qubit/gate counts; AI agents speed up hardware design and calibration. Effect: pulls forward the date of cryptographically relevant machines by an unknown amount (possibly years). Risk: a faster, less-predictable Q-day than survey data suggests.
3. **Quantum accelerates AI (speculative).** Would need fault-tolerant machines plus a genuine advantage for a core AI workload — e.g., quantum-simulated training data for chemistry/materials models, or learning from quantum experiments. Specialized scientific-AI benefits are plausible; generic LLM/AGI acceleration is not supported by current theory.
4. **Compound risk scenario.** Strong autonomous cyber-capable AI + CRQC in the same time window → collapsed trust in legacy PKI, with HNDL archives suddenly readable. Mitigation is dull and available: finish PQC migration, crypto-agility, and treat long-lived secrets as already exposed.
5. **Concentration risk.** Frontier AI labs (Google, IBM, Microsoft, NVIDIA-ecosystem) are also the leading quantum players, so AI-for-quantum feedback loops accrue to a handful of firms and states.
6. **Hype risk.** "Quantum-AI" is a marketing category; funding and valuations can detach from the technical evidence (see 1.1 and Majorana controversy).

---

## Verdict

**Proven / strongly established**
- Shor's algorithm breaks RSA/ECC; Gidney's 2025 estimate (<1M noisy qubits, <1 week) is a published resource analysis, and NIST PQC standards exist today. HNDL is a rational threat model.
- Classical algorithms dequantized much of the claimed exponential QML speedup (Tang et al.); data loading is a real bottleneck.
- Quantum advantage in *learning about quantum systems* is theoretically proven (Huang et al. 2022).
- ML decoders can beat conventional decoders on real small-scale surface-code data (AlphaQubit, *Nature* 2024) — but not yet in real time.
- Quantum computers rely on classical HPC/GPU infrastructure for control and decoding (NVQLink/CUDA-Q are vendor-confirmed products).
- No evidence that AGI/ASI requires quantum computation.

**Plausible (credible, not yet demonstrated at scale)**
- AI-designed QEC codes, encodings and circuits cutting fault-tolerant resource costs (IBM, qBraid/AlphaEvolve, Harvard/QuEra preprints) — promising, mostly preprints and vendor reports.
- Quantum simulation giving AI better chemistry/materials data once fault tolerance arrives (late 2020s–2030s at the earliest).
- AI shortening the timeline to cryptographically relevant quantum computers.
- Verifiable quantum advantage (Quantum Echoes) maturing into an application in NMR/molecular Hamiltonian learning.

**Hype / unsupported**
- "Quantum computers will train/accelerate LLMs or give us AGI/ASI."
- "Quantum is needed for consciousness/general intelligence" (Orch-OR is a minority hypothesis facing strong physical objections).
- "Quantum will solve AI's energy problem."
- Variational/NISQ QML advantage claims, and optimization-advantage marketing without classical-baseline comparison.
- "ASI + quantum = unstoppable code breaker" as stated — the mathematics of Shor needs hardware that doesn't exist yet; AI doesn't remove that constraint.

**Bottom line:** A superintelligence is not *dependent* on quantum computing, but it can be *accelerated by* progress in specialized quantum simulation (later) and can in turn accelerate quantum engineering (now). The urgent, actionable overlap is cryptography: migrate to PQC regardless of how either technology evolves.

---

## Sources

**Quantum-for-AI**
- Tang, "A quantum-inspired classical algorithm for recommendation systems": https://arxiv.org/abs/1807.04271
- Tang, "Quantum PCA only achieves an exponential speedup because of its state preparation assumptions": https://arxiv.org/abs/1811.00414
- Chia et al., "Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing QML": https://arxiv.org/abs/1910.06151
- Tang overview of quantum-inspired sampling: https://ewintang.com/assets/2019-01-28-an-overview-of-quantum-inspired-sampling.pdf
- Huang et al., "Power of data in quantum machine learning": https://arxiv.org/abs/2011.01938
- Huang et al., "Quantum advantage in learning from experiments" (Science 2022): https://science.org/doi/abs/10.1126/science.abn7293
- "Scalable Passive QRAM" (arXiv 2610.03700): https://arxiv.org/pdf/2610.03700
- Cerezo et al., "Does provable absence of barren plateaus imply classical simulability?": https://nature.com/articles/s41467-025-63099-6
- LANL summary: https://lanl.gov/media/news/0409-quantum-learning-models
- Sanders et al., "Future of Quantum Computing" panel (Aaronson et al.): https://arxiv.org/pdf/2506.19232
- PostQuantum.com Quantum-AI taxonomy (secondary): https://postquantum.com/quantum-ai/quantum-ai-taxonomy
- Tegmark/Hameroff Orch-OR debate: https://arxiv.org/html/quant-ph/0005025v1 ; https://pubmed.ncbi.nlm.nih.gov/12188753

**AI-for-quantum**
- AlphaQubit, Nature: https://nature.com/articles/s41586-024-08148-8
- Google blog on AlphaQubit: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphaqubit-quantum-error-correction
- IBM, "Can LLMs discover QEC codes?": https://research.ibm.com/blog/ai-for-qec
- qBraid + AlphaEvolve (secondary): https://quantum-brief.com/blog/news-2026-06-27-qbraid-alphaevolve
- Gu, Kemeny, Yelin, Lukin, "Discovering state-of-the-art quantum circuits with LLMs": https://arxiv.org/pdf/2610.22367v1
- Crichigno & Flammia, "Automating quantum circuit optimization with AI agents": https://arxiv.org/pdf/2610.31352v1
- RL compilation: https://arxiv.org/html/2506.05536v1 ; https://arxiv.org/html/2307.05744v1
- Modular hyperbolic codes (secondary summary): https://danjellinek.com/article/google-s-quantum-leap-reducing-qec-overhead-by-30x-with-modular-hyperbolic-codes
- Google Quantum Echoes: https://research.google/blog/a-verifiable-quantum-advantage ; https://blog.google/innovation-and-ai/technology/research/quantum-hardware-verifiable-advantage
- Google magic state cultivation (Oct 2026): https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing
- Chemistry with 25–100 logical qubits: https://pubs.acs.org/doi/10.1021/acs.jctc.5c01038
- ML + HPC quantum drug discovery: https://arxiv.org/pdf/2603.17790v1.pdf
- IBM Nov 2025 announcements (Loon, decoding): https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance
- Quantinuum (Oct 2026): https://prnewswire.com/news-releases/quantinuum-breaks-error-correction-world-record-by-10x-validating-its-leading-path-to-fault-tolerant-quantum-computing-by-2029-302912631.html
- Majorana 1 critique: https://theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims

**Infrastructure & energy**
- NVIDIA NVQLink: https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing
- NVIDIA CUDA-Q Logical (Sep 2026): https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Expands-Open-Source-CUDA-Q-Platform-for-Fault-Tolerant-Quantum-Computing
- Qblox + NVQLink: https://thequantuminsider.com/2026/10/22/qblox-hybrid-quantum-computing-nvidia-dgx-spark-nvqlink
- NVIDIA/Jülich 104-qubit simulation: https://quantumcomputingreport.com/nvidia-and-julich-run-104-qubit-magic-state-cultivation-simulation-on-jupiter-supercomputer
- IEA, Key Questions on Energy and AI: https://iea.org/reports/key-questions-on-energy-and-ai/executive-summary

**Security**
- Gidney, "How to factor 2048 bit RSA integers with less than a million noisy qubits": https://arxiv.org/abs/2505.15917
- Global Risk Institute Quantum Threat Timeline 2025: https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b
- NIST IR 8547 explainer (secondary): https://quantumsecuritydefence.com/insights/nist-ir-8547-transition-timeline
- PQC standards index (secondary): https://pqaudit.org
- NSA PQC hub: https://nsa.gov/Cybersecurity/Post-Quantum-Cryptography-Resource-Hub/Article-Display/Article/4616296/post-quantum-cryptography-a-digital-armor
- CSA note on GPT-6 Astra (vendor-reported figures): https://labs.cloudsecurityalliance.org/research/csa-research-note-gpt6-astra-autonomous-zeroday-exploitation
- Multi-step cyber-attack evals: https://arxiv.org/pdf/2603.11214v1.pdf ; ZeroDayBench: https://arxiv.org/pdf/2603.02297v1.pdf

*Not verified / deliberately excluded:* the "Willow-Alpha" catalyst article (syncflo.xyz); exact AlphaQubit percentage improvements; final NIST IR 8547 dates (recalled from draft).
