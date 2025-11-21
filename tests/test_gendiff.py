import os

import pytest

from hexlet_code import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def read_fixture(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read()


@pytest.mark.parametrize("file1, file2, format_name, expected", [
    ('file1.json', 'file2.json', 'stylish', 'result_stylish.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'result_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'result_plain.txt'),
    ('file1.yml', 'file2.yml', 'plain', 'result_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'result_json.txt'),
    ('file1.yml', 'file2.yml', 'json', 'result_json.txt'),
])
def test_generate_diff(file1, file2, format_name, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_result = read_fixture(expected)

    result = generate_diff(file1_path, file2_path, format_name)
    assert result == expected_result


def test_generate_diff_default_format():
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    expected_result = read_fixture('result_stylish.txt')

    result = generate_diff(file1_path, file2_path)
    assert result == expected_result
