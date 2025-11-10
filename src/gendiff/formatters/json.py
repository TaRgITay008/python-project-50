#!/usr/bin/env python3
"""JSON formatter module."""
import json


def format_json(diff):
    """Format diff in JSON format."""
    return json.dumps(diff, indent=2)
