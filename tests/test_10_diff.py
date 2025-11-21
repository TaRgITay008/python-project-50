import os
import pytest
from hexlet_code import generate_diff

def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

def read_fixture(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read()

def test_gendiff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_fixture('result_stylish.txt')
    assert generate_diff(file1, file2) == expected

def test_gendiff_yml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected = read_fixture('result_stylish.txt')
    assert generate_diff(file1, file2) == expected

def test_gendiff_plain_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_fixture('result_plain.txt')
    assert generate_diff(file1, file2, 'plain') == expected

def test_gendiff_json_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = read_fixture('result_json.txt')
    assert generate_diff(file1, file2, 'json') == expected
