## Actionable Checklist (Step-by-Step Tutorial)

### 1. Finalize Workflow & Tool Selection
- [ ] Review phased workflow and tool options with team
- [ ] Decide on primary training framework (Unsloth, smol-course, or both)
- [ ] Document rationale and configuration

### 2. Data Loader Implementation
- [ ] Write a data loader for processed datasets (simulation, real-world, multi-modal)
- [ ] Test loader with sample data and training scripts
- [ ] Document loader usage and expected formats

### 3. LLM Training Scripts
- [ ] Script Unsloth-based training pipeline (configurable for dataset, hardware)
- [ ] Script smol-course/HuggingFace-based prototyping pipeline
- [ ] Add checkpointing, logging, and validation hooks
- [ ] Document script usage and configuration

### 4. Evaluation Integration
- [ ] Integrate evaluation checkpoints into training loop
- [ ] Define and implement evaluation metrics
- [ ] Document evaluation process and results

### 5. Documentation
- [ ] Write a tutorial-style guide for the full LLM training and fine-tuning workflow

## Actionable Checklist
- [ ] Finalize phased workflow and tool selection
- [ ] Implement data loader for processed datasets
- [ ] Script LLM training (Unsloth, smol-course)
- [ ] Integrate evaluation checkpoints
- [ ] Document training configs and results


# LLM Training & Fine-Tuning Strategy

## Quick Navigation & Related Documents
- [Master Actionable Checklist](master_actionable_checklist.md)
- [Data Engineering & Management Plan](data_engineering_plan.md)
- [Evaluation & Benchmarking Plan](evaluation_benchmarks_plan.md)

---

## Onboarding & How to Use
**Who should use this?** Anyone working on LLM training, fine-tuning, or evaluation for the 3dpai project.

**How to use:**
- Review the phased workflow and tool options below.
- Use the actionable checklist to track your progress.
- Reference the example config and command-line snippets for quick setup.
- For data requirements, see the Data Engineering & Management Plan.

---

## Rationale for Tool Selection
- **Unsloth:** Chosen for its high efficiency and scalability in LLM fine-tuning, especially for large datasets and distributed training.
- **smol-course/HuggingFace:** Used for rapid prototyping, educational purposes, and smaller-scale experiments. Provides flexibility and access to a wide range of models.

---

## Example Training Config (Unsloth)
```yaml
model: deepseek-r1-distill-qwen-1.5b-gguf
dataset_path: /data/processed/phase1_simulation/
batch_size: 32
learning_rate: 2e-5
epochs: 3
output_dir: /models/phase1_qwen_finetuned/
eval_interval: 1000
checkpoint_interval: 5000
log_dir: /logs/unsloth/
```

**Example Command:**
```bash
python train_unsloth.py --config config.yaml
```

---

## 1. Overview & Phased Workflow

### A. Simulation-First Pretraining
- Train on Prunt3D-generated synthetic data for physics-perfect understanding
- Use Unsloth or smol-course for efficient large-scale fine-tuning

### B. Domain Adaptation (Sim-to-Real)
- Progressive noise injection and domain randomization
- Transfer learning and feature alignment
- Validation with Virtual Klipper Printer

### C. Real-World Refinement
- Fine-tune on real print data (carefully curated)
- Safety-first, conservative learning rate, human-in-the-loop

---

## 2. Tooling & Framework Selection

| Tool/Framework | Strengths | Limitations | Best Use |
|---|---|---|---|
| Unsloth | High efficiency, low memory, fast | Newer, less community support | Large-scale, cost-sensitive training |
| smol-course | Simple, educational, HuggingFace-based | Not optimized for scale | Prototyping, small models, rapid iteration |
| HuggingFace Transformers | Mature, flexible | Higher resource use | Custom pipelines, integration |

**Decision Criteria:**
- Dataset size and complexity
- Hardware availability (GPU/TPU/RAM)
- Need for rapid iteration vs. production scale

---


## 3. Data Pipeline Integration

### Step-by-Step Workflow
1. **Data Ingestion**
    - Collect simulation data from Prunt3D (G-code, sensor logs, images, audio)
    - Gather real-world print data (logs, sensor streams, user feedback)
    - Aggregate multi-modal data (text, images, audio, sensor time series)
2. **Data Cleaning & Validation**
    - Remove corrupt/incomplete records
    - Validate data consistency and labeling
    - Normalize units and formats
3. **Preprocessing & Feature Engineering**
    - Tokenize G-code and configuration files
    - Extract features from sensor data (e.g., temperature trends, vibration signatures)
    - Encode images and audio (if used)
    - Align multi-modal data to common timeline
4. **Augmentation & Synthesis**
    - Generate synthetic variations (parameter sweeps, noise injection)
    - Simulate rare failure modes
5. **Dataset Organization & Versioning**
    - Structure datasets by phase (simulation, adaptation, real-world)
    - Maintain metadata and provenance for reproducibility
    - Use DVC or similar tools for version control
6. **Pipeline Automation**
    - Implement scripts/workflows for repeatable preprocessing
    - Integrate with training frameworks (Unsloth, smol-course, HuggingFace)

---
## 9. Phased Implementation Plan

### Phase 1: Simulation-First Pretraining
- Build and validate data pipeline for Prunt3D simulation data
- Train initial LLM using Unsloth or smol-course
- Evaluate on synthetic benchmarks

### Phase 2: Domain Adaptation (Sim-to-Real)
- Expand pipeline to include domain-randomized and noise-augmented data
- Fine-tune LLM with transfer learning techniques
- Validate with Virtual Klipper Printer and domain-adapted benchmarks

### Phase 3: Real-World Refinement
- Integrate real print data into pipeline (with safety checks)
- Human-in-the-loop fine-tuning and evaluation
- Deploy and monitor in controlled real-world settings

### Milestones & Dependencies
- Data pipeline automation and validation
- Model training and evaluation at each phase
- Feedback loop for continuous improvement

---

---

## 4. Hardware & Compute Requirements
- GPU/TPU specs for each phase (simulation, adaptation, real-world)
- Storage and I/O considerations for large datasets
- Distributed training options (if needed)

---

## 5. Evaluation & Validation
- Metrics: print success prediction, failure mode detection, G-code generation quality
- Validation sets: simulation, domain-adapted, real-world
- Checkpoints: phase transitions, model selection, ablation studies

---

## 6. Integration with Main Project
- Model export and deployment (ONNX, PyTorch, GGUF, etc.)
- API/interface for Klipper/Prunt3D integration
- Continuous learning and feedback loop

---

## 7. Key Open Questions & Research Topics
- What are the limits of sim-to-real transfer for 3D printing physics?
- How to best combine Unsloth and smol-course workflows for hybrid pipelines?
- What multi-modal architectures are most effective for this domain?
- How to ensure safety and reliability in autonomous LLM-driven printer control?
- What are the best practices for uncertainty quantification in this context?

---

## 8. Placeholders for Diagrams & Decision Tables
- [ ] Workflow diagram: end-to-end LLM training pipeline
- [ ] Tool selection matrix
- [ ] Data flow and integration map
- [ ] Evaluation/validation flowchart

---

## LLM Training Resources
- **Unsloth:** https://docs.unsloth.ai/ — High-efficiency LLM fine-tuning library for large-scale, cost-effective training.
- **smol-course:** https://github.com/huggingface/smol-course — Educational resource and code for LLM fine-tuning, especially for smaller models and rapid prototyping.
