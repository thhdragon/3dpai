
# Prunt3D Simulator: Insights & Wishlist

## Quick Navigation & Related Documents
- [Prunt Simulator Reference](prunt_simulator_reference.md)
- [Master Actionable Checklist](master_actionable_checklist.md)
- [Data Engineering & Management Plan](data_engineering_plan.md)

---

## Onboarding & How to Use
**Who should use this?** Anyone evaluating, extending, or integrating the Prunt3D simulator for the 3dpai project.

**How to use:**
- Review the insights and limitations below to understand current simulator capabilities.
- Use the wishlist and mapping table to prioritize enhancements or propose new features.
- For technical details and integration, see the Prunt Simulator Reference.

---

## Rationale for Wishlist & Enhancements
- **Standardization:** Consistent outputs and APIs enable robust automation and easier integration with ML/data pipelines.
- **Performance:** Faster batch simulation and real-time streaming are critical for large-scale data generation and online learning.
- **Extensibility:** Custom failure injection and scenario templates support advanced research and edge case modeling.

---

## Mapping: Current Limitations to Desired Enhancements
| Limitation | Desired Enhancement |
|------------|--------------------|
| Output schema not standardized | Standardized output schema (JSON/YAML) |
| No direct ML API | Python API/CLI for ML integration |
| Limited failure mode injection | Custom failure mode injection support |
| Slow batch simulation | Faster batch/headless mode |
| Verbose G-code not always available | Option for detailed G-code export |
| Data streams not always aligned | Built-in multi-modal alignment |
| Few scenario templates | Library of scenario configs |
| No real-time streaming | Real-time data streaming option |
| Limited environmental modeling | Enhanced environmental effects |
| Sparse user documentation | Expanded docs, code/API examples |

---

## 1. Insights from Simulator Analysis
- Prunt3D provides high-fidelity physics simulation for 3D printing, including thermal, mechanical, and material science modeling.
- The simulator supports multi-modal outputs (G-code, sensor logs, images, audio), which is critical for LLM training.
- Scenario configuration is flexible, allowing for parameter sweeps, failure injection, and domain randomization.
- Current API allows batch simulation and export of structured results, but integration with external ML pipelines could be improved.
- Verbose logging and metadata are available, but not always standardized across runs.
- Real-time simulation speed is variable and may be a bottleneck for large-scale data generation.
- Sensor noise and environmental effects are supported, but some real-world phenomena (e.g., rare hardware faults) are not fully modeled.

---

## 2. Wishlist: Desired Enhancements for Project Fit
- [ ] **Standardized Output Schema:** Ensure all simulation runs output consistent, machine-readable metadata (JSON, YAML) for easy ingestion.
- [ ] **API for Direct ML Integration:** Expose a Python API or CLI hooks for direct invocation from data pipelines and LLM training scripts.
- [ ] **Custom Failure Mode Injection:** Allow user-defined failure scenarios and rare event simulation (e.g., stepper driver faults, filament jams).
- [ ] **Faster Batch Simulation:** Optimize for parallel execution and headless mode to accelerate large-scale scenario generation.
- [ ] **Verbose G-code Export:** Option to export G-code with detailed comments and layer/event markers for downstream parsing.
- [ ] **Multi-Modal Data Alignment:** Built-in synchronization of sensor, image, and audio data streams with G-code timeline.
- [ ] **Scenario Templates:** Library of reusable scenario configs for common print types, materials, and failure cases.
- [ ] **Real-Time Streaming:** Option to stream simulation data for online learning or interactive debugging.
- [ ] **Enhanced Environmental Modeling:** Add support for more complex environmental effects (humidity, airflow patterns, power fluctuations).
- [ ] **User Documentation:** Expand documentation with code examples, API usage, and integration guides for ML workflows.

---

## 3. Open Questions
- What is the best way to synchronize Prunt3D simulation time with real printer logs for sim-to-real transfer?
- How can we validate the fidelity of rare failure mode simulations against real-world data?
- What are the performance limits for batch simulation on available hardware?

---

## 4. Next Steps
- Review and prioritize wishlist items with the team.
- Propose contributions or feature requests to the Prunt3D project.
- Prototype API integration and batch scenario generation workflows.
- Update this document as new insights and requirements emerge.
# Prunt Simulator: Insights & Wishlist for Project Alignment

## Purpose
Capture key insights from a deep dive into the Prunt Simulator and maintain a prioritized wishlist of changes or enhancements to better support the 3dpai project's LLM/data-driven goals.

---

## 1. Insights from Simulator Review
- The simulator is highly modular and physics-accurate, with extensible Ada code and Python utilities for visualization.
- Output data (CSV) is well-structured for kinematic analysis, but field documentation is lacking.
- Real-time and post-process plotting tools are powerful, but could benefit from more multi-modal (e.g., sensor, image, audio) support.
- The TOML config is comprehensive, supporting detailed printer and motion parameterization.
- The build and run process is robust, but assumes familiarity with Ada/Alire and shell scripting.
- The simulator is well-suited for generating synthetic data for LLM training, but integration with automated pipelines is not yet seamless.

---

## 2. Wishlist: Enhancements for Project Fit

### A. Data & Output
- [ ] Add detailed documentation for all CSV output fields (names, units, meaning)
- [ ] Support for additional output formats (JSON, HDF5) for easier downstream integration
- [ ] Option to output multi-modal data (e.g., simulated sensor noise, images, audio)
- [ ] Include run metadata (config, random seed, version) in every output

### B. Usability & Automation
- [ ] Add CLI flags for headless/batch operation (no interactive prompts)
- [ ] Provide Python API or bindings for direct invocation from data pipelines
- [ ] Improve error handling and logging (clear error messages, exit codes)
- [ ] Add example scripts for automated scenario generation and batch runs

### C. Extensibility
- [ ] Modularize Ada code further for easier addition of new kinematic models or sensors
- [ ] Document extension points and provide templates for new features
- [ ] Add hooks for custom event injection (e.g., simulated failures, domain randomization)

### D. Visualization
- [ ] Expand Python plotting utilities to support multi-modal and annotated plots
- [ ] Add support for saving plots/images automatically during batch runs
- [ ] Provide example notebooks for data exploration and LLM training integration

### E. Documentation
- [ ] Expand README and add tutorial-style guides for new users
- [ ] Provide a reference for all config options and their effects
- [ ] Add troubleshooting and FAQ sections

---

## 3. Prioritization & Next Steps
- Review and prioritize wishlist items with the team
- Assign owners for high-impact enhancements
- Track progress and update this doc as changes are made

---
