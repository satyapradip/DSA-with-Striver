# Test all new linked list problems
import subprocess
import sys

def run_test(file_path):
    """Run a test file and return (passed, output)."""
    try:
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

def main():
    files = [
        'linked_list/easy/07_reverse_in_kgroups.py',
        'linked_list/easy/08_reorder_list.py',
        'linked_list/easy/09_check_palindrome_ll.py',
        'linked_list/hard/02_sort_linked_list.py',
    ]

    print("=" * 60)
    print("Running new linked list tests...")
    print("=" * 60)

    all_passed = True
    for file in files:
        print(f"\nTesting: {file}")
        passed, output = run_test(file)
        if passed:
            print("  ✅ PASSED")
        else:
            print("  ❌ FAILED")
            print(output)
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("All new linked list tests PASSED!")
    else:
        print("Some tests FAILED!")
    print("=" * 60)

if __name__ == "__main__":
    main()