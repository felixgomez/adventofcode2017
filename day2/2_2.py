import pytest


def calculate_checksum(code):
    sum = 0

    matrix = obtain_matrix_from_code(code)
    for row in matrix:
        row.sort(reverse=True)
        for index, digit in enumerate(row):
            for divisor in row[(index + 1):]:
                if digit % divisor == 0:
                    sum += int(digit / divisor)

    return sum


def obtain_matrix_from_code(code):
    matrix = []
    lines = code.splitlines()
    for line in lines:
        matrix.append(list(map(int, line.split())))

    return matrix


@pytest.mark.parametrize("test_input, expected", [
    ("""5 9 2 8
9 4 7 3
3 8 6 5""", 9)
])
def test_calculate_checksum(test_input, expected):
    assert calculate_checksum(test_input) == expected


if __name__ == '__main__':
    code = open("input", "r").read()
    print("Result: %d" % calculate_checksum(code))
