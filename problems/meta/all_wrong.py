from problems.utils import noop


def inverse(char: str):
    A, B = ('A', 'B')
    opposites = {'A': B, 'B': A }
    return opposites[char]


def get_wrong_answers(N: int, C: str) -> str:
    noop(N)
    chars = list(C)
    inversed = map(inverse, chars)
    return ''.join(inversed)
