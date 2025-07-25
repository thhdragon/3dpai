import os
import json
import logging
from typing import Optional

# Configure logging
logging.basicConfig(filename='prunt3d_ingest.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

REQUIRED_FILES = ['print.gcode', 'sensors.csv']  # Extend as needed
OPTIONAL_FILES = ['metadata.json']


def required_files_present(run_folder: str) -> bool:
    for fname in REQUIRED_FILES:
        if not os.path.isfile(os.path.join(run_folder, fname)):
            return False
    return True

def load_gcode(run_folder: str) -> Optional[str]:
    path = os.path.join(run_folder, 'print.gcode')
    with open(path, 'r') as f:
        return f.read()

def load_sensors(run_folder: str) -> Optional[list]:
    path = os.path.join(run_folder, 'sensors.csv')
    with open(path, 'r') as f:
        return f.readlines()

def load_metadata(run_folder: str) -> Optional[dict]:
    path = os.path.join(run_folder, 'metadata.json')
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return json.load(f)
    return None

def validate_schema(sensors: list, metadata: Optional[dict]) -> bool:
    # Placeholder: implement schema checks as needed
    return True

def check_consistency(sensors: list, gcode: str) -> bool:
    # Placeholder: implement cross-modality consistency checks
    return True

def save_validated_run(run_folder: str):
    # Placeholder: could move/copy to a validated/ directory or mark as valid
    pass

def ingest_sim_data(sim_data_root: str):
    for run_id in os.listdir(sim_data_root):
        run_folder = os.path.join(sim_data_root, run_id)
        if not os.path.isdir(run_folder):
            continue
        logging.info(f"Processing {run_folder}")
        if not required_files_present(run_folder):
            logging.error(f"{run_folder}: Missing required files")
            continue
        try:
            gcode = load_gcode(run_folder)
            sensors = load_sensors(run_folder)
            metadata = load_metadata(run_folder)
            if gcode is None or sensors is None:
                logging.error(f"{run_folder}: Failed to load required files (gcode or sensors)")
                continue
            if not validate_schema(sensors, metadata):
                logging.error(f"{run_folder}: Schema mismatch")
                continue
            if not check_consistency(sensors, gcode):
                logging.error(f"{run_folder}: Inconsistent data")
                continue
            save_validated_run(run_folder)
            logging.info(f"{run_folder}: Ingestion successful")
        except Exception as e:
            logging.error(f"{run_folder}: {str(e)}")
            continue
    logging.info("Ingestion complete. See log for details.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python prunt3d_ingest.py <sim_data_root>")
        exit(1)
    ingest_sim_data(sys.argv[1])
