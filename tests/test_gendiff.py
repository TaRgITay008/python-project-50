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
