from ..search import get_all_palindromes


def get_longest_palindrome(string: str) -> set:
    palindromes = get_all_palindromes(string)
    return max(palindromes, key=len)
