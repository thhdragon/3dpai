
# Prunt3D Simulation Output Ingestion Script: Design

## Quick Navigation & Related Documents
- [Master Actionable Checklist](master_actionable_checklist.md)
- [Data Engineering & Management Plan](data_engineering_plan.md)
- [Prunt Simulator Reference](prunt_simulator_reference.md)

---

## Onboarding & How to Use
**Who should use this?** Anyone implementing or maintaining the data ingestion pipeline for Prunt3D simulation outputs.

**How to use:**
- Review the supported input formats and directory structure below.
- Reference the rationale for ingestion design and example log entries for implementation guidance.
- For downstream data requirements, see the Data Engineering & Management Plan.

---

## Rationale for Ingestion Design
- **Modular Validation:** Each file type (G-code, sensors, images, audio) is validated independently to maximize robustness and allow partial ingestion.
- **Schema Compliance:** Enforces consistency and enables downstream automation by ensuring all data matches expected formats.
- **Comprehensive Logging:** All actions and errors are logged for traceability and debugging.

---

## Example Log Entries
```text
INFO 2025-07-24 12:00:01 [ingest] Processing run: run_00001
SUCCESS 2025-07-24 12:00:02 [ingest] All required files present for run_00001
ERROR 2025-07-24 12:00:03 [ingest] sensors.csv missing required column: vibration
WARNING 2025-07-24 12:00:04 [ingest] Incomplete image set for run_00002, continuing with available data
SUMMARY 2025-07-24 12:00:10 [ingest] 10 runs processed, 8 successful, 2 with errors
```

---

## 1. Supported Input Formats
- **G-code files**: `.gcode` (plain or verbose)
- **Sensor logs**: `.csv`, `.json`, or similar (temperature, position, etc.)
- **Images**: `.png`, `.jpg` (layer snapshots, camera feeds)
- **Audio**: `.wav`, `.mp3` (if available)

---

## 2. Directory/File Structure Expectations
- Each simulation run is stored in a dedicated folder:
  - `/sim_data/<run_id>/`
    - `print.gcode`
    - `sensors.csv` or `sensors.json`
    - `images/` (optional, per-layer or per-event)
    - `audio/` (optional)
    - `metadata.json` (optional, for run parameters)

---

## 3. Validation Checks
- **File presence**: All required files exist for each run
- **File integrity**: Files are readable, not empty, and parseable
- **Schema compliance**: Sensor logs and metadata match expected fields
- **Consistency**: Timestamps and layer/event counts align across modalities
- **Logging**: All validation steps and errors are logged for review

---

## 4. Logging & Error Handling
- Log all ingestion attempts, successes, and failures (with reasons)
- Skip or quarantine incomplete/corrupt runs, but continue processing others
- Generate a summary report after each batch ingestion

---

## 5. Output
- Structured, validated data folders ready for downstream preprocessing
- Summary log/report of ingestion results

---

## 6. Pseudocode Outline

```python
for run_folder in sim_data_root:
    log(f"Processing {run_folder}")
    if not required_files_present(run_folder):
        log_error(run_folder, "Missing required files")
        continue
    try:
        gcode = load_gcode(run_folder)
        sensors = load_sensors(run_folder)
        images = load_images(run_folder)
        audio = load_audio(run_folder)
        metadata = load_metadata(run_folder)
        if not validate_schema(sensors, metadata):
            log_error(run_folder, "Schema mismatch")
            continue
        if not check_consistency(sensors, images, gcode):
            log_error(run_folder, "Inconsistent data")
            continue
        save_validated_run(run_folder)
    except Exception as e:
        log_error(run_folder, str(e))
        continue
log("Ingestion complete. See report for details.")
```

---

## 7. Open Questions
- What is the minimum required set of files for a valid run?
- How to handle optional modalities (images, audio) in downstream steps?
- Should ingestion auto-fix minor schema mismatches or only log them?

---
