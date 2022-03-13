
def create_filter(prefix):
    return lambda word: word.startswith(prefix)


# SRC: https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
def longest_common_prefix(words):
    length = len(words)
    first_word = words[0]
    chars = list(first_word)
    prefix = ''
    result = prefix
    for char in chars:
        prefix += char
        fn = create_filter(prefix)
        filtered = list(filter(fn, words))
        if len(filtered) == length:
            result = prefix
        else:
            return result
    return result


def run(words, expected=None):
    result = longest_common_prefix(words)
    assert result == expected, f'expected:"{expected}", got:"{result}"'


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


if __name__ == '__main__':
    run_all()
