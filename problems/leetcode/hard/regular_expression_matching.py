import re


# SRC: https://leetcode.com/problems/regular-expression-matching/
#
# implement regular expression matching with support for '.' and '*' where:
#  - '.' Matches any single character.
#  - '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial)
def isMatch(s: str, p: str) -> bool:
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    string = s
    pattern = p
    return re.match(f'^{pattern}$', string) is not None


def run(string: str, pattern: str, expected: bool = None):
    result = isMatch(string, pattern)
    assert result is expected, f'expected:{expected}, got:{result}'
    print('✅', end='')


def run_all():
    # Example 1:
    # Input: s="aa", p="a"
    # Output: false
    # Explanation: "a" does not match the entire string "aa".
    run('aa', 'a', expected=False)

    # Example 2:
    #
    # Input: s="aa", p="a*"
    # Output: true
    # Explanation: '*' means zero or more of the preceding element, 'a'.
    # Therefore, by repeating 'a' once, it becomes "aa".
    run('aa', 'a*', expected=True)

    # Example 3:
    #
    # Input: s="ab", p=".*"
    # Output: true
    # Explanation: ".*" means "zero or more (*) of any character (.)".
    run('ab', '.*', expected=True)

    run('aab', 'c*a*b', expected=True)

    print('\n')


if __name__ == '__main__':
    run_all()
