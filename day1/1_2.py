import pytest


def calculate_sum(code):
    code_list = [int(digit) for digit in list(code)]
    sum = 0
    step = len(code_list) / 2

    for index, digit in enumerate(code_list):
        real_index = (index + step) if (index + step) < len(code_list) else (index + step) % len(code_list)
        if digit == code_list[int(real_index)]:
            sum += digit

    return sum


@pytest.mark.parametrize("test_input, expected", [
    ("1212", 6),
    ("1221", 0),
    ("123425", 4),
    ("123123", 12),
    ("12131415", 4),
])
def test_calculate_sum(test_input, expected):
    assert calculate_sum(test_input) == expected


if __name__ == '__main__':
    code = open("input", "r").read()
    print("Result: %d" % calculate_sum(code))
