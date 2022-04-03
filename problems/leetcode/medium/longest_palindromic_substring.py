from lib.palindromes.longest.neet import get_longest_palindrome


# SRC: https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    return get_longest_palindrome(s)


def test(string: str, expected: str = None):
    result = longestPalindrome(string)
    assert result == expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def test_all():
    # Example 1:
    #
    # Input: s = "babad"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.
    test('babad', expected='bab')

    # Example 2:
    #
    # Input: s = "cbbd"
    # Output: "bb"
    test('cbbd', expected='bb')

    print('\n')


if __name__ == '__main__':
    test_all()
