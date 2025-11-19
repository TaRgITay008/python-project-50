from hexlet_code import generate_diff

def test_generate_diff():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert isinstance(result, str)
    assert len(result) > 0
