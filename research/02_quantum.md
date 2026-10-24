# 02 — Quantum Computing: Fundamentals, Hardware, State of Play, Timelines (as of late Oct 2026)

> Confidence legend: **[P]** primary source (company/agency/journal), **[S]** secondary/press/blog (treat as less reliable), **[V]** vendor claim not independently verified, **[BG]** standard textbook background (no specific citation). Many 2026 items below come from press releases and trade press; I could not independently verify them.

---

## 1. Fundamentals (textbook background [BG])

- **Qubit**: a two-level quantum system. Its state is a|0⟩ + b|1⟩ with complex amplitudes, |a|²+|b|²=1. Measurement returns 0 or 1 with probabilities |a|², |b|².
- **Superposition**: n qubits carry 2ⁿ amplitudes. This is *not* "trying all answers at once". Useful algorithms use **interference** to boost the amplitudes of correct answers. You only read out n classical bits, so the speedup comes from structure in the problem.
- **Entanglement**: joint states that can't be written as a product of single-qubit states. They give correlations with no classical analogue, and they are a resource the algorithms consume.
- **Gates**: unitary operations. Single-qubit gates (H, X, Z, S, T, rotations) plus a two-qubit entangler (CNOT/CZ) are universal. Clifford gates are easy to simulate classically. Non-Clifford gates (T/Toffoli) are what make circuits hard to simulate, and they dominate fault-tolerant cost.
- **Noise/decoherence**: physical gates today fail about 1 in 10² to 1 in 10⁴ operations. Useful algorithms need about 10⁹–10¹² reliable operations. That gap is why **quantum error correction (QEC)** is the central problem. It encodes one *logical* qubit in many *physical* qubits and repeatedly measures error syndromes. It works only if physical error is below a code-dependent *threshold* (about 1% for the surface code).
- **Key metrics**: two-qubit gate fidelity, coherence time, connectivity, gate speed, and the logical error rate per cycle. Raw physical-qubit counts are the least informative number.

## 2. Hardware modalities

| Modality | Strengths | Weaknesses | Players |
|---|---|---|---|
| Superconducting | Fast gates (ns–µs), mature chip fabrication | Needs a dilution fridge (~15 mK), fixed 2D connectivity, wiring/scaling | IBM, Google, Rigetti, (IQM, Alice&Bob etc.) |
| Trapped ion | Highest fidelities, all-to-all connectivity (QCCD shuttling), long coherence | Slow gates (µs–ms), harder to scale | Quantinuum, IonQ |
| Neutral atom | Large arrays (thousands of atoms), reconfigurable via optical tweezers | Slow cycle times, atom loss, mid-circuit readout is hard | QuEra, Atom Computing, Pasqal, Infleqtion, (Google program, see §3) |
| Photonic | Room-temp components, uses chip foundries, networking-friendly | Photon loss, probabilistic gates, needs huge component counts | PsiQuantum, Xanadu, Quandela |
| Topological (Majorana) | In theory built-in error protection | Not yet convincingly demonstrated (see §3.5) | Microsoft |
| Annealing (not gate-model) | 4,400+ qubits, commercially sold | Only for optimization/sampling, no universal computation | D-Wave |
| Spin/silicon | CMOS-compatible | Early | Diraq, Intel |

## 3. Current state by company (newest first within each entry)

