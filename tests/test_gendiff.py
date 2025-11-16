#!/usr/bin/env python3
"""Tests for gendiff."""

import pytest
from gendiff import generate_diff


def test_generate_diff_function_exists():
    """Test that generate_diff function exists."""
    assert callable(generate_diff)


def test_generate_diff_returns_string():
    """Test that generate_diff returns string."""
    # Это базовый тест
    result = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    )
    assert isinstance(result, str)
