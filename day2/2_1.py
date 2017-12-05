import pytest


def calculate_checksum(code):
    sum = 0

    matrix = obtain_matrix_from_code(code)
    for row in matrix:
        sum += max(row) - min(row)
    return sum


def obtain_matrix_from_code(code):
    matrix = []
    lines = code.splitlines()
    for line in lines:
        matrix.append(list(map(int, line.split())))
    return matrix


@pytest.mark.parametrize("test_input, expected", [
    ("""5 1 9 5
7 5 3
2 4 6 8""", 18)
])
def test_calculate_checksum(test_input, expected):
    assert calculate_checksum(test_input) == expected


if __name__ == '__main__':
    code = open("input", "r").read()
    print("Result: %d" % calculate_checksum(code))
