import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from problems.euler.multiples_of_3_or_5.percebus import sum_multiples


def run(limit: int, multiples: list = [3, 5], expected: list = None):
    result = sum_multiples(limit, multiples)  # FIXME?
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def run_all():
    # If we list all the natural numbers below 10 that are multiples of 3 or 5,
    # we get 3, 5, 6 and 9. The sum of these multiples is 23.
    run(10, expected=23)

    # Find the sum of all the multiples of 3 or 5 below 1000.
    run(1000, expected=233168)


if __name__ == '__main__':
    run_all()
