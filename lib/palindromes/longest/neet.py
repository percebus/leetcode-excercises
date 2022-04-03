

# NeetCode's approach (tweaked)
# SRC: https://www.youtube.com/watch?v=XYQecbcd6_c
def get_longest_palindrome(string: str) -> str:
    length = len(string)
    palindrome = ''

#   _len = len(palindrome)
    _len = 0
    for idx in range(length):
        left, right = idx, idx  # odd length
        while left >= 0 and right < length and string[left] == string[right]:
            delta = right - left + 1
            if delta > _len:
                palindrome = string[left: right + 1]
                _len = delta

            left -= 1
            right += 1

        left, right = idx, idx + 1  # even length
        while left >= 0 and right < length and string[left] == string[right]:
            delta = right - left + 1
            if delta > _len:
                palindrome = string[left: right + 1]
                _len = delta

            left -= 1
            right += 1

    return palindrome
