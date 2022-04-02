

# Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
def reverseString(s: str) -> None:
    chars = s
    # FIXME simplify do 1 trip, instead of 2
    inverted = chars[::-1]
    for idx, item in enumerate(inverted):
        s[idx] = item


def run(chars, expected=None):
    reverseString(chars)
    actual = ''.join(chars)
    assert actual == ''.join(expected), f'expected{expected}, got:{chars}'


def run_all():
    # Example 1:
    # Input: s = ['h','e','l','l','o']
    # Output: ['o','l','l','e','h']
    run(['h', 'e', 'l', 'l', 'o'], expected=['o', 'l', 'l', 'e', 'h'])

    # Example 2:
    # Input: s = ['H', 'a', 'n', 'n', 'a', 'h']
    # Output: ['h', 'a', 'n', 'n', 'a', 'H']
    run(['H', 'a', 'n', 'n', 'a', 'h'], expected=['h', 'a', 'n', 'n', 'a', 'H'])


if __name__ == '__main__':
    run_all()
