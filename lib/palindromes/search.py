from .check.using_for import is_palindrome


def get_all_palindromes(string: str) -> set:
    chars = list(string)
    palindromes = set(chars)
    length = len(string)
    for i, char_i in enumerate(string):
        word = char_i
        for j in range(i + 1, length):
            char_j = chars[j]
            word += char_j
            if is_palindrome(word):
                palindromes.add(word)

    return palindromes
