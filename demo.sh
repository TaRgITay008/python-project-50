#!/bin/bash
echo "=== Gendiff Demo ==="
echo

echo "1. Stylish format (default):"
echo "gendiff file1.json file2.json"
uv run gendiff file1.json file2.json
echo

echo "2. Plain format:"
echo "gendiff -f plain file1.json file2.json"  
uv run gendiff -f plain file1.json file2.json
echo

echo "3. YAML files with stylish format:"
echo "gendiff file1.yml file2.yml"
uv run gendiff file1.yml file2.yml
echo

echo "4. YAML files with plain format:"
echo "gendiff -f plain file1.yml file2.yml"
uv run gendiff -f plain file1.yml file2.yml