### 3.1 Google Quantum AI (superconducting)
- **Willow**, 105 qubits, announced Dec 2024. In *Nature* ("Quantum error correction below the surface code threshold") a surface-code memory showed exponential suppression: logical error fell by a factor Λ≈2.14 for each step of code distance (3→5→7). At distance 7 (101 physical qubits) the logical error was 0.143% per cycle, and the logical qubit outlived the best physical qubit by 2.4×. [P: nature.com/articles/s41586-024-08449-y; summary in S: ajayk.sh]
- **Quantum Echoes (OTOC)**, *Nature*, 22 Oct 2025: Google claims the first **verifiable** quantum advantage, running ~13,000× faster than the best classical supercomputer algorithm for that task. It also showed a proof-of-principle NMR-related molecular-structure application. [P: research.google/blog/a-verifiable-quantum-advantage] The task is a physics benchmark, not a commercially useful computation.
- Mar 2026: Google set a **2029 deadline for its own PQC migration** citing hardware and QEC progress and falling cryptanalysis cost estimates. [P: blog.google/…/cryptography-migration-timeline]
- Mar 2026: Google hired Adam Kaufman (JILA) to lead a **neutral-atom program** aiming for "thousands or tens of thousands" of qubits as a second modality. [S: ajayk.sh, citing colorado.edu/jila]
- A Sept 2026 blog review found no 2026 Google announcement of a long-lived logical qubit; Google's own milestone page had not advanced past Milestone 2. [S, single blog; treat with caution]

### 3.2 IBM (superconducting)
- **Nov 12 2025**: *Nighthawk* (120 qubits, 218 tunable couplers, square lattice, up to 5,000 two-qubit gates per circuit, targeting 7,500 in 2026, 10,000 in 2027, and 15,000 gates on 1,000+ connected qubits by 2028). *Loon* demonstrates all the hardware elements needed for fault tolerance. Real-time qLDPC decoding was 10× faster than the prior leading approach, finished a year early. Chip fab moved to 300 mm wafers in Albany. [P: newsroom.ibm.com 2025-11-12]
- **Jun 2 2026**: IBM committed **more than $10 billion over five years** to quantum (R&D, capex, manufacturing, ecosystem, M&A). [P: newsroom.ibm.com 2026-06-02]
- **Jul 30 2026**: IBM + Univ. of Chicago ran **70 logical qubits** (2,415 logical two-qubit gates, 468 logical T gates) in a verifiable random-circuit-style sampling task. IBM says it ran in about 15 minutes, with logical error rates 10× below physical. IBM's Gambetta: "We are now firmly in the quantum advantage era." [P: newsroom.ibm.com 2026-07-30] This is an IBM claim. The task is a sampling benchmark, and classical-spoofing rebuttals have historically followed such claims (see §8).
- **Aug 19 2026**: two cryogenic modules joined and cooled in one environment, a step toward modular systems. [P: newsroom.ibm.com 2026-08-19]
- **Roadmap** (IBM Technology Atlas): 2026 first community-confirmed advantage; *Kookaburra* (2026) as first fault-tolerant module; *Cockatoo* (2027); **Starling, 2029: ~200 logical qubits, 100 million logical gates**, in Poughkeepsie. Later: *Blue Jay* (~2,000 logical qubits, 1B gates, 2033+). [P: ibm.com/roadmaps/quantum; June 2025 announcement via S: postquantum.com]
- Selected for DARPA QBI Stage C (Oct 2026).

### 3.3 Quantinuum (trapped ion, Nasdaq: QNT)
- **Helios** (commercial Nov 2025): 98 barium-137 qubits, QCCD architecture. Typical 2Q fidelity ≈99.92% (infidelity ~8×10⁻⁴), 1Q 99.9975%. Reported **48 error-corrected logical qubits** (~2:1 encoding, per the [S] qbitcount/hpcwire accounts) and 94 error-detected logical qubits. [S: hpcwire.com 2025-11-05; qbitcount.com]
- Sep 2026: "Helix" fault-tolerant architecture shown on Helios (logical memory, logical Clifford operations, logical entanglement across codes). Quantinuum's CEO stressed that "fault-tolerant means you are error-correcting, not detecting, not mitigating". [S: quantumworldcongress.com]
- **Oct 19 2026**: Quantinuum reports **99.9995% logical fidelity** (≈5 errors per million operations) with a color code on Helios, 10× better than its own Sep 2026 result. It claims this is 100× better than Google's published result on superconducting hardware. [V: PR Newswire; also thequantuminsider.com 2026-10-19] Caveat: this is a logical-memory/primitive result, not a full algorithm at scale, and the comparison is vendor-framed.
- **Roadmap**: Sol (2027), **Apollo, universal fault-tolerant, 2029**; "Lumos", >1 million physical qubits, early 2030s (stated at Quantum World Congress 2026). [S: quantumworldcongress.com] Pending: Sol details not checked.

