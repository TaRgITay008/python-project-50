try:
    from gendiff import generate_diff
    print("SUCCESS: from gendiff import generate_diff")
except ImportError as e:
    print(f"FAILED: from gendiff import generate_diff - {e}")

try:
    from hexlet_code import generate_diff
    print("SUCCESS: from hexlet_code import generate_diff")
except ImportError as e:
    print(f"FAILED: from hexlet_code import generate_diff - {e}")

try:
    from hexlet_code.scripts.gendiff import generate_diff
    print("SUCCESS: from hexlet_code.scripts.gendiff import generate_diff")
except ImportError as e:
    print(f"FAILED: from hexlet_code.scripts.gendiff import generate_diff - {e}")

try:
    import gendiff
    print("SUCCESS: import gendiff")
except ImportError as e:
    print(f"FAILED: import gendiff - {e}")

try:
    import hexlet_code
    print("SUCCESS: import hexlet_code")
except ImportError as e:
    print(f"FAILED: import hexlet_code - {e}")
