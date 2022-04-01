from typing import List

from problems.utils import noop


TAKEN = '8'
AVAILABLE = '_'
UNAVAILABLE = 'X'


def get_current_seats(total:int, distance:int, occupied: List[int]):
    seats = [AVAILABLE for i in range(0, total)]
    length = len(seats)
    for seat in occupied:  # [2, 4, 6]
        idx = seat - 1
        seats[idx] = TAKEN

        for left in range(1, distance + 1):
            i = idx - left
            if i < 0:
                break
            seats[i] = UNAVAILABLE

        for right in range(1, distance + 1):
            i = idx + right
            if i >= length:
                break
            seats[i] = UNAVAILABLE

    print(seats)
    return seats


# Your task is to implement the function getSum(A, B, C) which returns the sum A + B + CA+B+C.
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    distance = K
    noop(M)
    seats = get_current_seats(N, K, S)
    length = len(seats)
    for idx, seat in seats.items():
        if seat == AVAILABLE:
            for left in range(1, distance + 1):
                i = idx - left
                if i < 0:
                    break
                seats[i] = UNAVAILABLE

            for right in range(1, distance + 1):
                i = idx + right
                if i >= length:
                    break
                seats[i] = UNAVAILABLE

    noop(seats)
    return 0
