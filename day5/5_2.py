import pytest


def calculate_steps(jump_offsets):
    position = 0
    steps = 0
    while position < len(jump_offsets):
        new_position = position + jump_offsets[position]
        if jump_offsets[position] > 2:
            jump_offsets[position] -= 1
        else:
            jump_offsets[position] += 1

        position = new_position
        steps += 1
    return steps


@pytest.mark.parametrize("test_input, expected", [
    ([0, 3, 0, 1, -3], 10)
])
def test_calculate_steps(test_input, expected):
    assert calculate_steps(test_input) == expected


if __name__ == '__main__':
    jump_offsets = list(map(int, open("input").read().splitlines()))
    print("Number of steps : %d" % calculate_steps(jump_offsets))
