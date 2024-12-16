from pathlib import Path

import yaml


# Load the YAML configuration
def load_config(yaml_file: Path) -> dict:
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)
    return config
