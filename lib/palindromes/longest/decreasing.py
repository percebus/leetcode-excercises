from ..check.using_for import is_palindrome


def get_longest_palindrome(string: str) -> str:
    length = len(string)
    for i in range(length):
        diff = length - i
        for j in range(i + 1):
            substring = string[j:diff + j]
            if is_palindrome(substring):
                return substring
    return ''
