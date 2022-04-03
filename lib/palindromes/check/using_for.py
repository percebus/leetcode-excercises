

# SRC: https://www.mygreatlearning.com/blog/palindrome-in-python/#palindrome-string
def is_palindrome(string: str) -> bool:
    length = len(string)
    for idx in range(0, int(length / 2)):
        char_a = string[idx]
        char_b = string[length - idx - 1]
        if char_a != char_b:
            return False

    return True
