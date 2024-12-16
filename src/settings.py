"""
Use this file to add static variables like paths ...
"""

from pathlib import Path

from config.utils import load_config

BASE_PATH = Path.cwd()
MODLUE_PATH = Path(BASE_PATH / "src")
INPUT_CONFIG = Path(MODLUE_PATH / "config" / "config.yml")

# Load configuration
config = load_config(INPUT_CONFIG)  # Replace with your YAML file path

# Combine metadata_storage_path and metadata_document_name
METADATA_FILE_PATH_STRING = (
    f"{config['etl_processes']['metadata_storage_path']}"
    f"{config['etl_processes']['metadata_document_name']}.xml"
)

META_FILE_PATH = Path(BASE_PATH / METADATA_FILE_PATH_STRING)
