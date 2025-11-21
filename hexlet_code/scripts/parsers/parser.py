import json
import os

import yaml


def parse_file(file_path):
    """Parse JSON or YAML file."""
    _, extension = os.path.splitext(file_path)

    with open(file_path, 'r') as file:
        if extension.lower() in ('.yaml', '.yml'):
            return yaml.safe_load(file)
        elif extension.lower() == '.json':
            return json.load(file)
        else:
            raise ValueError(f"Unsupported file format: {extension}")
