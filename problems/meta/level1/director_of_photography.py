
# A photography set consists of N cells in a row, numbered from 1 to N in order,
# and can be represented by a string C of length N.
# Each cell i is one of the following types
#
# A photograph consists of
#  * a photographer
#  * an actor
#  * and a backdrop
#
# Such that each of them is placed in a valid cell,
# and such that the actor is between the photographer and the backdrop.
# Such a photograph is considered artistic
#   * if the distance between the photographer and the actor is between X and Y cells (inclusive),
#   * and the distance between the actor and the backdrop is also between X and Y cells (inclusive).
#
# Determine the number of different artistic photographs which could potentially be taken at the set.
# Two photographs are considered different if they involve
#   * a different photographer cell,
#   * actor cell,
#   * and/or backdrop cell.
from pprint import pprint

P = 'P'  # photographer
A = 'A'  # artist
B = 'B'  # backdrop
_ = '.'  # space


# NOTE the requirement is confusing.
# It says "the distance between the photographer and the actor is between X and Y cells (inclusive)"
#
# Test Cases, where X=1 & Y=2, one would assume that *at least* 1 cell would be in between
# But their expected result, assumes 0 distance?
#
# There is also this other line
# "The distance between cells i and j is |i - j| (the absolute value of the difference between their indices)."
def get_spacing(minimum: int, maximum: int):
    diff = maximum - minimum  # i.e. 2 -1 = 1
    return range(0, diff + 1)
#   return range(minimum, maximum + 1) # TODO ? or XXX?


def permute_artistic_photographies(minimum: int, maximum: int) -> list:
    photographies = []
    for i in get_spacing(minimum, maximum):
        for j in get_spacing(minimum, maximum):
            length = i + j + 1  # actor
            array = [_ for idx in range(0, length)]
            array.insert(0, P)
            array[i + 1] = A
            array.append(B)
            photographies.append(array)

    # NOTE: I could do this in the for loop above
    # But this is a more pythonic way
    for array in photographies.copy():
        inverted = array[::-1]
        photographies.append(inverted)

    return photographies


def permute_scenarios(miminum: int, maximum: int, length: int) -> list:
    photographies = permute_artistic_photographies(miminum, maximum)
    results = []
    for photography in photographies:
        _len = len(photography)
        diff = length - _len
        for i in range(0, diff +1):
            left = [_ for idx in range(0, i)]
            right = [_ for idx in range(0, diff - i)]
            pprint((left, photography, right))
            expanded = left + photography + right
            results.append(expanded)

    return results



# def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
#     mask = C
#     minimum = X
#     maximum = Y
#



if __name__ == '__main__':
    photographies = permute_scenarios(1, 2, 8)
