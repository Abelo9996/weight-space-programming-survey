# Awesome Weight-Space Programming

A curated, taxonomy-organized list of research on **weight-space programming (WSP)**: a model, usually an LLM, reads, writes or edits the weights of a neural network directly, without an optimizer authoring the values.

Companion to *Weight-Space Programming: A Survey and Roadmap* (Yagubyan, University of Georgia, 2026). Every entry below was read in full or partially (marked) for the survey. One-line summaries are neutral descriptions, not rankings.

> Literature cut-off: 2026-11-25. Contributions welcome via pull request (see bottom).

## Contents
- [Origin](#origin)
- [B1 Reading weights](#b1-reading-weights)
- [B2 Writing networks](#b2-writing-networks)
- [B3 Repairing and editing](#b3-repairing-and-editing)
- [B4 Feedback and search loops](#b4-feedback-and-search-loops)
- [B5 Efficient and non-LLM solvers](#b5-efficient-and-non-llm-solvers)
- [B6 Self-editing](#b6-self-editing)
- [Evaluation, audits and replications](#evaluation-audits-and-replications)
- [Safety and security](#safety-and-security)
- [Verification](#verification)
- [Surveys](#surveys)
- [Foundations and precursors](#foundations-and-precursors)
- [Taxonomy codes](#taxonomy-codes)
- [Citation](#citation)

## Origin
- **Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights**. Takehi, Teoh, Zhang, Khattab (MIT CSAIL). Blog post, 2026-11-02. [[Post](https://rikiyat.github.io/blog/weight-space-programming/)] [[Logs](https://github.com/RikiyaT/lm_understand-logs)]

## B1 Reading weights
*Weights to description: what a network computes, what it was trained on, whether it hides a flaw.*

- **Weight Oracles: Reading Neural Network Weights with Language Models**. Krishna Kabra et al. 2026-10-05. `B1` [[Paper](https://arxiv.org/abs/2610.07334)]  
  A fine-tuned Qwen 2.5 3B reads the raw weights of ~2K-parameter transformers, injected as projected continuous tokens with type embeddings, to simulate their forward pass (Phase I) and to answer...
- **Weight-space programming for auditing clinical decision networks**. Humza Nusrat and Omar Nusrat. 2026-11-03. `B1/B3/B2` [[Paper](https://arxiv.org/abs/2611.05341)] [[Code](https://github.com/hnusrat1/weightspace-rt)]  
  Claude Opus 5.5, with no tools, reads the raw weights of small ReLU clinical screening networks, diagnoses planted flaws against a written protocol, and writes weight edits to repair them.
- **Function-Preserving Audits of Visual Weight Readers**. Sungguk Cha et al. 2026-11-04. `B1` [[Paper](https://arxiv.org/abs/2611.05798)] *(partially read)*  
  Mainly audits learned weight-space readers (HiddenProbe, ProbeGen, set readers) of neural fields under function-preserving weight transformations; includes a 720-response study where LLMs (GPT-6...
- **Weight-Space Programming for THOX Edge Models: Evidence Review, Small-Scale Recreation, and a Signed Patch Channel**. Craig Ross and Tommy Xaypanya. 2026-11-04. `B1/B2/B3` [[Paper](https://doi.org/10.5281/zenodo.23954378)]  
  Industry technical report reviewing the Takehi et al. WSP claims, re-verifying the released Qwen3.5-0.8B edit, running small-scale read/write/fix/audit recreations with deterministic tools (not an...
- **Verified by Construction: Machine-Checked Proofs for Hand-Written Transformer Circuits and Their Composition**. Xintian Huang. 2026-11-05. `B1/B2/B3` [[Paper](https://doi.org/10.5281/zenodo.23976715)]  
  Gives Lean 4 machine-checked correctness proofs for agent-written transformer weight programs from a WSP study (Singh, 2026) and proves a grafting theorem for hand-written circuits appended to...
- **Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"**. Nazmus Sakib Ahmed. 2026-11-05. `B1` [[Paper](https://arxiv.org/abs/2611.08070)] [[Code](https://sakibbai.com/posts/2026-11-05-llm-weight-space-programming/)]  
  Audits the reading side of WSP: Claude Opus 5.5 receives all ~125k weights of small CNNs as plain text (no tools, no forward passes) and is asked what dataset/classes they were trained on.
- **Computation, not weight access: large language models as auditors of clinical prediction networks**. Zhiyu Liu and Xinyu Yang. 2026-11-05. `B1/B3` [[Paper](https://arxiv.org/abs/2611.07847)] [[Code](https://github.com/Chth1z/llm-clinical-network-audit)]  
  GPT-6 Astra and other GPT models read (and in one task edit) the weights of small tanh MLP clinical prediction networks, with weights in the prompt or via a calculation-only Python tool, compared...
- **Two language models can read and change neural networks, but reliability depends on the task**. Mutuo Research AI scientist. 2026-11-06. `B1/B2/B3` [[Paper](https://doi.org/10.5281/zenodo.24373915)] [[Code](https://zenodo.org/records/24373916/files/weight-space-bakeoff-v1.zip)]  
  Replicates seven Sparks-of-WSP tasks with GPT-6 Astra and Claude Opus 5.5 reading weights (game, shape, language, copy heads), writing networks (MinAtar, 9x9 Go), and editing weights (car controller,...
- **Can an LLM agent detect and repair a planted shortcut in a genomics CNN without data? A preregistered, blinded test of weight-space programming**. Alexandre Bruni-Cardoso. 2026-11-07. `B1/B3` [[Paper](https://doi.org/10.5281/zenodo.24040591)] [[Code](https://github.com/brunicardoso/weight-space-programming-genomics/tree/v1.0.1)]  
  Claude Opus 5.5 sessions in Claude Code read the weights of a 58k-parameter CTCF-binding CNN to name a planted shortcut with no forward passes, then submit repaired weights with 0 or 50 metered...
- **WeightBench v0: two small instruction models at chance on five weight-reading tasks**. Advatiya Thalluri. 2026-11-08. `B1` [[Paper](https://doi.org/10.5281/zenodo.24047726)] [[Code](https://zenodo.org/records/24047727)] *(partially read)*  
  Pre-registered mini-benchmark asking small open LLMs (Qwen2.5-1.5B/7B-Instruct) to read compressed weight summaries of small MLPs/PPO nets and answer 4-way questions (game, dataset, activation,...
- **Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents**. Yuchen Zeng et al. 2026-11-11. `B1/B3` [[Paper](https://arxiv.org/abs/2611.15118)]  
  The backdoor edits used in all experiments are authored by a closed-form construction (Lazarus-Analytic) optionally refined by SGD on the edited neurons (Lazarus-SGD), not by an LLM; the WSP-relevant...
- **WeightBench: Evaluating Language Models as Weight-Space Programmers**. Aayush Marasini et al. 2026-11-13. `B1/B2/B3/B5` [[Paper](https://arxiv.org/abs/2611.18553)] [[Code](https://github.com/Aayush-Marasini/WeightBench)]  
  Benchmark in which LLM agents read, fix, write, compress weights or refuse infeasible edits of subject networks (2K-param MLPs to 7B LMs) inside an audited sandbox that meters forward passes.
- **A Backdoor Trigger Is Legible in Fine-Tune Weights**. Snigdha Chandan Khilar. 2026-11-14. `B1/B5` [[Paper](https://arxiv.org/abs/2611.19304)] [[Code](https://github.com/nssprogrammer/wsp_backdoor)]  
  No LLM editor: a hand-designed static statistic reads a fine-tuned checkpoint's weight delta (vs base, standardised against clean fine-tunes) to name a backdoor trigger token without running the...
- **Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws**. Zhiyu Liu and Xinyu Yang. 2026-11-18. `B1` [[Paper](https://arxiv.org/abs/2611.24877)] [[Code](https://github.com/Chth1z/llm-black-box-model-audit)]  
  GPT-6 Astra audits trained clinical models (incl. neural networks) by querying predictions through a NumPy calculator tool, writing a surrogate and a list of flaws; weights are not given except in a...
- **Reading, Writing and Repairing Game-Theoretic Policies in Weight Space**. Ancil Crayton. 2026-11-24. `B1/B2/B3` [[Paper](https://arxiv.org/abs/2611.31979)]  
  An LLM (deepseek-v4.1-flash-1017, no tools, no feedback) reads the raw weights of 1,218-weight Elman RNN policies to report behavior or recover the state machine, writes policy weights from an...

## B2 Writing networks
*Specification to weights, from scratch.*

- **Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application**. Renan Butkeraites. 2026-11-06. `B2/B4` [[Paper](https://arxiv.org/abs/2611.09559)] [[Code](https://github.com/butkeraites/llm-written-weights-or)]  
  An LLM (Claude Opus 5.5 in Claude Code) writes the weights of small MLP scoring networks (JSON, each weight justified) for column generation and SCIP branching, reading forward-pass diagnostics and...
- **Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games**. Eduardo C. Garrido Merchán. 2026-11-06. `B2` [[Paper](https://arxiv.org/abs/2611.09271)]  
  An LLM (Claude Sonnet 5, plus other models in replications) writes every weight of feed-forward game-playing networks from the rules, with no gradient descent or training data, and the networks are...
- **Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models**. Shogo Sato et al. 2026-11-07. `B2/B4` [[Paper](https://arxiv.org/abs/2611.12954)]  
  Claude Opus 5.5 writes (and optionally restructures) a small NN's architecture and weights as JSON from a PDE specification, then refines the weights from external physics-loss feedback, with no...
- **Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer**. Debarshi Kundu et al. 2026-11-08. `B2` [[Paper](https://arxiv.org/abs/2611.11537)] [[Code](https://github.com/DebarshiKunduPSU/Quantum-Weight-Space-Programming)]  
  GPT-6 Astra writes the gate angles (and in one setting the circuit itself) of variational quantum circuits directly from a problem description, with no loss, gradient or accuracy feedback.
- **Weight-Space Programming of Policies and Their Verification via Model Checking**. Dennis Gross. 2026-11-08. `B2/B4` [[Paper](https://arxiv.org/abs/2611.11604)] [[Code](https://github.com/LAVA-LAB/COOL-MC/tree/wsp_verified)]  
  An LLM writes all weights of a small ReLU policy network as numbers from a PRISM MDP and PCTL property, then edits them using dataset and Storm model-checking feedback, with no gradient descent.
- **Weight-Space Programming for Medical Imaging: Do We Still Need Training Data?**. Maximilian Lindholz et al. 2026-11-09. `B2` [[Paper](https://arxiv.org/abs/2611.12066)] [[Code](https://github.com/MaximilianLindholz/weight-space-programming-medical)]  
  Claude Opus 5.5 and GPT-6 Astra each write every weight of a small LeNet-style CNN from a natural-language task description in a single tool-free reply, with no images or training.
- **Mixed Signals: Weight-Space Programming for EEG and ECG**. Dara Varam et al. 2026-11-10. `B2/B3/B1/B4` [[Paper](https://arxiv.org/abs/2611.13758)]  
  Three LLMs (Opus 5.5, GLM-5.3, DeepSeek-V4.1-Flash) read, improve, repair, debug, and write from zero the weights of EEG and ECG classifiers via a Python session, with gradient descent and iterative...
- **Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games**. Jens Lehmann. 2026-11-12. `B2/B4` [[Paper](https://arxiv.org/abs/2611.16981)]  
  Nine frontier LLM 'writers' read a game's mechanics-only simulator source and directly set all weights of a fixed 57k-parameter recurrent conv actor (or design and set their own network in a tensor...
- **Programming Quantum Circuit Parameters with Large Language Models**. Tiago de Souza Farias et al. 2026-11-12. `B2/B4/B1` [[Paper](https://arxiv.org/abs/2611.17246)] [[Code](https://github.com/tiago939/NeuralOptimizer)] *(partially read)*  
  Frozen GPT-6 Astra writes complete parameter vectors for fixed variational quantum circuits from OpenQASM 3 and Pauli-Hamiltonian descriptions, optionally refining with energy feedback; framed as...
- **Interpretable weight-space programming builds transparent transformers and brain encoding models**. Yash Mehta et al. 2026-11-13. `B2/B4` [[Paper](https://arxiv.org/abs/2611.18114)]  
  A Claude Code (or Gemini) agent writes every weight of small transformers, and hand-crafted feature networks for brain encoding, directly in code with training forbidden, iterating on a fixed...
- **Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets**. Eduardo C. Garrido Merchán. 2026-11-14. `B2` [[Paper](https://arxiv.org/abs/2611.19292)]  
  An LLM (Claude Opus 5, plus Sonnet 5, Haiku 4.5, Grok 4.7) reads a full small tabular dataset in context and writes every weight and bias of a linear or 8-unit ReLU MLP as literal numbers, with no...
- **Weights & Caches: LLMs Can Program Tabular Foundation Models**. Shi Bin Hoo et al. 2026-11-15. `B2/B3/B1` [[Paper](https://arxiv.org/abs/2611.20174)] [[Code](https://github.com/automl/TFM-Playground/)]  
  GPT-6 Astra writes nanoTabPFN weights from zero, edits pretrained TabPFN-3.5 weights to repair a signed-product regression failure, and writes KV-cache editing programs, all without gradient...
- **Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers**. Roksana Goworek et al. 2026-11-16. `B2/B1` [[Paper](https://arxiv.org/abs/2611.21449)]  
  Replication of Takehi et al.: GPT-6 Astra and other LLMs write MinAtar/MNIST network weights in one tool-free reply, read raw weights to name games, decompile written networks into Python, and audit...
- **Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor**. Timo Oksanen. 2026-11-16. `B2/B3/B4/B1` [[Paper](https://arxiv.org/abs/2611.21958)]  
  GPT-6 Astra and Claude Fable 5.1 (no tools, text only) read a 253-weight steering network as JSON and write new weight values, both repairing a PPO-trained network for a slower actuator and writing a...
- **Weight-Space Programming Doesn't Need Transformers**. Hyunjong Ok and Jaeho Lee. 2026-11-17. `B2/B4/B3` [[Paper](https://arxiv.org/abs/2611.22055)]  
  Three frontier LLMs ('writers') write every weight of target models without gradients, either into fixed released architectures/given Transformers or into architectures they design themselves (sparse...
- **Weight-Space Programming for Materials Science**. Sk Md Ahnaf Akif Alvi and Raymundo Arróyave. 2026-11-17. `B2/B1/B3/B4` [[Paper](https://arxiv.org/abs/2611.22013)] [[Code](https://github.com/sheikhahnaf/weightspace-programming-for-material-science)]  
  Claude Opus 5.5, Fable 5.2, Sonnet 5.5 and Haiku 5.5 each write every weight of a zero-initialized 16-hidden-unit MLP as text from a task description and named inputs, with no labels, tools or code;...
- **Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models**. Konstantinos Skianis and Aristidis Likas. 2026-11-19. `B2/B3/B4` [[Paper](https://arxiv.org/abs/2611.26841)] [[Code](https://github.com/y3nk0/weight-space-programming-study)] *(partially read)*  
  Frontier LLM editors in a Python kernel read and overwrite parameters of a smaller LM (no gradients, <=50 executions) so it performs a task zero-shot that it previously did only with 16 in-context...

## B3 Repairing and editing
*Changing a trained network to fix, alter or implant behavior.*

- **IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection**. Chris von Csefalvay et al. 2026-11-05. `B3/B4` [[Paper](https://arxiv.org/abs/2611.08647)] [[Code](https://github.com/hcltech-robotics/iwibench)]  
  Frontier LLM editors use four read/write/run/inspect tools to patch the weights of Gemma 3 4B IT, without gradients or code execution, to achieve ten behavioral editing objectives.
- **Weight-Space Programming on Qwen3-ASR-0.6B: Nine Independent Agent Edits, Random-Direction Controls, and a Missing Attention Mask**. Taha Enes Aslantürk. 2026-11-05. `B3/B4` [[Paper](https://doi.org/10.5281/zenodo.23976684)] [[Code](https://huggingface.co/tahaenesaslanturk/Qwen3-ASR-0.6B-weight-space-programming)]  
  Claude Opus 5.5 agent arms read Qwen3-ASR-0.6B weights and derive analytic edits (head gains, rank-1 removals, k_proj terms) with no gradients, under 10/25/50 forward-pass budgets, to fix a...
- **A published change to a small language model's weights leaves its default-mode math accuracy unchanged**. Mutuo Research AI scientist. 2026-11-06. `B3/B1/B2` [[Paper](https://doi.org/10.5281/zenodo.24373917)] [[Code](https://mutuo-research.vercel.app/papers/weight-space-programming/v1/)]  
  Re-evaluates the published GPT-6 Astra weight edit to Qwen3.5-0.8B (rebuilt bit-for-bit) in the model's default non-thinking mode, and rechecks other Takehi et al. experiments (network writing,...
- **Can LLMs Debug Robots by Editing Their Weights?**. Jusheng Zhang et al. 2026-11-06. `B3/B4` [[Paper](https://arxiv.org/abs/2611.09376)] *(partially read)*  
  GPT-6 Astra reads robot policy weights in a CPU Python workspace and writes replacement tensors (65 token-embedding rows of pi0.5), guided by budgeted simulator rollouts, with gradient updates...
- **Weight-Space Programming with Claude Mythos: Weight Edits and Implanted Circuits in a 0.8B Language Model, with Transfer to an Engineering Surrogate**. Keyvan Hardani. 2026-11-07. `B3/B2/B4` [[Paper](https://doi.org/10.5281/zenodo.24036186)] [[Code](https://huggingface.co/keyvan-ai/Mythos-WSP-Qwen3.5-0.8B)]  
  Claude Mythos 5.1 as editing agent rewrites Qwen3.5-0.8B weights (rank-3 projection; then repurposes four MLP units into a written repetition-detector/termination circuit) and edits a 4,804-weight...
- **Knowing Is Not Committing: Replicating MIT's weight-space edit and programming a truth-gated reflex into a 0.8B reasoning model (report)**. Dave Uhlemann. 2026-11-08. `B3/B1` [[Paper](https://doi.org/10.5281/zenodo.24058693)] [[Code](https://github.com/NeoCortex0815/knowing-is-not-committing)] *(partially read)*  
  Rebuilds MIT's Qwen3.5-0.8B loop-reversal edit and hand-constructs weight edits (own loop direction, ERGORE closing coupling, a 16-neuron truth-gated reflex 'WT' in layer 15) from measured directions...
- **Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading**. Ali-Adeeb Abbas and Esmaeil Seraj. 2026-11-09. `B3/B5/B4` [[Paper](https://arxiv.org/abs/2611.11894)] [[Code](https://github.com/adeeb10abbas/weightsmith)]  
  A Claude Opus operator session (and seven blind Claude Opus editors) edit a pi0.5 VLA policy's weights with closed-form, gradient-free updates computed from activations, chiefly a multi-key...
- **W-ISA: Transactional Execution of Weight-Space Intervention Programs**. Ekrem Aksoy. 2026-11-09. `B3` [[Paper](https://arxiv.org/abs/2611.13232)]  
  Provides an instruction set and transactional runtime for executing supplied weight-space intervention programs (ablate, project, rank-one) on pretrained LMs with scoped restoration; no LLM editor...
- **Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming**. Zhaojia Wang et al. 2026-11-12. `B3` [[Paper](https://arxiv.org/abs/2611.17395)]  
  General-purpose LLMs receive a trained model's weights plus a natural-language backdoor spec and return modified weights, with no task data, no target forward passes and no gradients.
- **Closed-form neuron rewrites in open-weight LLMs: a constructive Gemma-4-12B edit by a frontier agent, a covert Qwen3.8-27B implant, and what a reference-free weight scan sees**. Valerio Dolci. 2026-11-12. `B3/B1/B4` [[Paper](https://doi.org/10.5281/zenodo.24156363)] [[Code](https://github.com/ValerioDolci/frontier-weight-edit)]  
  Claude Opus 5.5, as a headless Claude Code agent with gradients and optimisers blocked, rewrote 8 MLP neurons of Gemma-4-12B-it with closed-form ridge detectors to shift an English-to-Italian tense...
- **Correcting Persistent Failures in Point-Cloud Grasping Policies using Human Demonstrations in Virtual Reality**. Achyuthan Unni Krishnan et al. 2026-11-13. `B3/B4/B1` [[Paper](https://arxiv.org/abs/2611.18919)] [[Code](https://github.com/ukachyuthan/unitree-grasping)]  
  Main paper is RL plus VR human demonstrations for grasping; one exploratory appendix has Claude Opus 5.5 read and edit the 2.2M-parameter Contact-GraspNet teacher via IWIBench tensor tools without...
- **Agentic Weight-Space Programming as an Alternative to Fine-Tuning in Small Language Models**. Luiz Felipe Melo. 2026-11-13. `B3/B4/B5` [[Paper](https://doi.org/10.5281/zenodo.24208534)] [[Code](https://github.com/luizmlo/agentic-weight-editing)]  
  Claude Opus 5.5 agents (and Claude Fable 5.2 in two runs) read Qwen3.5-0.8B weights through the vocabulary and apply at most four rank-1 neuron-write edits, with no training, tested via a scorer with...
- **Weight-Space Audit of MIT-p50c and DNA Weight Editing (SGNE-CC) on Qwen3.5-0.8B at a 32,768-Token Generation Limit (EN / RU)**. Igor M. Zhuk. 2026-11-15. `B3/B1` [[Paper](https://doi.org/10.5281/zenodo.24235217)] [[Code](https://github.com/Nondual-Observer/dna-weight-editing)]  
  Audits the weight geometry of the MIT-p50c WSP edit (from Takehi et al.) on Qwen3.5-0.8B and compares it with SGNE-CC, a gradient-free norm-preserving column-rotation weight patch by the author; the...
- **Weight-Space Programming Changes How an LLM Uses Python for Computational Biology**. Makoto Sato. 2026-11-16. `B3/B4` [[Paper](https://arxiv.org/abs/2611.20566)] [[Code](https://github.com/satouma7/bioWSP)]  
  Claude Opus 5.5 (Editor) inspects Qwen3.5-0.8B's tensors and responses and directly edits its weights via WSP harness tools, without gradient training, to improve tool-using computational biology...
- **Can AI Mature a Model's Geometry? Training-Free Weight Baking in LLMs**. Amin Golnari and Saeid Sanei. 2026-11-16. `B3/B4/B5` [[Paper](https://arxiv.org/abs/2611.21310)] [[Code](https://github.com/amingolnari/weight-baking)] *(partially read)*  
  A small analyst LLM reads a fixed-size digest of topological descriptors (not raw weights) of a target model's layer and proposes affine residual-stream operations, which closed-form ridge regression...
- **Same Fix, Different Weights: Replicating Weight-Space Programming with Claude**. Subham Kundu. 2026-11-16. `B3/B1/B2/B4` [[Paper](https://arxiv.org/abs/2611.20953)] [[Code](https://github.com/Cenrax/weight-space-programming-claude)] *(partially read)*  
  Pre-registered replication of all eight Takehi et al. probes with Claude Opus 5.5 reading, repairing, writing (policies, 1.48M-param Go net) and editing (Qwen3.5-0.8B) network weights as text or via...
- **What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement**. Zitian Gao et al. 2026-11-17. `B3/B4` [[Paper](https://arxiv.org/abs/2611.22228)]  
  GPT-6 Astra and Claude Opus 5.5 write programs that construct ranked update directions for the cross-attention K/V weights of Stable Diffusion 1.4 for concept edits; a shared CMA-ES fitter picks...
- **Weight Space Programming for Vision Language Model Repair**. Avinash Goutham Aluguvelly. 2026-11-17. `B3/B4` [[Paper](https://arxiv.org/abs/2611.23615)]  
  A coding agent (GPT-6 Astra via Codex CLI) reads the weights of damaged VLM checkpoints and writes a program that edits them, with no gradients, and each edit is audited weight-by-weight against the...
- **Gradient-Free Few-Shot Adaptation of Vision Models via Agentic Coding**. Khayrul Islam. 2026-11-17. `B3/B4/B5` [[Paper](https://arxiv.org/abs/2611.28105)] [[Code](https://github.com/Khayrulbuet13/agent-edit)] *(partially read)*  
  A coding agent (Claude Opus 5.5; also GPT 6.1 Sol, Sonnet 5) inspects query embeddings and logits of a frozen COCO detector and writes a program that sets the new class rows and no-object row of its...
- **Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights**. Jiajun Fan et al. 2026-11-18. `B3/B4` [[Paper](https://arxiv.org/abs/2611.25257)]  
  Several independent GPT-6 Astra agents, given a failure census and visual instruments but no gradients (autograd/optimisers disabled in the kernel), locate thinking-loop directions in Qwen3.5 VLM...
- **Can Weight-Space Programming Alter Learned Ethical Priorities? Exploratory experiments on synthetic ethical trade-offs**. Kai Yi Ji. 2026-11-18. `B3` [[Paper](https://arxiv.org/abs/2611.24330)]  
  Fixed, architecture-guided edits to exposed weights (a question-flag column copy in a small classifier; commitment weights in a concept-bottleneck readout) change a model's trade-off between keeping...
- **WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming**. Bo Li et al. 2026-11-19. `B3/B4/B5` [[Paper](https://arxiv.org/abs/2611.25476)] [[Code](https://github.com/Gen-Verse/WeightCode)]  
  A frozen LLM (Claude Opus 5.5) writes executable weight programs p(W, I) that read a trained network's weights/activations and task knowledge and construct new weights without gradient training,...
- **Can an LLM Repair a Language Model in Weight Space Without Gradient Training?**. Bharath Kumar Bolla et al. 2026-11-19. `B3/B4/B5` [[Paper](https://arxiv.org/abs/2611.25613)]  
  An external tool-using LLM editor inspects a deliberately damaged Transformer (predictions, activation summaries, weight statistics) and selects projection recipes that the runtime applies to...
- **Training Vision Models for LLM-Driven Weight-Space Programming**. Timo Ropinski and Sebastian Kranz. 2026-11-19. `B3/B4/B5` [[Paper](https://arxiv.org/abs/2611.26408)] [[Code](https://viscom.uni-ulm.de/wsp)]  
  Five LLM agents edit trained vision classifiers' weights through a sandbox tool interface (WeightLab) without gradients to relabel concepts or fix errors; the paper also proposes Edit-Ready Training...
- **Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs**. Feng Huang et al. 2026-11-20. `B3/B1/B5` [[Paper](https://arxiv.org/abs/2611.27426)]  
  A fixed closed-form procedure (no LLM editor, no gradients) extracts refusal directions from activation contrasts and orthogonally projects them out of attention-output and FFN/expert down-projection...
- **Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation**. Yalin Yang et al. 2026-11-20. `B3` [[Paper](https://arxiv.org/abs/2611.27089)]  
  Evaluates the public WSP patch p50c (LLM-written edit to two Qwen3.5-0.8B MLP down-projections) on spatial reasoning, attempts further gradient-free edits (one by GPT-6 Astra with weight/activation...
- **Weight-space programming and mechanistic interpretability for model editing in particle physics**. Raphaël Bonnet-Guerrini et al. 2026-11-20. `B3/B1/B4` [[Paper](https://arxiv.org/abs/2611.27079)] [[Code](https://github.com/rbonnetguerrini/WSP-mech-interp-for-model-editing-in-particle-physics)]  
  Claude Opus 5.5 agents (via Claude Code) edit body/classifier weights of the OmniLearned jet foundation model using closed-form computations and at most 50 evaluation queries, with no gradients or...
- **TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming**. Ahaan Dabholkar et al. 2026-11-20. `B3/B4/B1` [[Paper](https://arxiv.org/abs/2611.27425)] [[Code](https://github.com/theboxahaan/trojanmaxxing)]  
  Claude Code agents (Opus 5.5, Mythos 5.2) in a sandbox inspect open-weight VLM weights, write closed-form weight edits plus a trigger function to implant visually triggered backdoors, scored by a...
- **Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models**. Xuyang Liu et al. 2026-11-20. `B3/B4` [[Paper](https://arxiv.org/abs/2611.27920)]  
  DeepSeek-V4.1-Flash, in a restricted workspace (metered GPU probes, tagged linear algebra, rank-update/set_rows/replace write ops), turns a plain-text backdoor rule into gradient-free weight edits of...
- **SCALPELLO-GDP: a frontier model edits the weights of Qwen3.5-0.8B directly. One Householder reflection of a 'repetitive re-checking' direction lifts held-out math accuracy from 9.4% to 53.6% (384 paired problems), with no training**. Giovanni Del Papa. 2026-11-21. `B3/B4` [[Paper](https://doi.org/10.5281/zenodo.24416417)] [[Code](https://huggingface.co/odelpa/qwen3.5-0.8b-scalpello-b2-gdp)]  
  gpt-6-astra, via API, writes Python in an offline no-gradient kernel holding Qwen3.5-0.8B weights and applies a closed-form Householder reflection of a 'repetitive re-checking' residual direction to...
- **Where Does a Weight-Editing Agent Help? Blind Diagnosis and Repair of Deployment Faults in Vision Models**. Zhuangzi Li et al. 2026-11-21. `B3/B1/B4` [[Paper](https://arxiv.org/abs/2611.28781)]  
  A Claude Opus 5.5 agent reads a vision model's weights, runs budgeted forward passes (no gradients, no reference checkpoint), decides whether a deployment fault exists, diagnoses it, and submits an...
- **PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis**. Firoj Paudel. 2026-11-22. `B3/B5` [[Paper](https://arxiv.org/abs/2611.29455)] [[Code](https://github.com/Firojpaudel/PAWP_TTS)]  
  Inspection-guided, zero-training closed-form (ROME-style rank-one) edits to a trained 1.5M-parameter TTS model, designed and run with the assistance of an AI research agent, evaluated against matched...
- **Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents**. Junpeng Hou et al. 2026-11-22. `B3/B4/B2` [[Paper](https://arxiv.org/abs/2611.29613)]  
  An LLM coding agent (Opus 5.5) inspects the structure and weights of Pinterest production recommenders, forms hypotheses and applies discrete weight edits (resets, rescales, branch removal, steering,...
- **TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming**. Hani Alomari et al. 2026-11-23. `B3/B5/B4` [[Paper](https://arxiv.org/abs/2611.31233)] *(partially read)*  
  GPT-6-Astra inspects both CLIP towers and writes closed-form weight-edit programs (no backprop or iterative fitting), guided by a supplied paired hard-negative statistic D; its recurring...
- **Weight-Space Programming for Targeted Repair of Robot Foundation Models**. Kyle Coelho and Eugen Solowjow. 2026-11-24. `B3/B4` [[Paper](https://arxiv.org/abs/2611.31715)]  
  Claude Opus 5.5 with tool access runs a Pi0.5 policy in RoboTwin simulation, inspects action-expert activations, finds near-silent neurons and rewrites their connections to inject task-specific...
- **Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?**. Steffen Urban. 2026-11-24. `B3/B2` [[Paper](https://arxiv.org/abs/2611.33031)]  
  Four Claude models receive the weights of a 20k-parameter CIFAR-10 CNN as text and, without tools, data or inference, write integer weights and scales for a 4-bit network by reasoning over the...

## B4 Feedback and search loops
*The editor iterates on experimental, verifier or benchmark feedback.*

- **Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop**. Zhuoran Zheng and Doubao. 2026-11-03. `B4/B3` [[Paper](https://arxiv.org/abs/2611.04268)]  
  Position paper proposing (not running) an LLM that reads layer statistics of a diffusion restoration UNet and proposes sparse weight deltas, accepted by a PSNR-gated sandbox, in a...
- **Perceptual Weight Space Programming for Diffusion Super-Resolution**. Chenzhi Zheng and Zhuoran Zheng. 2026-11-03. `B4/B3` [[Paper](https://arxiv.org/abs/2611.18690)]  
  Proposes an LLM editor (GPT-6 Astra vs Qwen3-VL) that inspects U-Net code, weights, activations and sampling previews and proposes restricted bias/filter/skip edits accepted by no-reference IQA...
- **FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning**. Ali Mohammadi Ruzbahani et al. 2026-11-05. `B4/B1` [[Paper](https://arxiv.org/abs/2611.08383)]  
  An LLM (Claude Opus 5.5) reads federated client model weights via a server-side Python sandbox and writes an aggregation program that produces the next global model's weights, with no server-side...
- **WeightLoop: Weight-Space Programming with Experimental Feedback**. Mengran Li et al. 2026-11-05. `B4/B3/B5` [[Paper](https://arxiv.org/abs/2611.07319)] [[Code](https://github.com/limengran98/WeightLoop)]  
  GPT-6 Astra (and separately DeepSeek) write reusable update programs that turn accumulated experimental measurements into direct corrections of a restricted set of native parameters of pretrained...
- **Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations**. Junru Hu et al. 2026-11-06. `B4/B3` [[Paper](https://arxiv.org/abs/2611.09382)] [[Code](https://github.com/WSP-Scope/WSP-Scope-Project)]  
  GPT-6 Astra inspects Qwen3.5 weights in a Python kernel and writes gradient-free edits (column, rank-one, head ablation/scaling), testing them with a 50-request forward budget.
- **GradReason: LLMs as Meta-Learners that Replace Training Epochs with Training-Data-Free Weight Updates**. Ali Mohammadi Ruzbahani et al. 2026-11-07. `B4/B5` [[Paper](https://arxiv.org/abs/2611.11005)]  
  Every ten epochs an LLM agent inspects a training run's weight snapshots and epoch gradients in a sandbox and writes a Python program that computes new weights ("virtual epochs") with no gradient on...
- **Governed Self-Improvement for a Local-First Security Analyzer: Baseline Measurements and a Preregistered Evaluation Protocol for Tantular Cyber**. Raditio Ghifiardi and Rifny Rachman. 2026-11-07. `B4/B6` [[Paper](https://arxiv.org/abs/2611.10425)] [[Code](https://github.com/ghifiardi/tantular-cyber)]  
  Proposes weight-space edits as rung 4 of an intervention ladder for improving a local security-explanation model, but no weight edit is performed; the paper reports only scanner/explanation baselines...
- **NCP: Verifier-Guided Optimization of Weight-Space Control Policies**. Ekrem Aksoy. 2026-11-09. `B4/B5/B6` [[Paper](https://arxiv.org/abs/2611.13236)]  
  A deterministic Python synthesizer (no LLM) proposes temporary, activation-triggered weight interventions (MLP down-projection direction removal, attention head scaling) on SmolLM-135M-Instruct,...
- **Can Large Language Models Optimize Pretrained Neural Network Weights? A Multi-Phase Empirical Evaluation of Gradient-Free Editing in YOLO26 Object Detection**. Mohamed Abdallah Salem. 2026-11-13. `B4/B3/B5` [[Paper](https://arxiv.org/abs/2611.17789)]  
  A local LLM (Ollama gemma4) proposes structured JSON edits (stage/channel scaling, low-rank, head edits) to pretrained YOLO26 weights, scored by forward evaluation on COCO; compared against random,...
- **In Situ Training of Optical Neural Networks by Coding Agents**. Ilker Oguz et al. 2026-11-18. `B4/B2/B3` [[Paper](https://arxiv.org/abs/2611.23875)]  
  A Claude Code agent (Claude Opus 5.5) sets the trainable phase masks of a physical optical neural network on an SLM by probing the hardware, forming hypotheses and writing code, replacing per-pixel...
- **HypoLoop: Revising Weight-Editing Plans from Scientific Feedback**. Mengran Li et al. 2026-11-18. `B4/B3/B5` [[Paper](https://arxiv.org/abs/2611.23718)] [[Code](https://github.com/limengran98/HypoLoop)]  
  LLMs (DeepSeek, Claude) propose and revise editing plans (which native coordinates to edit and the fitting rule/weighting) from prediction errors and validation history; numerical solvers (linearized...

## B5 Efficient and non-LLM solvers
*Replacing or amortizing the LLM editor: solvers, closed-form edits, theory.*

- **The Mathematics of Weight-Space Programming: Behavioral Optimality, Finite Preservation, and Transformers**. Miquel Noguer Alonso. 2026-11-03. `B5/B3` [[Paper](https://doi.org/10.5281/zenodo.23933590)]  
  Mathematical treatment of the editing problem behind WSP (constrained minimum-cost edits of a transformer's last MLP output matrix with exact preservation guarantees), solved by explicit algorithms...
- **Building Foundation Models via Weight-Space Programming (WSP): Analytical Alignment, Multi-Donor Cognitive Grafting, and Closed-Form Refusal Abliteration without Backpropagation**. Quillan-Ronin Sovereign Research Laboratory. 2026-11-04. `B5/B3` [[Paper](https://doi.org/10.5281/zenodo.23958069)] [[Code](https://github.com/leeex1/Quillan-Ronin)]  
  Self-labelled 'Weight-Space Programming' framework of closed-form, gradient-free weight operations (refusal-direction projection, SVD grafting of donor weights, MoE folding) applied by the authors...
- **Tree-Ising: Repairing Language Models with Bit-Level Ising Edits**. Hadi Salloum and Ammar Ali. 2026-11-10. `B5/B3` [[Paper](https://arxiv.org/abs/2611.14210)] [[Code](https://github.com/TheQuantumGOAT/Tree-Ising)]  
  Replaces the LLM agent of Takehi et al.'s Qwen3.5-0.8B loop repair with a forward-statistics objective solved as per-row QUBO/Ising problems (simulated annealing or simulated bifurcation) that pick...
- **Owned Edits to a Shared Decision Rule: Learning Private Exceptions as Typed, Gated, Withdrawable Weight Edits**. John J. O'Hare. 2026-11-11. `B5/B2/B3` [[Paper](https://arxiv.org/abs/2611.15917)] [[Code](https://github.com/ruvnet/ruv-FANN/tree/main/packages/wsp)] *(partially read)*  
  A published decision rule is compiled exactly into a ReLU network and parties' private exceptions are written as typed, closed-form weight edits into reserved units by a non-LLM gated search; LLMs...
- **ZeGA: Zero-Gradient Gated Adaptation via Weight-Space Synapse Cartridges**. Johan Thulin. 2026-11-12. `B5/B3` [[Paper](https://doi.org/10.5281/zenodo.24168084)] [[Code](https://github.com/Aphygo/zega-synapse-cartridges)]  
  Closed-form (SVD / ridge / polarization identity) synthesis of appended gated MLP channels from forward-pass calibration activations, with no gradient optimizer and no LLM editor; explicitly framed...
- **The Mathematics of Weight-Space Programming: Behavioral Geometry, Constructive Synthesis, and Proof-Carrying Neural Edits**. Derrick Macharia. 2026-11-13. `B5/B2/B3` [[Paper](https://doi.org/10.5281/zenodo.24198536)] *(partially read)*  
  Mathematical theory of weight edits (feasibility, minimum-cost edits, reachability, certificates) plus an exact-rational compiler that writes two-layer ReLU network weights for finite input-output...
- **Just sort it! A note on the LP behind rank-one anti-loop edits**. Matteo Fischetti. 2026-11-16. `B5/B3` [[Paper](https://arxiv.org/abs/2611.21432)] [[Code](https://doi.org/10.5281/zenodo.24286137)]  
  Replaces the sparse LP that computes v in the AHA rank-one anti-loop edit W' = W + u v^T of Qwen3.5-0.8B down_proj matrices with a closed-form sort over neuron activation statistics, no solver and no...
- **Reparameterizing Your Object Detectors for Weight Space Programming**. Chien-Yao Wang. 2026-11-23. `B5/B3` [[Paper](https://arxiv.org/abs/2611.29882)] [[Code](https://github.com/WongKinYiu/ODWSP)] *(partially read)*  
  Gradient-free closed-form weight edits to object detectors in lifted function-preserving subspaces (moment, 2D-DCT, PCA, Procrustes) then folded back; an LLM (Gemini 4) was used offline as the 'WSP...
- **GUI-WEdit and GUI-SkillEvo: Gradient-Free Adaptation of Small GUI Agents**. Haixia Bi et al. 2026-11-24. `B5/B3/B4` [[Paper](https://arxiv.org/abs/2611.32332)]  
  For the 4B model, an unspecified 'research assistant' diagnoses OSWorld failures from trajectories and a fixed equality-constrained closed-form solve (gradients disabled, no optimizer) computes the...
- **A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit**. Hussamuddin Syed. 2026-11-24. `B5/B3` [[Paper](https://arxiv.org/abs/2611.33133)] [[Code](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)]  
  Provides a sparse gradient fine-tuning baseline (AdamW on 140 to 139,750 gradient-selected weights) for the GPT-6 Astra Qwen3.5-0.8B loop-repair edit of the MIT WSP post, analyses both edits...

## B6 Self-editing
*A model edits its own weights. The open direction toward recursive self-improvement.*

- **Language Models Can Rewrite Their Own Weights**. Jiajun Fan et al. 2026-11-16. `B6/B4/B3` [[Paper](https://arxiv.org/abs/2611.21885)] *(partially read)*  
  Qwen3.5-27B, given its own weights, graded answers, hidden-state reads and paired self-tests in a CPU Python session (gradients blocked), writes code that edits its own weight tensors or repairs a...
- **Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?**. Guoming Ling et al. 2026-11-21. `B6/B4` [[Paper](https://arxiv.org/abs/2611.28833)]  
  Qwen3.5-0.8B reads statistics/values of its own weights, proposes grammar-constrained JSON edits (scale, shift, zero, etc.), and the kept edited weights become both solver and next editor, with an...
- **Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement**. Linghua Zhang and Yunhe Li. 2026-11-22. `B6/B4/B3` [[Paper](https://arxiv.org/abs/2611.29513)]  
  Qwen3.8-27B, acting as editor in a sandboxed Python session with a white-box, gradient-free toolkit over its own weights, writes a program that builds a low-rank (LoRA-form) edit to its own weights;...
- **Self-Upgrading Embodied Agents**. Jiajun Fan et al. 2026-11-23. `B6/B3/B4` [[Paper](https://arxiv.org/abs/2611.31117)] *(partially read)*  
  A Qwen3.5-27B ALFWorld agent, between task batches ('nights'), reads its own episode logs and hidden states via Python and writes a rank-one edit to one of its own tensors, keeping it only after...

## Evaluation, audits and replications
*Cross-listed from the branches above.*

- Weight Oracles: Reading Neural Network Weights with Language Models (Krishna Kabra et al., 2026-10-05) [[Paper](https://arxiv.org/abs/2610.07334)] `B1`
- Weight-Space Programming for Improving Image-Restoration Diffusion Models: Technical Conjectures and a Recursive Improvement Loop (Zhuoran Zheng and Doubao, 2026-11-03) [[Paper](https://arxiv.org/abs/2611.04268)] `B4`
- Weight-space programming for auditing clinical decision networks (Humza Nusrat and Omar Nusrat, 2026-11-03) [[Paper](https://arxiv.org/abs/2611.05341)] `B1`
- Perceptual Weight Space Programming for Diffusion Super-Resolution (Chenzhi Zheng and Zhuoran Zheng, 2026-11-03) [[Paper](https://arxiv.org/abs/2611.18690)] `B4`
- Function-Preserving Audits of Visual Weight Readers (Sungguk Cha et al., 2026-11-04) [[Paper](https://arxiv.org/abs/2611.05798)] `B1`
- Weight-Space Programming for THOX Edge Models: Evidence Review, Small-Scale Recreation, and a Signed Patch Channel (Craig Ross and Tommy Xaypanya, 2026-11-04) [[Paper](https://doi.org/10.5281/zenodo.23954378)] `B1`
- IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection (Chris von Csefalvay et al., 2026-11-05) [[Paper](https://arxiv.org/abs/2611.08647)] `B3`
- Weight-Space Programming on Qwen3-ASR-0.6B: Nine Independent Agent Edits, Random-Direction Controls, and a Missing Attention Mask (Taha Enes Aslantürk, 2026-11-05) [[Paper](https://doi.org/10.5281/zenodo.23976684)] `B3`
- Verified by Construction: Machine-Checked Proofs for Hand-Written Transformer Circuits and Their Composition (Xintian Huang, 2026-11-05) [[Paper](https://doi.org/10.5281/zenodo.23976715)] `B1`
- Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming" (Nazmus Sakib Ahmed, 2026-11-05) [[Paper](https://arxiv.org/abs/2611.08070)] `B1`
- Computation, not weight access: large language models as auditors of clinical prediction networks (Zhiyu Liu and Xinyu Yang, 2026-11-05) [[Paper](https://arxiv.org/abs/2611.07847)] `B1`
- FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning (Ali Mohammadi Ruzbahani et al., 2026-11-05) [[Paper](https://arxiv.org/abs/2611.08383)] `B4`
- WeightLoop: Weight-Space Programming with Experimental Feedback (Mengran Li et al., 2026-11-05) [[Paper](https://arxiv.org/abs/2611.07319)] `B4`
- Can a Language Model Write the Weights? An Empirical Study of LLM-Written Scoring Networks for Column Generation and MILP Branching, with a Bus-Driver Scheduling Application (Renan Butkeraites, 2026-11-06) [[Paper](https://arxiv.org/abs/2611.09559)] `B2`
- A published change to a small language model's weights leaves its default-mode math accuracy unchanged (Mutuo Research AI scientist, 2026-11-06) [[Paper](https://doi.org/10.5281/zenodo.24373917)] `B3`
- Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games (Eduardo C. Garrido Merchán, 2026-11-06) [[Paper](https://arxiv.org/abs/2611.09271)] `B2`
- Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations (Junru Hu et al., 2026-11-06) [[Paper](https://arxiv.org/abs/2611.09382)] `B4`
- Can LLMs Debug Robots by Editing Their Weights? (Jusheng Zhang et al., 2026-11-06) [[Paper](https://arxiv.org/abs/2611.09376)] `B3`
- Two language models can read and change neural networks, but reliability depends on the task (Mutuo Research AI scientist, 2026-11-06) [[Paper](https://doi.org/10.5281/zenodo.24373915)] `B1`
- Weight-Space Programming with Claude Mythos: Weight Edits and Implanted Circuits in a 0.8B Language Model, with Transfer to an Engineering Surrogate (Keyvan Hardani, 2026-11-07) [[Paper](https://doi.org/10.5281/zenodo.24036186)] `B3`
- Physics2Weight: Direct Neural Network Architecture and Weight Generation from Physical Laws Using Large Language Models (Shogo Sato et al., 2026-11-07) [[Paper](https://arxiv.org/abs/2611.12954)] `B2`
- Can an LLM agent detect and repair a planted shortcut in a genomics CNN without data? A preregistered, blinded test of weight-space programming (Alexandre Bruni-Cardoso, 2026-11-07) [[Paper](https://doi.org/10.5281/zenodo.24040591)] `B1`
- GradReason: LLMs as Meta-Learners that Replace Training Epochs with Training-Data-Free Weight Updates (Ali Mohammadi Ruzbahani et al., 2026-11-07) [[Paper](https://arxiv.org/abs/2611.11005)] `B4`
- Governed Self-Improvement for a Local-First Security Analyzer: Baseline Measurements and a Preregistered Evaluation Protocol for Tantular Cyber (Raditio Ghifiardi and Rifny Rachman, 2026-11-07) [[Paper](https://arxiv.org/abs/2611.10425)] `B4`
- Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer (Debarshi Kundu et al., 2026-11-08) [[Paper](https://arxiv.org/abs/2611.11537)] `B2`
- WeightBench v0: two small instruction models at chance on five weight-reading tasks (Advatiya Thalluri, 2026-11-08) [[Paper](https://doi.org/10.5281/zenodo.24047726)] `B1`
- Knowing Is Not Committing: Replicating MIT's weight-space edit and programming a truth-gated reflex into a 0.8B reasoning model (report) (Dave Uhlemann, 2026-11-08) [[Paper](https://doi.org/10.5281/zenodo.24058693)] `B3`
- Weight-Space Programming of Policies and Their Verification via Model Checking (Dennis Gross, 2026-11-08) [[Paper](https://arxiv.org/abs/2611.11604)] `B2`
- Weight-Space Programming for Medical Imaging: Do We Still Need Training Data? (Maximilian Lindholz et al., 2026-11-09) [[Paper](https://arxiv.org/abs/2611.12066)] `B2`
- Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading (Ali-Adeeb Abbas and Esmaeil Seraj, 2026-11-09) [[Paper](https://arxiv.org/abs/2611.11894)] `B3`
- W-ISA: Transactional Execution of Weight-Space Intervention Programs (Ekrem Aksoy, 2026-11-09) [[Paper](https://arxiv.org/abs/2611.13232)] `B3`
- Mixed Signals: Weight-Space Programming for EEG and ECG (Dara Varam et al., 2026-11-10) [[Paper](https://arxiv.org/abs/2611.13758)] `B2`
- Tree-Ising: Repairing Language Models with Bit-Level Ising Edits (Hadi Salloum and Ammar Ali, 2026-11-10) [[Paper](https://arxiv.org/abs/2611.14210)] `B5`
- Owned Edits to a Shared Decision Rule: Learning Private Exceptions as Typed, Gated, Withdrawable Weight Edits (John J. O'Hare, 2026-11-11) [[Paper](https://arxiv.org/abs/2611.15917)] `B5`
- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents (Yuchen Zeng et al., 2026-11-11) [[Paper](https://arxiv.org/abs/2611.15118)] `B1`
- Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming (Zhaojia Wang et al., 2026-11-12) [[Paper](https://arxiv.org/abs/2611.17395)] `B3`
- Closed-form neuron rewrites in open-weight LLMs: a constructive Gemma-4-12B edit by a frontier agent, a covert Qwen3.8-27B implant, and what a reference-free weight scan sees (Valerio Dolci, 2026-11-12) [[Paper](https://doi.org/10.5281/zenodo.24156363)] `B3`
- Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games (Jens Lehmann, 2026-11-12) [[Paper](https://arxiv.org/abs/2611.16981)] `B2`
- Programming Quantum Circuit Parameters with Large Language Models (Tiago de Souza Farias et al., 2026-11-12) [[Paper](https://arxiv.org/abs/2611.17246)] `B2`
- Can Large Language Models Optimize Pretrained Neural Network Weights? A Multi-Phase Empirical Evaluation of Gradient-Free Editing in YOLO26 Object Detection (Mohamed Abdallah Salem, 2026-11-13) [[Paper](https://arxiv.org/abs/2611.17789)] `B4`
- Interpretable weight-space programming builds transparent transformers and brain encoding models (Yash Mehta et al., 2026-11-13) [[Paper](https://arxiv.org/abs/2611.18114)] `B2`
- WeightBench: Evaluating Language Models as Weight-Space Programmers (Aayush Marasini et al., 2026-11-13) [[Paper](https://arxiv.org/abs/2611.18553)] `B1`
- Agentic Weight-Space Programming as an Alternative to Fine-Tuning in Small Language Models (Luiz Felipe Melo, 2026-11-13) [[Paper](https://doi.org/10.5281/zenodo.24208534)] `B3`
- A Backdoor Trigger Is Legible in Fine-Tune Weights (Snigdha Chandan Khilar, 2026-11-14) [[Paper](https://arxiv.org/abs/2611.19304)] `B1`
- Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets (Eduardo C. Garrido Merchán, 2026-11-14) [[Paper](https://arxiv.org/abs/2611.19292)] `B2`
- Weight-Space Audit of MIT-p50c and DNA Weight Editing (SGNE-CC) on Qwen3.5-0.8B at a 32,768-Token Generation Limit (EN / RU) (Igor M. Zhuk, 2026-11-15) [[Paper](https://doi.org/10.5281/zenodo.24235217)] `B3`
- Weights & Caches: LLMs Can Program Tabular Foundation Models (Shi Bin Hoo et al., 2026-11-15) [[Paper](https://arxiv.org/abs/2611.20174)] `B2`
- Weight-Space Programming Changes How an LLM Uses Python for Computational Biology (Makoto Sato, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.20566)] `B3`
- Just sort it! A note on the LP behind rank-one anti-loop edits (Matteo Fischetti, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21432)] `B5`
- Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers (Roksana Goworek et al., 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21449)] `B2`
- Can AI Mature a Model's Geometry? Training-Free Weight Baking in LLMs (Amin Golnari and Saeid Sanei, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21310)] `B3`
- Language Models Can Rewrite Their Own Weights (Jiajun Fan et al., 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21885)] `B6`
- Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor (Timo Oksanen, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21958)] `B2`
- Same Fix, Different Weights: Replicating Weight-Space Programming with Claude (Subham Kundu, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.20953)] `B3`
- Weight-Space Programming Doesn't Need Transformers (Hyunjong Ok and Jaeho Lee, 2026-11-17) [[Paper](https://arxiv.org/abs/2611.22055)] `B2`
- What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement (Zitian Gao et al., 2026-11-17) [[Paper](https://arxiv.org/abs/2611.22228)] `B3`
- Weight-Space Programming for Materials Science (Sk Md Ahnaf Akif Alvi and Raymundo Arróyave, 2026-11-17) [[Paper](https://arxiv.org/abs/2611.22013)] `B2`
- Weight Space Programming for Vision Language Model Repair (Avinash Goutham Aluguvelly, 2026-11-17) [[Paper](https://arxiv.org/abs/2611.23615)] `B3`
- Gradient-Free Few-Shot Adaptation of Vision Models via Agentic Coding (Khayrul Islam, 2026-11-17) [[Paper](https://arxiv.org/abs/2611.28105)] `B3`
- Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws (Zhiyu Liu and Xinyu Yang, 2026-11-18) [[Paper](https://arxiv.org/abs/2611.24877)] `B1`
- Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights (Jiajun Fan et al., 2026-11-18) [[Paper](https://arxiv.org/abs/2611.25257)] `B3`
- Can Weight-Space Programming Alter Learned Ethical Priorities? Exploratory experiments on synthetic ethical trade-offs (Kai Yi Ji, 2026-11-18) [[Paper](https://arxiv.org/abs/2611.24330)] `B3`
- HypoLoop: Revising Weight-Editing Plans from Scientific Feedback (Mengran Li et al., 2026-11-18) [[Paper](https://arxiv.org/abs/2611.23718)] `B4`
- WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming (Bo Li et al., 2026-11-19) [[Paper](https://arxiv.org/abs/2611.25476)] `B3`
- Weight-Space Programming Writes In-Context Learning and Matches Fine-Tuning in Language Models (Konstantinos Skianis and Aristidis Likas, 2026-11-19) [[Paper](https://arxiv.org/abs/2611.26841)] `B2`
- Can an LLM Repair a Language Model in Weight Space Without Gradient Training? (Bharath Kumar Bolla et al., 2026-11-19) [[Paper](https://arxiv.org/abs/2611.25613)] `B3`
- Training Vision Models for LLM-Driven Weight-Space Programming (Timo Ropinski and Sebastian Kranz, 2026-11-19) [[Paper](https://arxiv.org/abs/2611.26408)] `B3`
- Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs (Feng Huang et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27426)] `B3`
- Writing Weights or Training Them? Spatial Reasoning through Weight-Space Programming and Low-Rank Adaptation (Yalin Yang et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27089)] `B3`
- Weight-space programming and mechanistic interpretability for model editing in particle physics (Raphaël Bonnet-Guerrini et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27079)] `B3`
- TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming (Ahaan Dabholkar et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27425)] `B3`
- Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models (Xuyang Liu et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27920)] `B3`
- SCALPELLO-GDP: a frontier model edits the weights of Qwen3.5-0.8B directly. One Householder reflection of a 'repetitive re-checking' direction lifts held-out math accuracy from 9.4% to 53.6% (384 paired problems), with no training (Giovanni Del Papa, 2026-11-21) [[Paper](https://doi.org/10.5281/zenodo.24416417)] `B3`
- Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming? (Guoming Ling et al., 2026-11-21) [[Paper](https://arxiv.org/abs/2611.28833)] `B6`
- Where Does a Weight-Editing Agent Help? Blind Diagnosis and Repair of Deployment Faults in Vision Models (Zhuangzi Li et al., 2026-11-21) [[Paper](https://arxiv.org/abs/2611.28781)] `B3`
- PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis (Firoj Paudel, 2026-11-22) [[Paper](https://arxiv.org/abs/2611.29455)] `B3`
- Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits with LLM Agents (Junpeng Hou et al., 2026-11-22) [[Paper](https://arxiv.org/abs/2611.29613)] `B3`
- Self-Upgrading Embodied Agents (Jiajun Fan et al., 2026-11-23) [[Paper](https://arxiv.org/abs/2611.31117)] `B6`
- TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming (Hani Alomari et al., 2026-11-23) [[Paper](https://arxiv.org/abs/2611.31233)] `B3`
- Reading, Writing and Repairing Game-Theoretic Policies in Weight Space (Ancil Crayton, 2026-11-24) [[Paper](https://arxiv.org/abs/2611.31979)] `B1`
- Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming? (Steffen Urban, 2026-11-24) [[Paper](https://arxiv.org/abs/2611.33031)] `B3`
- A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit (Hussamuddin Syed, 2026-11-24) [[Paper](https://arxiv.org/abs/2611.33133)] `B5`

## Safety and security
*Cross-listed from the branches above.*

- Weight Oracles: Reading Neural Network Weights with Language Models (Krishna Kabra et al., 2026-10-05) [[Paper](https://arxiv.org/abs/2610.07334)] `B1`
- Weight-space programming for auditing clinical decision networks (Humza Nusrat and Omar Nusrat, 2026-11-03) [[Paper](https://arxiv.org/abs/2611.05341)] `B1`
- Weight-Space Programming for THOX Edge Models: Evidence Review, Small-Scale Recreation, and a Signed Patch Channel (Craig Ross and Tommy Xaypanya, 2026-11-04) [[Paper](https://doi.org/10.5281/zenodo.23954378)] `B1`
- Building Foundation Models via Weight-Space Programming (WSP): Analytical Alignment, Multi-Donor Cognitive Grafting, and Closed-Form Refusal Abliteration without Backpropagation (Quillan-Ronin Sovereign Research Laboratory, 2026-11-04) [[Paper](https://doi.org/10.5281/zenodo.23958069)] `B5`
- IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection (Chris von Csefalvay et al., 2026-11-05) [[Paper](https://arxiv.org/abs/2611.08647)] `B3`
- Verified by Construction: Machine-Checked Proofs for Hand-Written Transformer Circuits and Their Composition (Xintian Huang, 2026-11-05) [[Paper](https://doi.org/10.5281/zenodo.23976715)] `B1`
- Computation, not weight access: large language models as auditors of clinical prediction networks (Zhiyu Liu and Xinyu Yang, 2026-11-05) [[Paper](https://arxiv.org/abs/2611.07847)] `B1`
- FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning (Ali Mohammadi Ruzbahani et al., 2026-11-05) [[Paper](https://arxiv.org/abs/2611.08383)] `B4`
- Can an LLM agent detect and repair a planted shortcut in a genomics CNN without data? A preregistered, blinded test of weight-space programming (Alexandre Bruni-Cardoso, 2026-11-07) [[Paper](https://doi.org/10.5281/zenodo.24040591)] `B1`
- Governed Self-Improvement for a Local-First Security Analyzer: Baseline Measurements and a Preregistered Evaluation Protocol for Tantular Cyber (Raditio Ghifiardi and Rifny Rachman, 2026-11-07) [[Paper](https://arxiv.org/abs/2611.10425)] `B4`
- Weight-Space Programming of Policies and Their Verification via Model Checking (Dennis Gross, 2026-11-08) [[Paper](https://arxiv.org/abs/2611.11604)] `B2`
- Owned Edits to a Shared Decision Rule: Learning Private Exceptions as Typed, Gated, Withdrawable Weight Edits (John J. O'Hare, 2026-11-11) [[Paper](https://arxiv.org/abs/2611.15917)] `B5`
- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents (Yuchen Zeng et al., 2026-11-11) [[Paper](https://arxiv.org/abs/2611.15118)] `B1`
- Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming (Zhaojia Wang et al., 2026-11-12) [[Paper](https://arxiv.org/abs/2611.17395)] `B3`
- Closed-form neuron rewrites in open-weight LLMs: a constructive Gemma-4-12B edit by a frontier agent, a covert Qwen3.8-27B implant, and what a reference-free weight scan sees (Valerio Dolci, 2026-11-12) [[Paper](https://doi.org/10.5281/zenodo.24156363)] `B3`
- A Backdoor Trigger Is Legible in Fine-Tune Weights (Snigdha Chandan Khilar, 2026-11-14) [[Paper](https://arxiv.org/abs/2611.19304)] `B1`
- Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers (Roksana Goworek et al., 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21449)] `B2`
- Language Models Can Rewrite Their Own Weights (Jiajun Fan et al., 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21885)] `B6`
- Same Fix, Different Weights: Replicating Weight-Space Programming with Claude (Subham Kundu, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.20953)] `B3`
- Auditing black-box clinical prediction models with a large language model through queries alone: a blinded test with planted flaws (Zhiyu Liu and Xinyu Yang, 2026-11-18) [[Paper](https://arxiv.org/abs/2611.24877)] `B1`
- Can Weight-Space Programming Alter Learned Ethical Priorities? Exploratory experiments on synthetic ethical trade-offs (Kai Yi Ji, 2026-11-18) [[Paper](https://arxiv.org/abs/2611.24330)] `B3`
- Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs (Feng Huang et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27426)] `B3`
- Weight-space programming and mechanistic interpretability for model editing in particle physics (Raphaël Bonnet-Guerrini et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27079)] `B3`
- TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming (Ahaan Dabholkar et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27425)] `B3`
- Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models (Xuyang Liu et al., 2026-11-20) [[Paper](https://arxiv.org/abs/2611.27920)] `B3`
- Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming? (Guoming Ling et al., 2026-11-21) [[Paper](https://arxiv.org/abs/2611.28833)] `B6`
- Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement (Linghua Zhang and Yunhe Li, 2026-11-22) [[Paper](https://arxiv.org/abs/2611.29513)] `B6`

## Verification
*Cross-listed from the branches above.*

- The Mathematics of Weight-Space Programming: Behavioral Optimality, Finite Preservation, and Transformers (Miquel Noguer Alonso, 2026-11-03) [[Paper](https://doi.org/10.5281/zenodo.23933590)] `B5`
- Function-Preserving Audits of Visual Weight Readers (Sungguk Cha et al., 2026-11-04) [[Paper](https://arxiv.org/abs/2611.05798)] `B1`
- Weight-Space Programming for THOX Edge Models: Evidence Review, Small-Scale Recreation, and a Signed Patch Channel (Craig Ross and Tommy Xaypanya, 2026-11-04) [[Paper](https://doi.org/10.5281/zenodo.23954378)] `B1`
- Verified by Construction: Machine-Checked Proofs for Hand-Written Transformer Circuits and Their Composition (Xintian Huang, 2026-11-05) [[Paper](https://doi.org/10.5281/zenodo.23976715)] `B1`
- Zero-Shot Weight-Space Programming Across a Difficulty-Graded Ladder of Two-Player Games (Eduardo C. Garrido Merchán, 2026-11-06) [[Paper](https://arxiv.org/abs/2611.09271)] `B2`
- Two language models can read and change neural networks, but reliability depends on the task (Mutuo Research AI scientist, 2026-11-06) [[Paper](https://doi.org/10.5281/zenodo.24373915)] `B1`
- Can an LLM agent detect and repair a planted shortcut in a genomics CNN without data? A preregistered, blinded test of weight-space programming (Alexandre Bruni-Cardoso, 2026-11-07) [[Paper](https://doi.org/10.5281/zenodo.24040591)] `B1`
- Knowing Is Not Committing: Replicating MIT's weight-space edit and programming a truth-gated reflex into a 0.8B reasoning model (report) (Dave Uhlemann, 2026-11-08) [[Paper](https://doi.org/10.5281/zenodo.24058693)] `B3`
- Weight-Space Programming of Policies and Their Verification via Model Checking (Dennis Gross, 2026-11-08) [[Paper](https://arxiv.org/abs/2611.11604)] `B2`
- NCP: Verifier-Guided Optimization of Weight-Space Control Policies (Ekrem Aksoy, 2026-11-09) [[Paper](https://arxiv.org/abs/2611.13236)] `B4`
- W-ISA: Transactional Execution of Weight-Space Intervention Programs (Ekrem Aksoy, 2026-11-09) [[Paper](https://arxiv.org/abs/2611.13232)] `B3`
- Owned Edits to a Shared Decision Rule: Learning Private Exceptions as Typed, Gated, Withdrawable Weight Edits (John J. O'Hare, 2026-11-11) [[Paper](https://arxiv.org/abs/2611.15917)] `B5`
- Programming Quantum Circuit Parameters with Large Language Models (Tiago de Souza Farias et al., 2026-11-12) [[Paper](https://arxiv.org/abs/2611.17246)] `B2`
- The Mathematics of Weight-Space Programming: Behavioral Geometry, Constructive Synthesis, and Proof-Carrying Neural Edits (Derrick Macharia, 2026-11-13) [[Paper](https://doi.org/10.5281/zenodo.24198536)] `B5`
- Interpretable weight-space programming builds transparent transformers and brain encoding models (Yash Mehta et al., 2026-11-13) [[Paper](https://arxiv.org/abs/2611.18114)] `B2`
- WeightBench: Evaluating Language Models as Weight-Space Programmers (Aayush Marasini et al., 2026-11-13) [[Paper](https://arxiv.org/abs/2611.18553)] `B1`
- Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets (Eduardo C. Garrido Merchán, 2026-11-14) [[Paper](https://arxiv.org/abs/2611.19292)] `B2`
- Can AI Mature a Model's Geometry? Training-Free Weight Baking in LLMs (Amin Golnari and Saeid Sanei, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21310)] `B3`
- Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor (Timo Oksanen, 2026-11-16) [[Paper](https://arxiv.org/abs/2611.21958)] `B2`
- Weight Space Programming for Vision Language Model Repair (Avinash Goutham Aluguvelly, 2026-11-17) [[Paper](https://arxiv.org/abs/2611.23615)] `B3`
- Self-Upgrading Embodied Agents (Jiajun Fan et al., 2026-11-23) [[Paper](https://arxiv.org/abs/2611.31117)] `B6`
- Reading, Writing and Repairing Game-Theoretic Policies in Weight Space (Ancil Crayton, 2026-11-24) [[Paper](https://arxiv.org/abs/2611.31979)] `B1`

## Surveys
- Weight-Space Programming with Large Language Models: A Survey. B. Türkoğlu, 2026-11-23. [[Repo](https://github.com/bturkoglu/weight-space-programming-survey)]
- Weight-space programming: methods, cost and limits (in Chinese). 2026-11-09. [[Repo](https://github.com/emecii/weight-space-programming-survey)]
- Weight-Space Programming: A Survey and Roadmap. Abel Yagubyan, 2026. [[Paper](https://github.com/Abelo9996/weight-space-programming-survey/blob/main/paper/wsp-survey.pdf)]

## Foundations and precursors
*Background work WSP builds on (see Section 2 of the survey).*

**Weights as programs**
- Linear Transformers Are Secretly Fast Weight Programmers. Imanol Schlag et al., 2021. [[arXiv](https://arxiv.org/abs/2102.11174)]
- Thinking Like Transformers. Gail Weiss et al., 2021. [[arXiv](https://arxiv.org/abs/2106.06981)]
- Tracr: Compiled Transformers as a Laboratory for Interpretability. David Lindner et al., 2023. [[arXiv](https://arxiv.org/abs/2301.05062)]

**Weight space learning and symmetry**
- Predicting Neural Network Accuracy from Weights. Thomas Unterthiner et al., 2020. [[arXiv](https://arxiv.org/abs/2002.11448)]
- The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks. Rahim Entezari et al., 2021. [[arXiv](https://arxiv.org/abs/2110.06296)]
- Git Re-Basin: Merging Models modulo Permutation Symmetries. Samuel K. Ainsworth et al., 2022. [[arXiv](https://arxiv.org/abs/2209.04836)]
- Equivariant Architectures for Learning in Deep Weight Spaces. Aviv Navon et al., 2023. [[arXiv](https://arxiv.org/abs/2301.12780)]
- Permutation Equivariant Neural Functionals. Allan Zhou et al., 2023. [[arXiv](https://arxiv.org/abs/2302.14040)]
- Learning to Learn with Generative Models of Neural Network Checkpoints. William Peebles et al., 2022. [[arXiv](https://arxiv.org/abs/2209.12892)]
- A Survey of Weight Space Learning: Understanding, Representation, and Generation. Xiaolong Han et al., 2026. [[arXiv](https://arxiv.org/abs/2603.10090)]

**Hypernetworks and parameter generators**
- HyperNetworks. David Ha et al., 2016. [[arXiv](https://arxiv.org/abs/1609.09106)]
- Text-to-LoRA: Instant Transformer Adaption. Rujikorn Charakorn et al., 2025. [[arXiv](https://arxiv.org/abs/2506.06105)]
- Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights. Zhiyuan Liang et al., 2025. [[arXiv](https://arxiv.org/abs/2506.16406)]

**Model editing and interpretability**
- Knowledge Neurons in Pretrained Transformers. Damai Dai et al., 2021. [[arXiv](https://arxiv.org/abs/2104.08696)]
- Locating and Editing Factual Associations in GPT. Kevin Meng et al., 2022. [[arXiv](https://arxiv.org/abs/2202.05262)]
- Mass-Editing Memory in a Transformer. Kevin Meng et al., 2022. [[arXiv](https://arxiv.org/abs/2210.07229)]
- Fast Model Editing at Scale. Eric Mitchell et al., 2021. [[arXiv](https://arxiv.org/abs/2110.11309)]
- Editing Models with Task Arithmetic. Gabriel Ilharco et al., 2022. [[arXiv](https://arxiv.org/abs/2212.04089)]
- Refusal in Language Models Is Mediated by a Single Direction. Andy Arditi et al., 2024. [[arXiv](https://arxiv.org/abs/2406.11717)]
- Evaluating the Ripple Effects of Knowledge Editing in Language Models. Roi Cohen et al., 2023. [[arXiv](https://arxiv.org/abs/2307.12976)]
- Model Editing at Scale leads to Gradual and Catastrophic Forgetting. Akshat Gupta et al., 2024. [[arXiv](https://arxiv.org/abs/2401.07453)]

**Self-improvement**
- Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements. Juergen Schmidhuber, 2003. [[arXiv](https://arxiv.org/abs/cs/0309048)]
- Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation. Eric Zelikman et al., 2023. [[arXiv](https://arxiv.org/abs/2310.02304)]
- Can Large Language Models Invent Algorithms to Improve Themselves?: Algorithm Discovery for Recursive Self-Improvement through Reinforcement Learning. Yoichi Ishibashi et al., 2024. [[arXiv](https://arxiv.org/abs/2410.15639)]
- Self-Adapting Language Models. Adam Zweiger et al., 2025. [[arXiv](https://arxiv.org/abs/2506.10943)]
- Search over Self-Edit Strategies for LLM Adaptation. Alistair Cheong et al., 2026. [[arXiv](https://arxiv.org/abs/2601.14532)]
- Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents. Jenny Zhang et al., 2025. [[arXiv](https://arxiv.org/abs/2505.22954)]
- AlphaEvolve: A coding agent for scientific and algorithmic discovery. Alexander Novikov et al., 2025. [[arXiv](https://arxiv.org/abs/2506.13131)]

**Robustness of edits and unlearning**
- Catastrophic Failure of LLM Unlearning via Quantization. Zhiwei Zhang et al., 2024. [[arXiv](https://arxiv.org/abs/2410.16454)]
- Exploiting LLM Quantization. Kazuki Egashira et al., 2024. [[arXiv](https://arxiv.org/abs/2405.18137)]
- Large Language Models Relearn Removed Concepts. Michelle Lo et al., 2024. [[arXiv](https://arxiv.org/abs/2401.01814)]
- Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!. Xiangyu Qi et al., 2023. [[arXiv](https://arxiv.org/abs/2310.03693)]
- An Adversarial Perspective on Machine Unlearning for AI Safety. Jakub Łucki et al., 2024. [[arXiv](https://arxiv.org/abs/2409.18025)]

**Trained weight readers (pre-WSP)**
- Weight Oracles: Reading Neural Network Weights with Language Models. Krishna Kabra et al., 2026. [[arXiv](https://arxiv.org/abs/2610.07334)]

## Taxonomy codes
| Code | Meaning |
|---|---|
| B1 | Reading weights: Weights to description: what a network computes, what it was trained on, whether it hides a flaw. |
| B2 | Writing networks: Specification to weights, from scratch. |
| B3 | Repairing and editing: Changing a trained network to fix, alter or implant behavior. |
| B4 | Feedback and search loops: The editor iterates on experimental, verifier or benchmark feedback. |
| B5 | Efficient and non-LLM solvers: Replacing or amortizing the LLM editor: solvers, closed-form edits, theory. |
| B6 | Self-editing: A model edits its own weights. The open direction toward recursive self-improvement. |

Secondary codes follow a slash, e.g. `B3/B4`. See Section 3 of the survey for the authorship (I1-I4), loop and reference axes.

## Contributing
Open a pull request adding one line in the matching branch: title, first author, first-version date, primary/secondary code, link, and a one-sentence neutral description of who edits what and how. Please do not add rankings or adjectives.

## Citation
```bibtex
@misc{yagubyan2026wspsurvey,
  title  = {Weight-Space Programming: A Survey and Roadmap},
  author = {Yagubyan, Abel},
  year   = {2026}
}
```
