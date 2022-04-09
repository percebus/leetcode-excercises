import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from lib.palindromes.check.reversing import is_palindrome


def get_limits(chars: int):
    minimum = '1' + ''.join('0' for num in range(0, chars - 1))
    minimum = int(minimum)

    maximum = ''.join('9' for num in range(0, chars))
    maximum = int(maximum)
    return minimum, maximum


def get_largest_paindrome_product(minimum: int, maximum: int):
    for x in reversed(range(minimum, maximum + 1)):
        for y in reversed(range(x, maximum + 1)):
            product = str(x * y)
            print(f'{x}x{y} = {product}')
            if is_palindrome(product):
                return x, y


def format(numbers: tuple):
    return 'x'.join(str(num) for num in numbers)


def run(chars: int, product=None, expected=None):
    minimum, maximum = get_limits(chars)
    result = get_largest_paindrome_product(minimum, maximum)
    assert format(result) == format(expected), f'expected:{expected}, got:{result}'
    x, y = result
    _product = x * y
    assert _product == product, f'expected:{product}, got:{_product}'
    print('✅', end='')


def run_all():
    run(chars=2, product=9009, expected=[91, 99])

    # FIXME
    run(chars=3, product=906609, expected=[924, 962])


if __name__ == '__main__':
    run_all()
