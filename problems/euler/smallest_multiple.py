

def is_divisible(x: int, limit: int):
    for i in reversed(range(1, limit + 1)):
        if x % i != 0:
            return False
    return True


# SRC: https://projecteuler.net/problem=5
def smallest_divisible(limit: int) -> int:
    step = limit * (limit -1)
    x = step
    while not is_divisible(x, limit):
        x += step
    return x


def run(limit, expected=None):
    result = smallest_divisible(limit)
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def run_all():
    # 2520 is the smallest number that can be divided
    # by each of the numbers from 1 to 10 without any remainder.
    run(10, expected=2520)

    # What is the smallest positive number that is evenly divisible
    # by all of the numbers from 1 to 20?
    run(20, expected=232792560)


if __name__ == '__main__':
    run_all()