### 3.4 IonQ (trapped ion, NYSE: IONQ)
- **Oct 21 2025**: **99.99% two-qubit gate fidelity** ("four nines") using Oxford Ionics-derived Electronic Qubit Control (chip-integrated, laser-free). [P: ionq.com/news]
- Aug 2026: IonQ closed its acquisition of **SkyWater Technology** (a chip foundry). It reported Q2 2026 revenue growth of 287% y/y and raised 2026 revenue guidance to **$280–290M**. [P: ionq.com Q2 2026 release] Much of the revenue is acquisition-driven. I did not verify the organic/inorganic split.
- **Sep 8 2026**: **Superion 256** announced, a 256-qubit chip fabricated at SkyWater, with first ions trapped in prototypes and customer deliveries in 2027. [P: ionq.com/news]
- Roadmap claims (earlier IonQ statements, not re-verified this session): ~2 million physical qubits / 80,000 logical qubits by 2030. Treat as aspirational. [V]
- Selected for DARPA QBI Stage C.

### 3.5 Microsoft (topological) and Atom Computing (neutral atom)
- **Majorana 1** (Feb 2025) was announced as the first topological-qubit chip. A *Nature* paper's own peer-review note said the data were not evidence for Majorana zero modes. On **Jun 24 2026**, *Nature* published a formal critique (Henry Legg, St Andrews) arguing the evidence can be explained by trivial phenomena. Microsoft disputes this and published a reply. [S: theverge.com; unbiasedheadlines.com; nature.com/articles/s41586-026-10567-8 (the critique, URL from the Verge article)]
- **Majorana 2** (Jun 2 2026): Microsoft claims a new materials stack gives 1,000× better reliability, a mean qubit "lifetime" of 20 s (up to 1 min), 1 µs operations, and a scalable machine by **2029** ("cutting its original timeline in half"). [P: news.microsoft.com] **Flag**: the "lifetime" metric is a Microsoft-defined parity-type lifetime. It is not a gate fidelity or a demonstrated logical qubit. Independent replication was lacking in what I found.
- **Magne** (Denmark, QuNorth, built by Microsoft + Atom Computing): ~1,225 physical neutral-atom qubits targeting **50 logical qubits**, funded with €80M by EIFO and the Novo Nordisk Foundation, operational ~early/spring 2027. [S: quantumcomputingreport.com; thequantumcomputer.com] It is under construction, not delivered.
- Microsoft/Atom earlier (Nov 2024) reported 24 entangled logical qubits. [P: Azure blog, URL linked in Microsoft insights page]
- Microsoft and PsiQuantum went straight to DARPA QBI Stage C via the earlier US2QC program; Atom Computing is also in Stage C.

### 3.6 PsiQuantum (photonic)
- Raised **$1B Series E** in 2025 at a ~$7B valuation (>$3B total raised). Building utility-scale sites in **Chicago** (Illinois Quantum and Microelectronics Park) and **Brisbane/Queensland**, with the Brisbane site moved to Moreton Bay Central. Goal: a ~1-million-qubit-class fault-tolerant machine, with chips made at GlobalFoundries. [S: entangledfuture.com; ia.acs.org.au; gophotonics.com] **No fault-tolerant demonstration yet**. The stated targets are about 2027–2029 and are aspirational.

### 3.7 Neutral-atom leaders: QuEra / Harvard / MIT, Infleqtion
- **Sep 2025** (*Nature*): continuous operation of a **3,000-qubit** array for hours, with atom replenishment. [P/S: phys.org; postquantum.com]
- **Nov 2025** (*Nature*): Harvard/QuEra **448-atom** fault-tolerant architecture, with errors detected and removed below a fault-tolerance threshold. [S: phys.org; arXiv 2506.20661]
- QuEra raised >$230M (Dec 2025). [P: quera.com press release]. A Jan 2026 *Nature* result of ~96 logical qubits is referenced in one aggregator only and is unverified here. [S: quantumnews.in]
- **Sep 24 2026**: Infleqtion entangled **30 logical qubits from 80 physical atoms**. Trade press notes that this relies on **error detection** (not full correction). [V/S: infleqtion.com; postquantum.com]

