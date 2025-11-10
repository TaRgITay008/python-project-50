#!/usr/bin/env python3
import json
import yaml


def parse_file(file_path):
    """Read and parse file based on its extension."""
    with open(file_path) as file:
        content = file.read()
    
    if file_path.endswith(('.yml', '.yaml')):
        return yaml.safe_load(content)
    elif file_path.endswith('.json'):
        return json.loads(content)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
