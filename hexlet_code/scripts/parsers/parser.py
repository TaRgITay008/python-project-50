import json
import yaml

def parse_file(file_path):
    """Parse JSON or YAML file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    if file_path.endswith('.json'):
        return json.loads(content)
    elif file_path.endswith(('.yml', '.yaml')):
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
