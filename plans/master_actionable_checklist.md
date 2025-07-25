
# Master Actionable Checklist: 3dpai Project

## Purpose
A unified, actionable checklist covering all major phases and deliverables for the 3dpai project. This document is the central hub for project tracking, accountability, and onboarding. It should be regularly updated and referenced by all contributors.

---

## Quick Navigation & Related Documents
- [Data Engineering & Management Plan](data_engineering_plan.md)
- [LLM Training & Fine-Tuning Strategy](llm_training_strategy.md)
- [Evaluation & Benchmarking Plan](evaluation_benchmarks_plan.md)
- [Risk Assessment & Mitigation Plan](risk_mitigation_plan.md)
- [Brainstorming & Open Questions](brainstorming_notes.md)
- [Prunt3D Ingestion Design](prunt3d_ingest_design.md)

---

## Onboarding Notes
- **Who should use this?** Anyone contributing to the 3dpai project, from new team members to core developers.
- **How to use:**
  - Review the checklist below and find tasks that match your skills or interests.
  - Check the "Owner" and "Status" columns to see what is in progress or needs help.
  - For details, follow the links in the "Reference" column.
  - Update your progress and notes as you work (or ping the project lead).
- **Where to start:** If new, begin with the Data Pipeline or LLM Training sections, or review the Brainstorming Notes for open research questions.

---

## Progress Tracking Table

