

# SRC: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p001.py?ts=4
def sum_multiples_nayuki(limit):
    return sum(x for x in range(limit) if (x % 3 == 0 or x % 5 == 0))


# SRC: https://projecteuler.net/problem=1
def sum_multiples(limit, multiples):
    nums = set(
        num
        for num in range(limit)
        for multiple in multiples
        if (num % multiple) == 0)

    return sum(nums)


def test(limit: int, multiples: list = [3, 5], expected: list = None):
    result = sum_multiples(limit, multiples)  # FIXME?
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def test_all():
    # If we list all the natural numbers below 10 that are multiples of 3 or 5,
    # we get 3, 5, 6 and 9. The sum of these multiples is 23.
    test(10, expected=23)

    # Find the sum of all the multiples of 3 or 5 below 1000.
    test(1000, expected=233168)


if __name__ == '__main__':
    test_all()
