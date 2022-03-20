

brackets = {
    '[': ']',
    '{': '}',
    '(': ')'
}


# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#  * Open brackets must be closed by the same type of brackets.
#  * Open brackets must be closed in the correct order.
#
# SRC: https://leetcode.com/problems/valid-parentheses/
def is_valid(string):
    opened = []  # TODO? use queue instead?
    for char in string:
        is_opening = char in brackets.keys()
        is_closing = char in brackets.values()
        if is_opening:
            opened.append(char)
        elif is_closing:
            last_opened = opened[-1] if opened else None
            if char == brackets.get(last_opened):
                opened.pop()
            else:
                return False
        else:
            pass  # any other char
    return False if opened else True


def run(string, expected=None):
    result = is_valid(string)
    assert result == expected, f"'{string}'.- expected:{expected}, got:{result}"


def run_all():
    # Example 1:
    #  * Input: s = "()"
    #  * Output: true
    run('()', expected=True)

    # Example 2:
    #  * Input: s = "()[]{}"
    #  * Output: true
    run('()[]{}', expected=True)

    # Example 3:
    #  * Input: s = "(]"
    #  * Output: false
    run('(]', expected=False)

    # Example
    #  * Input: s = "["
    #  * Output: false
    run('[', expected=False)


if __name__ == '__main__':
    run_all()
