import math


def calculate_next_value(number):
    matrix_range = math.ceil(math.sqrt(number))
    x = y = 0
    dx = 0
    dy = -1
    matrix = [[0 for x in range(matrix_range)] for y in range(matrix_range)]
    matrix[0][0] = 1
    for i in range(matrix_range ** 2):
        if (-matrix_range / 2 < x <= matrix_range / 2) and (-matrix_range / 2 < y <= matrix_range / 2):
            sum = 0

            for x_prime in range(x - 1, x + 2):
                for y_prime in range(y - 1, y + 2):
                    sum += matrix[x_prime][y_prime]

            matrix[x][y] = sum
            if sum > number:
                return sum

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


if __name__ == '__main__':
    number = 347991
    print("Next value from number %d is %d" % (number, calculate_next_value(number)))
