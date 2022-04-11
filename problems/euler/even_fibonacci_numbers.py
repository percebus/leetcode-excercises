

# SRC: https://projecteuler.net/problem=2
def sum_evens(limit=1000):
    x, y = [1, 2]
    num = y
    sum = 0

    # TODO? build fibonacci separately, and then filter?
    while(num <= limit):
        if (num % 2) == 0:
            sum += num

        num = x + y
        x = y
        y = num

    return sum


def run(limit: int, expected: list = None):
    result = sum_evens(limit)
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def run_all():
    #       2
    #       8
    run(10, expected=10)

    #       2
    #       8
    #      34
    run(100, expected=44)

    #       2
    #       8
    #      34
    #     144
    #     610
    run(1000, expected=798)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    run(10000, expected=3382)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    #   10946
    #   46368
    run(100000, expected=60696)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    #   10946
    #   46368
    #  196418
    #  832040
    run(1000000, expected=1089154)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    #   10946
    #   46368
    #  196418
    #  832040
    # 3524578
    run(4000000, expected=4613732)


if __name__ == '__main__':
    run_all()
