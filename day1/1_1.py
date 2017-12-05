import pytest


def calculate_sum(code):
    code_list = [int(digit) for digit in list(code)]
    sum = 0

    for index, digit in enumerate(code_list):
        next_index = (index + 1) if (index + 1) < len(code_list) else (index + 1) % len(code_list)
        if digit == code_list[next_index]:
            sum += digit
    return sum


@pytest.mark.parametrize("test_input, expected", [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9)
])
def test_calculate_sum(test_input, expected):
    assert calculate_sum(test_input) == expected


if __name__ == '__main__':
    code = open("input", "r").read()
    print("Result: %d" % calculate_sum(code))