### 3.8 Rigetti (superconducting)
- Jan 2026: delayed 108-qubit Cepheus-1-108Q. **Apr 7 2026**: general availability (on Rigetti QCS and Amazon Braket). [P: investors.rigetti.com] Fidelity of the 108-qubit system in the 99.5% range per past roadmap statements (not re-verified). Small-scale, no QEC milestone.

### 3.9 D-Wave (annealing → gate model)
- **Mar 2025** (*Science*): claimed "quantum supremacy" on a materials-simulation problem with a 5,000+ qubit annealer. Subsequent tensor-network and other classical rebuttals attempted to match it (see §8). [S: postquantum.com; arXiv 2603.18825 review]
- Jan 20 2026: bought **Quantum Circuits** (dual-rail superconducting, gate-model) for $550M ($250M cash + $300M stock). Roadmap: dual-rail to **100 logical qubits by end-2032**. [S: quantum-data.com; note.com]
- Q1 2026: revenue **$2.9M (−81% y/y)** but record bookings of $33.4M, driven mainly by a **$20M** Advantage2 sale to Florida Atlantic University. [S: quantum-data.com; longyield.substack.com]. This shows how lumpy and small the real quantum revenue is.

### 3.10 Government validation: DARPA QBI
- Goal: determine whether **utility-scale** quantum computing (value > cost) is achievable **by 2033**. Stage B selected 11 companies (Nov 6 2025). **Oct 7 2026**: Stage C adds Atom Computing, Diraq, IBM, IonQ, joining Microsoft and PsiQuantum (the Xanadu-related news on Oct 19 describes six "final test" participants. I did not reconcile this and Quantinuum/Google status is not confirmed here). DARPA's managing director: "we increasingly expect that someone will build a utility-scale quantum computer by 2033." [P: darpa.mil/news/2026/four-more-teams…; darpa.mil stage-b-selection]

## 4. Error correction & logical-qubit milestones (timeline)

| Date | Milestone | Source type |
|---|---|---|
| Dec 2024 | Google Willow: below-threshold surface code, d=7, Λ≈2.14, 0.143%/cycle | P |
| Nov 2024 | Microsoft+Atom: 24 entangled logical qubits (neutral atoms) | P |
| Sep–Nov 2025 | Harvard/QuEra 3,000-qubit continuous operation; 448-atom fault-tolerant architecture | P/S |
| Nov 2025 | Quantinuum Helios: 48 error-corrected / 94 error-detected logical qubits | S/V |
| Nov 2025 | IBM Loon (all FT hardware elements), qLDPC decoder 10× faster | P |
| Jul 2026 | IBM/UChicago: 70 logical qubits, 2,415 logical 2Q gates, 468 logical T gates | P (vendor) |
| Sep 2026 | Infleqtion: 30 logical qubits / 80 atoms (error-detected) | V |
| Oct 2026 | Quantinuum: 99.9995% logical fidelity (color code, Helios) | V |

**Honest read**: the field has gone from "can logical error go down?" (2023–24) to dozens of logical qubits and logical fidelities near 10⁻⁵–10⁻⁶ per operation on small codes. It has **not** yet shown the ~100–1,000+ logical qubits at ~10⁻⁹–10⁻¹² error for ≥10⁸–10⁹ gates that Shor on RSA/ECC or industrially valuable chemistry needs. "Logical qubit" counts are not comparable across vendors. Codes, error detection vs correction, post-selection, and encoding overhead differ.

## 5. Roadmaps and honest timelines to fault tolerance

