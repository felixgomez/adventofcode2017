import pytest
import math


def calculate_manhattan_distance_from_origin(number):
    matrix_range = math.ceil(math.sqrt(number))
    x = y = 0
    dx = 0
    dy = -1
    for i in range(matrix_range ** 2):
        if (-matrix_range / 2 < x <= matrix_range / 2) and (-matrix_range / 2 < y <= matrix_range / 2):
            if number == i + 1:
                return abs(x) + abs(y)

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


@pytest.mark.parametrize("test_input, expected", [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31)
])
def test_calculate_manhattan_distance_from_origin(test_input, expected):
    assert calculate_manhattan_distance_from_origin(test_input) == expected


if __name__ == '__main__':
    number = 347991
    print("Manhattan distance: %d" % calculate_manhattan_distance_from_origin(347991))
