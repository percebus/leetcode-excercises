

# SRC: https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
def longest_common_prefix(words):
    first_word = words[0]
    chars = list(first_word)
    prefix = ''
    result = prefix
    for char in chars:
        prefix += char
        invalid = next((word for word in words if not word.startswith(prefix)), None)
        if invalid is None:
            result = prefix
        else:
            return result
    return result


def run(words, expected=None):
    result = longest_common_prefix(words)
    assert result == expected, f'expected:"{expected}", got:"{result}"'
    print('✅', end='')


def run_all():
    # Example1:
    #
    # * Input: strs = ["flower", "flow", "flight"]
    # * Output: "fl"
    run(["flower", "flow", "flight"], expected="fl")

    # Example 2:
    #
    # * Input: strs = ["dog", "racecar", "car"]
    # * Output: ""
    # Explanation: There is no common prefix among the input strings.
    run(["dog", "racecar", "car"], expected="")

    run([""], expected="")

    print('\n')


if __name__ == '__main__':
    run_all()
