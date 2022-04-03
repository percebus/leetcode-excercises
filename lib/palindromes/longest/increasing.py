from ..check.using_for import is_palindrome


def get_longest_palindrome(string: str) -> str:

    def compare_strings(a, b):
        return a if len(a) >= len(b) else b

    if is_palindrome(string):
        return string

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
