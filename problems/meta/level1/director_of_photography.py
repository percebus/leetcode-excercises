import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from pprint import pprint
from config import DEBUG


P = 'P'  # photographer
A = 'A'  # artist
B = 'B'  # backdrop
_ = '.'  # space  # FIXME find a better char. '_' blends them together
DIFF_METHOD = 'bounds2'


def pretty_print(items: list) -> None:
    strings = [''.join(item) for item in items]
    pprint(strings)


# NOTE the requirement is confusing.
# It says "the distance between the photographer and the actor is between X and Y cells (inclusive)"
#
# Test Cases, where X=1 & Y=2, one would assume that *at least* 1 cell would be in between
# But their expected result, assumes 0 distance?
#
# There is also this other line
# "The distance between cells i and j is |i - j|
# (the absolute value of the difference between their indices)."
def create_lambda():
    create_range = {
        'diff': lambda x, y: range(y - x + 1),
        'bounds': lambda x, y: range(x, y + 1),
        'bounds2': lambda x, y: range(x - 1, y)
    }

    return create_range[DIFF_METHOD]


def permute_artistic_photos(minimum: int, maximum: int) -> list:
    get_spacing = create_lambda()
    photos = []
    for i in get_spacing(minimum, maximum):
        for j in get_spacing(minimum, maximum):
            length = i + j + 1  # actor
            array = [_ for idx in range(length)]
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
        for i in range(diff +1):
            left = [_ for idx in range(i)]
            right = [_ for idx in range(diff - i)]
            if DEBUG:
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

                array = [_ for idx in range(len(chars))]
                array[p] = P
                array[a] = A
                array[b] = B
                string = ''.join(array)
                filters.append(string)

    return filters


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


def run_large_sample():
    photos = permute_artistic_photos(1, 90)
    scenarios = permute_scenarios(200, photos)
    pretty_print(scenarios)


def test(length:int, mask:str, minimium: int, maximum: int, expected: int) -> None:
    result = getArtisticPhotographCount(length, mask, minimium, maximum)
    assert result == expected, f'expected:{expected}, got:{result}'


def test_all():
    # Sample test case #1
    # * N=5, C=APABA
    # * X=1, Y=2
    #
    # Expected Return Value = 1
    # Explanation:
    # The absolute distances between photographer/actor and actor/backdrop must be between 1 and 2.
    # The only possible photograph that can be taken is with the 3 middle cells,
    # and it happens to be artistic.
    test(5, 'APABA', 1, 2, expected=1)

    # Sample test case #2
    # * N=5, C=APABA
    # * X=2, Y=3
    #
    # Expected Return Value = 0
    # Explanation:
    # he only possible photograph is again taken with the 3 middle cells.
    # However, as the distance requirement is between 2 and 3,
    # it is not possible to take an artistic photograph.
    test(5, 'APABA', 2, 3, expected=0)

    # Sample test case #3
    # N=8, C=.PBAAP.B
    # X=1, Y=3
    #
    # Expected Return Value = 3
    # Explanation
    #  | .P.A...B | <<  the artist and backdrop exceed the maximum distance of 3.
    #  | .P..A..B |
    #  | ..BA.P.. |
    #  | ..B.AP.. |
    test(8, '.PBAAP.B', 1, 3, expected=3)


if __name__ == '__main__':
    test_all()
#   run_large_sample() # FIXME it takes 30s!
