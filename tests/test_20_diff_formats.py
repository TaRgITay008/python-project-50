from hexlet_code import generate_diff


def test_stylish_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    result = generate_diff(file1, file2, 'stylish')
    assert isinstance(result, str)
    assert result.startswith('{')
    assert result.endswith('}\n')
    assert '+' in result or '-' in result


def test_plain_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    result = generate_diff(file1, file2, 'plain')
    assert isinstance(result, str)
    assert 'was added' in result or 'was removed' in result or 'was updated' in result


def test_json_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    result = generate_diff(file1, file2, 'json')
    assert isinstance(result, str)
    assert result.startswith('[')
    assert result.endswith(']\n')
    assert '"key"' in result and '"type"' in result


def test_default_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'

    result_default = generate_diff(file1, file2)
    result_stylish = generate_diff(file1, file2, 'stylish')

    assert result_default == result_stylish
