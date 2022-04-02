from pprint import pprint

# from problems.utils import DEBUG  # FIXME "No module named 'problems'"
DEBUG = False


DIFF_METHOD = 'bounds2'

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
    create_range = {
        'diff': lambda x, y: range(0, y - x + 1),
        'bounds': lambda x, y: range(x, y + 1),
        'bounds2': lambda x, y: range(x - 1, y)
    }

    return create_range[DIFF_METHOD](minimum, maximum)


def permute_artistic_photos(minimum: int, maximum: int) -> list:
    photos = []
    for i in get_spacing(minimum, maximum):
        for j in get_spacing(minimum, maximum):
            length = i + j + 1  # actor
            array = [_ for idx in range(0, length)]
            array.insert(0, P)
            array[i + 1] = A
            array.append(B)
            photos.append(array)

    # NOTE: I could do this in the for loop above
    # But this is a more pythonic way
    for array in photos.copy():
        inverted = array[::-1]
        photos.append(inverted)

    return photos


def permute_scenarios(length: int, photos: list) -> list:
    results = []
    for photo in photos:
        _len = len(photo)
        diff = length - _len
        for i in range(0, diff +1):
            left = [_ for idx in range(0, i)]
            right = [_ for idx in range(0, diff - i)]
            if DEBUG is True:
                pprint((left, photo, right))

            expanded = left + photo + right
            results.append(expanded)

    return results


def expand_mask(mask:str) -> list:
    # '.PBAAP.B'
    #
    # '.P_A__.B'
    # '.P__A_.B'
    # '._BA_P._'
    # '._B_AP._'
    chars = list(mask)
    indexes = {
        'P': [],
        'A': [],
        'B': []
    }

    # FIXME simplify
    for idx, char in enumerate(chars):
        for element in [P, A, B]:
            if element == char:
                indexes[element].append(idx)

    filters = []
    for p in indexes[P]:
        for a in indexes[A]:
            for b in indexes[B]:
                if (p > a) and (b > a):
                    continue

                if (p < a) and (b < a):
                    continue

                array = [_ for idx in range(0, len(chars))]
                array[p] = P
                array[a] = A
                array[b] = B
                string = ''.join(array)
                filters.append(string)

    return filters


def pretty_print(items: list) -> None:
    strings = [''.join(item) for item in items]
    pprint(strings)


def get_artistic_photos(mask:str, minimum:int, maximum:int) -> list:
    photos = permute_artistic_photos(minimum, maximum)
    scenarios = permute_scenarios(len(mask), photos)
    filters = expand_mask(mask)
    filtered = [
        photo
        for photo in scenarios
        if ''.join(photo) in filters]

    if DEBUG:
        pretty_print(filtered)

    return filtered


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    assert len(C) == N, f'mask:{C} is NOT of size {N}'
    valid_photos = get_artistic_photos(C, X, Y)
    return len(valid_photos)


def run(length:int, mask:str, minimium: int, maximum: int, expected: int) -> None:
    result = getArtisticPhotographCount(length, mask, minimium, maximum)
    assert result == expected, f'expected:{expected}, got:{result}'


def run_all():
    # Sample test case #1
    # * N=5, C=APABA
    # * X=1, Y=2
    #
    # Expected Return Value = 1
    run(5, 'APABA', 1, 2, expected=1)

    # Sample test case #2
    # * N=5, C=APABA
    # * X=2, Y=3
    #
    # Expected Return Value = 0
    run(5, 'APABA', 2, 3, expected=0)

    # Sample test case #3
    # N=8, C=.PBAAP.B
    # X=1, Y=3
    #
    # Expected Return Value = 3
    run(8, '.PBAAP.B', 1, 3, expected=3)


if __name__ == '__main__':
    run_all()
