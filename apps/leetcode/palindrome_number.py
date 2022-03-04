import math


def split_num(number):
    string = str(number)
    size = len(string)
    is_even = size % 2 == 0
    mid = math.ceil(size / 2) - 1
    prefix = string[:mid + 1]
    if is_even:
        mid += 1
    suffix = string[mid:]
    return prefix, suffix


def is_palindrome(number):
    prefix, suffix = split_num(number)
    last = suffix[::-1]
    return prefix == last


def run(number, expected=None):
    result = is_palindrome(number)
    print(f'{number}: {result}')
    assert result == expected


def run_all():
    # Input: x = 121
    # Output: true
    # Explanation: 121 reads as 121 from left to right and from right to left.
    run(121, expected=True)

    run(123, expected=False)

    run(1221, expected=True)

    # Input: x = -121
    # Output: false
    # Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
    # Therefore it is not a palindrome.
    run(-121, expected=False)

    # Input: x = 10
    # Output: false
    # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    run(10, expected=False)


if __name__ == '__main__':
    run_all()
