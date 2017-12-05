import pytest


def is_valid_password(password):
    password_chunk = password.split()
    if len(password_chunk) != len(set(password_chunk)):
        return False
    return True


@pytest.mark.parametrize("test_input, expected", [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd aa", False),
    ("aa bb cc dd aaa", True)

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