| Task | Owner | Status | Due Date | Reference |
|------|-------|--------|----------|-----------|
| Prunt3D Ingestion Script |  | Not Started |  | [Data Pipeline](#1-data-pipeline-step-by-step-tutorial) |
| Verbose G-code Parser |  | Not Started |  | [Data Pipeline](#1-data-pipeline-step-by-step-tutorial) |
| Feature Extraction Module |  | Not Started |  | [Data Pipeline](#1-data-pipeline-step-by-step-tutorial) |
| Multi-Modal Alignment Tool |  | Not Started |  | [Data Pipeline](#1-data-pipeline-step-by-step-tutorial) |
| Dataset Versioning & Organization |  | Not Started |  | [Data Pipeline](#1-data-pipeline-step-by-step-tutorial) |
| Pipeline Automation & Testing |  | Not Started |  | [Data Pipeline](#1-data-pipeline-step-by-step-tutorial) |
| LLM Training (Unsloth) |  | Not Started |  | [LLM Training](#2-llm-training-fine-tuning-step-by-step-tutorial) |
| LLM Training (smol-course/HF) |  | Not Started |  | [LLM Training](#2-llm-training-fine-tuning-step-by-step-tutorial) |
| Data Loader Integration |  | Not Started |  | [LLM Training](#2-llm-training-fine-tuning-step-by-step-tutorial) |
| Training/Evaluation Loop |  | Not Started |  | [LLM Training](#2-llm-training-fine-tuning-step-by-step-tutorial) |
| Model Export & Deployment |  | Not Started |  | [LLM Training](#2-llm-training-fine-tuning-step-by-step-tutorial) |
| Evaluation Harness |  | Not Started |  | [Evaluation & Benchmarking](#3-evaluation-benchmarking-step-by-step-tutorial) |
| Monitoring & Dashboard |  | Not Started |  | [Evaluation & Benchmarking](#3-evaluation-benchmarking-step-by-step-tutorial) |
| A/B Testing & Regression |  | Not Started |  | [Evaluation & Benchmarking](#3-evaluation-benchmarking-step-by-step-tutorial) |
| Human-in-the-Loop Review |  | Not Started |  | [Evaluation & Benchmarking](#3-evaluation-benchmarking-step-by-step-tutorial) |
| FMEA Tables |  | Not Started |  | [Risk Mitigation](#4-risk-mitigation-safety) |
| Monitoring/Alerting Scripts |  | Not Started |  | [Risk Mitigation](#4-risk-mitigation-safety) |
| Emergency Stop/Fallback Logic |  | Not Started |  | [Risk Mitigation](#4-risk-mitigation-safety) |
| Diagrams & Documentation |  | Not Started |  | [Diagrams & Docs](#5-diagrams-documentation) |
| Open Questions & Research Assignments |  | Not Started |  | [Open Questions](#6-open-questions-research-assignments) |
| Project Tracking Setup |  | Not Started |  | [Project Tracking](#7-project-tracking) |

---

## 1. Data Pipeline (Step-by-Step Tutorial)

### 1.1 Prunt3D Ingestion Script
- [ ] Create a new Python file `prunt3d_ingest.py` in the project root.
- [ ] Define required and optional input files (e.g., `print.gcode`, `sensors.csv`, `metadata.json`).
- [ ] Write a function to check for required files in each simulation run folder.
- [ ] Write functions to load and validate each file (G-code, sensors, metadata).
- [ ] Implement schema and consistency checks (e.g., timestamps, layer counts).
- [ ] Add logging for successes, errors, and skipped runs.
- [ ] Test the script on a sample directory of Prunt3D outputs.
- [ ] Review and document usage in a README section.

### 1.2 Verbose G-code Parser
- [ ] Create a new Python file `gcode_verbose_parser.py`.
- [ ] Write a parser to extract comments, metadata, and layer info from verbose G-code files.
- [ ] Output structured data (e.g., JSON or CSV) for downstream use.
- [ ] Add unit tests for edge cases (missing comments, malformed lines).
- [ ] Document parser usage and expected input/output.

### 1.3 Feature Extraction/Engineering
- [ ] Create a module `feature_extraction.py`.
- [ ] Implement functions to extract trends and metrics from sensor logs.
- [ ] Integrate with parsed G-code and metadata.
- [ ] Output feature vectors for each print session.
- [ ] Add tests and document feature definitions.

### 1.4 Multi-Modal Alignment
- [ ] Create a script `align_modalities.py`.
- [ ] Write logic to synchronize time series (sensor, G-code, images, audio) to a common timeline.
- [ ] Validate alignment with sample data.
- [ ] Document alignment process and assumptions.

### 1.5 Dataset Organization & Versioning
- [ ] Define directory structure for processed data (by phase, modality, scenario).
- [ ] Integrate DVC or similar tool for dataset versioning.
- [ ] Write a script to generate metadata files for each dataset version.
- [ ] Document organization and versioning workflow.

### 1.6 Automation & Testing
- [ ] Develop ETL pipeline scripts/workflows to automate all above steps.
- [ ] Write integration tests for the full pipeline.
- [ ] Set up logging and error reporting for pipeline runs.
- [ ] Document the full pipeline in a tutorial-style guide.

## 2. LLM Training & Fine-Tuning (Step-by-Step Tutorial)

### 2.1 Unsloth-Based LLM Training
- [ ] Set up a Python environment with Unsloth and required dependencies.
- [ ] Prepare a configuration file specifying dataset paths, model parameters, and hardware settings.
- [ ] Write a script to load processed datasets and initialize the Unsloth training pipeline.
- [ ] Implement training loop with checkpointing and logging.
- [ ] Validate model outputs on a held-out validation set.
- [ ] Export the trained model in ONNX, GGUF, or other required formats.
- [ ] Document the training process and configuration options.

### 2.2 Smol-Course/HuggingFace Prototyping
- [ ] Set up a Python environment with HuggingFace Transformers and smol-course code.
- [ ] Write a script to load a small dataset and run a prototype fine-tuning job.
- [ ] Compare results and resource usage with Unsloth pipeline.
- [ ] Document prototyping workflow and lessons learned.

### 2.3 Data Loader Integration
- [ ] Implement data loader modules for processed datasets (simulation, real-world, multi-modal).
- [ ] Test data loaders with both Unsloth and HuggingFace pipelines.
- [ ] Document data loader interfaces and usage.

### 2.4 Training/Evaluation Loop
- [ ] Write a unified training/evaluation loop script with support for checkpoints, logging, and early stopping.
- [ ] Integrate evaluation metrics (print success prediction, failure detection, etc.).
- [ ] Document loop usage and configuration.

### 2.5 Model Export & Deployment
- [ ] Write scripts to export trained models to ONNX, GGUF, or other formats.
- [ ] Develop deployment scripts for integration with downstream systems (e.g., Klipper, Prunt3D).
- [ ] Document deployment process and requirements.

### 2.6 Documentation
- [ ] Write a tutorial-style guide for the full LLM training and fine-tuning workflow.

## 3. Evaluation & Benchmarking (Step-by-Step Tutorial)

### 3.1 Evaluation Harness
- [ ] Create a Python module `evaluation_harness.py`.
- [ ] Define evaluation metrics (accuracy, recovery rate, print quality, etc.).
- [ ] Write functions to load test sets and run model inference.
- [ ] Output evaluation results in structured format (CSV, JSON).
- [ ] Add unit tests for metric calculations.
- [ ] Document harness usage and expected outputs.

### 3.2 Continuous Monitoring & Dashboard
- [ ] Set up a monitoring script or service to track key metrics over time.
- [ ] Integrate with a dashboard tool (e.g., Grafana, Streamlit, custom web UI).
- [ ] Document dashboard setup and usage.

### 3.3 A/B Testing & Regression
- [ ] Write scripts to compare new model versions against baselines.
- [ ] Automate regression testing for critical outputs.
- [ ] Document A/B testing process and criteria.

### 3.4 Human-in-the-Loop Review
- [ ] Develop a process for expert review of model outputs (e.g., print failure explanations).
- [ ] Document review workflow and feedback integration.

### 3.5 Documentation
- [ ] Write a tutorial-style guide for evaluation and benchmarking workflows.

## 4. Risk Mitigation & Safety
- [ ] Complete FMEA tables for all critical components
- [ ] Implement monitoring and alerting scripts (safety, data drift, failures)
- [ ] Emergency stop and fallback logic in control scripts
- [ ] Document all risk protocols and playbooks

## 5. Diagrams & Documentation
- [ ] Data pipeline workflow diagram
- [ ] LLM training workflow diagram
- [ ] Evaluation/monitoring flowchart
- [ ] Architecture overview diagram
- [ ] Update all planning docs with actionable checklists

## 6. Open Questions & Research Assignments
- [ ] Review and assign all open questions in brainstorming_notes.md
- [ ] Schedule regular review of research progress
- [ ] Update checklist as questions are resolved

## 7. Project Tracking
- [ ] Set up a project board or issue tracker (optional)
- [ ] Regularly update checklist status and assignments

---

## Notes
- Each item should be broken down into smaller tasks as needed and assigned to responsible contributors.
- Checklist should be reviewed and updated at each project milestone or sprint.
