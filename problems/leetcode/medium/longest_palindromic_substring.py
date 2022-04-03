

def compare_strings(a, b):
    return a if len(a) >= len(b) else b


# SRC: https://www.mygreatlearning.com/blog/palindrome-in-python/#palindrome-string
def is_palindrome_iterative(string: str) -> bool:
    length = len(string)
    for idx in range(0, int(length / 2)):
        char_a = string[idx]
        char_b = string[length - idx - 1]
        if char_a != char_b:
            return False

    return True


METHOD = 'iterative'
is_palindrome_methods = {
    'reverse': lambda string: string == string[::-1],
    'iterative': is_palindrome_iterative
}
is_palindrome = is_palindrome_methods[METHOD]


# DEBUG ONLY
# def get_all_palindromes(string: str) -> set:
#     chars = list(string)
#     palindromes = set(chars)
#     length = len(string)
#     for i, char_i in enumerate(string):
#         word = char_i
#         for j in range(i + 1, length):
#             char_j = chars[j]
#             word += char_j
#             if is_palindrome(word):
#                 palindromes.add(word)
#
#     return palindromes


# SRC: https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    # palindromes = get_all_palindromes(s)
    # return max(palindromes, key=len)
    string = s
    chars = list(string)
    length = len(string)
    palindrome = ''
    for i, char_i in enumerate(string):
        word = char_i
        palindrome = compare_strings(palindrome, word)
        for j in range(i + 1, length):
            char_j = chars[j]
            word += char_j
            if is_palindrome(word):
                palindrome = compare_strings(palindrome, word)

    return palindrome


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
