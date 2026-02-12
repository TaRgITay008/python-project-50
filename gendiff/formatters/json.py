import json


def render_json(diff):
    return json.dumps(diff, indent=2)