| Vendor | Stated FT target | Notes |
|---|---|---|
| IBM | Starling 2029 (200 logical qubits, 10⁸ gates); Blue Jay 2033+ | Modular qLDPC; 2026 deliverables still being met per IBM |
| Quantinuum | Apollo 2029; Lumos early 2030s (>1M physical qubits) | Public company now; vendor-reported |
| Microsoft | "Scalable quantum computer" 2029 (stated Jun 2026) | Topological science disputed; Magne (neutral atom, 50 logical qubits) 2027 is the nearer-term deliverable |
| Google | Previously ~2029 for "useful, error-corrected" machine; no new 2026 FT date found | Moved PQC deadline to 2029 |
| IonQ | Aggressive: ~2M physical qubits by 2030 [V, not re-verified] | Superion 256 deliveries 2027 |
| PsiQuantum | Utility-scale sites in Chicago/Brisbane, late 2020s | No demos at scale yet |
| D-Wave (gate model) | 100 logical qubits by end-2032 | Conservative relative to others |
| DARPA QBI | Utility-scale **by 2033** is being tested | Government is hedged: evaluating, not guaranteeing |

**Synthesis (my judgment)**: many credible players now cluster on **2029** for first small-to-mid-scale fault-tolerant machines. These will have hundreds of logical qubits at best and are likely too small for RSA-2048. Cryptographically relevant machines are plausibly in the **early-to-mid 2030s**, with wide uncertainty. Timelines have pulled in over 2025–26, but roadmap dates have historically slipped (e.g., Rigetti's 108-qubit delay in Jan 2026). Treat 2029 as "target if everything works", not a forecast.

## 6. Key algorithms and what they need

| Algorithm | Speedup | Status / resource note |
|---|---|---|
| **Shor** (factoring, discrete log) | Superpolynomial (exponential-ish) vs best known classical | Breaks RSA/ECC/DH. Gidney (Google, May 2025): RSA-2048 in under a week with **<1 million noisy qubits** (vs 20M in 2019 estimate), ~100× fewer than before [P: arXiv 2505.15917]. Google Mar 2026: **ECDLP-256 (secp256k1) in ≤1,200–1,450 logical qubits, 70–90M Toffoli gates, <500,000 physical qubits**, minutes of runtime on superconducting assumptions (10⁻³ physical error rate) [S: postquantum.com; P: quantumai.google cryptocurrency whitepaper]. Google withheld circuits and published a zero-knowledge proof of the claims. An IonQ-adjacent preprint (arXiv 2609.05625, unverified/unreviewed) estimates 256-bit ECDLP in 26 days on a 20,000-qubit trapped-ion design [S]. Largest *honest* Shor demos remain toy-sized. |
| **Grover** (search) | Quadratic (√N) | Provable but modest. Halves effective symmetric key length (AES-256 stays safe). Overheads of error correction often erase the advantage for practical sizes. |
| **Quantum simulation** (Hamiltonian, chemistry/materials) | Potentially exponential for some systems | The most credible long-term commercial use. Needs fault tolerance for strongly correlated molecules. Classical methods (DMRG, tensor networks, neural states) keep eroding "advantage" claims; active research disputes where quantum advantage in chemistry will genuinely appear [S: arXiv 2603.28648]. |
| **VQE / QAOA** (variational) | No proven speedup | NISQ-era hybrid heuristics. Hit barren plateaus and noise limits, and no clear evidence of practical advantage over classical optimization. |
| **HHL / quantum linear algebra** | Exponential *under strong caveats* | Needs efficient state loading (qRAM) and only returns global properties of the solution. "Dequantization" results weakened many ML claims. Not a practical near-term tool. |
| **Quantum phase estimation / QSVT** | Core subroutines | Underpin chemistry and many FT algorithms. |

## 7. Post-quantum cryptography (PQC) status

- **NIST standards finalized 13 Aug 2024**: FIPS 203 (ML-KEM, key encapsulation), FIPS 204 (ML-DSA, signatures), FIPS 205 (SLH-DSA, hash-based signatures). **HQC** was selected Mar 2025 as a backup KEM (draft expected). **FIPS 206 (FN-DSA/Falcon)** was still pending/expected in 2026 per the sources I found; verify current status before publishing. [P/S: nist.gov; czinda.io; pqaudit.org]
- **NIST IR 8547 (draft)**: deprecate RSA/ECC at 112-bit security after **2030**, disallow after **2035**. [P: csrc.nist.gov/pubs/ir/8547/ipd]
- **Deployment**: hybrid X25519MLKEM768 is on by default in major browsers; Cloudflare reported **over two-thirds** (~70%) of human browser traffic post-quantum protected in 2026. [S: myssl.info; encryptionconsulting.com; shattered.io]. This covers key exchange (the *harvest-now-decrypt-later* risk). **Certificates/signatures lag**.
- **Google moved its own migration deadline to 2029** (Mar 25 2026), 6 years ahead of the NIST 2035 backstop. [P: blog.google]
- Symmetric crypto (AES-256) and hashes are considered fine against known quantum attacks.
- Crypto-assets: Bitcoin/Ethereum signatures are ECDLP-based, so the Google Mar 2026 paper adds urgency, but no CRQC exists today.

## 8. Limits and hype (read this before writing marketing copy)

1. **"Advantage" claims keep being contested.** Random circuit sampling, OTOC, and D-Wave annealing results all drew classical-simulation counters (tensor networks, etc.). A 2026 review of IBM, D-Wave, and Google advantage experiments examined exactly where classical methods caught up. [S: arXiv 2603.18825] IBM now runs a public "Quantum Advantage Tracker" for adjudicating claims. Advantages shown so far are on **contrived or physics-benchmark tasks**, not business workloads.
2. **No commercially useful quantum advantage has been conclusively demonstrated** for a real-world business problem. (My conclusion based on the sources; vendors assert the contrary for some narrow cases.)
3. **Logical-qubit counts are slippery**: detection vs correction, post-selection, code distance, and overhead (2:1 vs 100s:1) differ.
4. **Business reality**: D-Wave Q1 2026 revenue $2.9M; IonQ's growth is largely acquisitions (SkyWater, Oxford Ionics). Valuations are far above revenue. Many quantum equities are volatile.
5. **Data loading and I/O bottleneck**: quantum computers are poor at big-data problems. Loading classical data can erase speedups, which matters for any "quantum for AI/ML" pitch.
6. **Roadmap risk**: delays are common; 2029 targets assume engineering (cryogenics, wiring, decoders, yield, manufacturing) scales as planned.
7. **Not a general accelerator**: no known exponential speedup for most optimization, NP-complete problems, or deep-learning training.
8. **Source-quality warning**: much 2026 coverage is press-release echo or aggregator content. Prefer the primary sources below.

## 9. Open items / uncertainty flagged
- Quantinuum Apollo/Sol details, Google's current FT roadmap, and IonQ's 2030 targets were not re-verified this session.
- QuEra "96 logical qubits (Jan 2026)" appears only in an aggregator. Not confirmed.
- DARPA QBI: full Stage C roster incl. Quantinuum/Google/QuEra status not confirmed. The Oct 2026 techtimes piece says "six rivals" are in the final stage.
- FIPS 206 (FN-DSA) and HQC draft publication status should be re-checked at csrc.nist.gov.

---

## Sources (URLs retrieved during research)

**Primary / near-primary**
- IBM roadmap: https://ibm.com/roadmaps/quantum and https://ibm.com/roadmaps/quantum/2026
- IBM Nov 12 2025 (Nighthawk, Loon): https://newsroom.ibm.com/2025-11-12-ibm-delivers-new-quantum-processors,-software,-and-algorithm-breakthroughs-on-path-to-advantage-and-fault-tolerance
- IBM $10B commitment (Jun 2 2026): https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers
- IBM/UChicago 70 logical qubits (Jul 30 2026): https://newsroom.ibm.com/2026-07-30-ibm-and-the-university-of-chicago-demonstrate-quantum-advantage,-establishing-trusted-quantum-computation-on-logical-circuits
- IBM modular cryogenic systems (Aug 19 2026): https://newsroom.ibm.com/2026-08-19-ibm-connects-its-first-modular-cryogenic-systems-in-milestone-toward-fault-tolerant-quantum-computing
- Google Quantum Echoes: https://research.google/blog/a-verifiable-quantum-advantage
- Google Willow QEC (Nature): https://www.nature.com/articles/s41586-024-08449-y
- Google PQC 2029 timeline: https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline
- Google ECC whitepaper: https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf (arXiv https://arxiv.org/pdf/2603.28846)
- Gidney RSA-2048: https://arxiv.org/pdf/2505.15917.pdf
- Quantinuum (Oct 19 2026): https://www.prnewswire.com/news-releases/quantinuum-breaks-error-correction-world-record-by-10x-validating-its-leading-path-to-fault-tolerant-quantum-computing-by-2029-302912556.html
- IonQ 99.99%: https://ionq.com/news/ionq-achieves-landmark-result-setting-new-world-record-in-quantum-computing
- IonQ Superion 256: https://ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing
- IonQ Q2 2026: https://ionq.com/news/ionq-announces-record-second-quarter-2026-revenues-growing-287-yoy
- Microsoft Majorana 2: https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai
- Majorana critique (Nature): https://www.nature.com/articles/s41586-026-10567-8
- Rigetti GA: https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system
- D-Wave Q1 2026: https://dwavequantum.com/company/newsroom/press-release/d-wave-reports-first-quarter-2026-results
- QuEra 2025 review: https://quera.com/press-releases/quera-computing-marks-record-2025-as-the-year-of-fault-tolerance-and-over-230m-of-new-capital-to-accelerate-industrial-deployment
- Harvard 448-atom arXiv: https://arxiv.org/pdf/2506.20661
- Infleqtion 30 logical qubits: https://infleqtion.com/infleqtion-achieves-30-entangled-logical-qubits-on-its-sqale-quantum-computer
- DARPA QBI: https://darpa.mil/research/programs/quantum-benchmarking-initiative ; Stage B: https://darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection ; Stage C (Oct 7 2026): https://darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage
- NIST IR 8547: https://csrc.nist.gov/pubs/ir/8547/ipd

**Secondary (use with caution)**
- Quantinuum at Quantum World Congress 2026 (Helix/Lumos): https://quantumworldcongress.com/news/quantinuums-next-quantum-milestone-is-not-just-a-bigger-computer-it-is-a-computing-era
- Quantinuum Helios launch: https://hpcwire.com/2025/11/05/quantinuum-introduces-helios-quantum-system-as-roadmap-advances-toward-apollo ; https://qbitcount.com/history/2025-quantinuum-helios.html
- Google ECC analysis: https://postquantum.com/security-pqc/google-quantum-bitcoin-ecdlp
- Trapped-ion ECDLP preprint: https://arxiv.org/html/2609.05625v1
- Majorana dispute: https://theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims
- Magne: https://quantumcomputingreport.com/denmarks-qunorth-to-acquire-50-logical-qubit-magne-quantum-computer-from-atom-computing-and-microsoft
- PsiQuantum: https://entangledfuture.com/company/psiquantum ; https://ia.acs.org.au/article/2026/psiquantum-changes-location-for--1bn-quantum-build.html
- Harvard/MIT 3,000 qubits: https://postquantum.com/quantum-research/harvard-mit-continuous-3000-qubit
- D-Wave supremacy claim: https://postquantum.com/industry-news/d-wave-quantum-advantage ; Q1 2026: https://quantum-data.com/events/2026-05-12-d-wave-q1-2026-earnings-quantum-circuits-dual-rail-roadmap
- Tensor-network critique of advantage claims: https://arxiv.org/html/2603.18825v2
- Chemistry advantage skepticism: https://arxiv.org/html/2603.28648
- 2026 hardware review blog: https://ajayk.sh/blog/quantum-computing-hardware-error-correction-2026
- PQC deployment / status: https://myssl.info/learn/post-quantum-tls ; https://czinda.io/posts/state-of-pqc-may-2026 ; https://pqaudit.org
