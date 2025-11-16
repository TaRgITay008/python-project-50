#!/usr/bin/env python3
"""Tests for gendiff."""

import pytest
import os
from gendiff import generate_diff


def test_generate_diff_function_exists():
    """Test that generate_diff function exists."""
    assert callable(generate_diff)


def test_generate_diff_returns_string():
    """Test that generate_diff returns string."""
    # Проверяем что файлы существуют
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    
    if os.path.exists(file1) and os.path.exists(file2):
        result = generate_diff(file1, file2)
        assert isinstance(result, str)
    else:
        # Если файлов нет, просто проверяем что функция работает
        pytest.skip("Test files not found")


def test_generate_diff_with_different_formats():
    """Test generate_diff with different formats."""
    file1_json = 'tests/fixtures/file1.json'
    file2_json = 'tests/fixtures/file2.json'
    file1_yml = 'tests/fixtures/file1.yml'
    file2_yml = 'tests/fixtures/file2.yml'
    
    if (os.path.exists(file1_json) and os.path.exists(file2_json) and
        os.path.exists(file1_yml) and os.path.exists(file2_yml)):
        
        # Test JSON files
        result_json = generate_diff(file1_json, file2_json)
        assert isinstance(result_json, str)
        
        # Test YAML files
        result_yml = generate_diff(file1_yml, file2_yml)
        assert isinstance(result_yml, str)
        
        # Test different formats
        result_plain = generate_diff(file1_json, file2_json, 'plain')
        assert isinstance(result_plain, str)
        
        result_stylish = generate_diff(file1_json, file2_json, 'stylish')
        assert isinstance(result_stylish, str)
    else:
        pytest.skip("Test files not found")
