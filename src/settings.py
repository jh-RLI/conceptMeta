"""
Use this file to add static variables like paths ...
"""

from pathlib import Path

from config.utils import load_config

BASE_PATH = Path.cwd()
MODLUE_PATH = Path(BASE_PATH / "src")
INPUT_CONFIG = Path(MODLUE_PATH / "config" / "config.yml")

OUTPUT_PATH = Path(BASE_PATH / "output")


# Load configuration
config = load_config(INPUT_CONFIG)  # Replace with your YAML file path
# Access the ETL processes
ETL_PROCESSES: list = config.get("etl_processes", [])
