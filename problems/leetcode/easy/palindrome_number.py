

# SRC: https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
def is_palindrome(number):
    str1 = str(number)
    str2 = str1[::-1]
    return str1 == str2


def test(number, expected=None):
    result = is_palindrome(number)
#   print(f'{number}: {result}') # DEBUG only
    assert result == expected
    print('✅', end='')


def test_all():
    # Input: x = 121
    # Output: true
    # Explanation: 121 reads as 121 from left to right and from right to left.
    test(121, expected=True)

    test(123, expected=False)

    test(1221, expected=True)

    # Input: x = -121
    # Output: false
    # Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
    # Therefore it is not a palindrome.
    test(-121, expected=False)

    # Input: x = 10
    # Output: false
    # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    test(10, expected=False)

    print('\n')


if __name__ == '__main__':
    test_all()
