

# https://medium.com/interview-buddy/palindrome-python-interview-problems-6a684a4cbdbe
def is_palindrome(string: str) -> bool:
    length = len(string)
    start = 0
    end = length -1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
