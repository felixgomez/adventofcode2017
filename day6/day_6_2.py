import pytest


def redistribution_cycle_number(input):
    states = []
    state = input
    number_of_blocks = len(input)

    while True:
        blocks_to_redistribute = max(state)
        bank_index = state.index(blocks_to_redistribute)

        new_state = list(state)  # copy

        if states.count(new_state) == 1:
            index = states.index(new_state)

        if states.count(new_state) == 2:
            return len(states) - index - 1

        states.append(new_state)

        state[bank_index] = 0
        while blocks_to_redistribute > 0:
            bank_index += 1
            if bank_index == number_of_blocks:
                bank_index = 0
            state[bank_index] += 1
            blocks_to_redistribute -= 1


@pytest.mark.parametrize("test_input, expected", [
    ([0, 2, 7, 0], 4)
])
def test_redistribution_cycle_number(test_input, expected):
    assert redistribution_cycle_number(test_input) == expected


if __name__ == '__main__':
    input = list(map(int, open("input", "r").readline().split()))
    print("Number or cycles: %d" % redistribution_cycle_number(input))
