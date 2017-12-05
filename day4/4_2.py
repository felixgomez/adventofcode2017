import pytest


def is_valid_password(password):
    password_list = list(map(lambda s: "".join(sorted(s)), password.split()))

    if len(password_list) != len(set(password_list)):
        return False
    return True


@pytest.mark.parametrize("test_input, expected", [
    ("abcde fghij", True),
    ("abcde xyz ecdab", False),
    ("a ab abc abd abf abj", True),
    ("iiii oiii ooii oooi oooo", True),
    ("oiii ioii iioi iiio", False)

])
def test_is_valid_password(test_input, expected):
    assert is_valid_password(test_input) == expected


def count_valid_passwords(passwords):
    count = 0
    for password in passwords:
        if is_valid_password(password):
            count += 1
    return count


if __name__ == '__main__':
    passwords = open("input", "r").read().splitlines()
    print("Number of valid passwords: %d" % count_valid_passwords(passwords))
