# Euclidean distance
def calculate_distance(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b

    def fn(a1, a2):
        return (a2 - a1) ** 2

    return fn(x1, x2) + fn(y1, y2)


def get_distances(points: list, center=(0, 0)):
    return map(
        lambda point: calculate_distance(point, center),
        points)


# Given a collection of n two dimensional points
# and a number k,
# return the k closest points to (0,0) by Euclidean distance.
#
#        *  |
#           |
#           |           *
#   *       |   *
# ----------o------------
#           |
#       *   |   *
#           |
#         * |         *
def filter_by_distance(points: list, k: int = 1, center=(0, 0)) -> list:
    distances = get_distances(points, center=center)
    pairs = list(zip(points, distances))
    pairs.sort(key=lambda pair: pair[1])  # FIXME heap sort
    return [
        pair[0]
        for pair in pairs[:k]
    ]


def run(points: list, k: int, center=(0, 0), expected=None):
    result = filter_by_distance(points, k, center=center)
    assert str(result) == str(expected), f'expected:{expected}, got:{result}'
    print('✅', end='')


def run_all():
    points = [
        (2, 2),
        (-1, 1),
        (3, 2),
        (1, 1),
        (2, 3),
        (1, -1),
        (-1, -1),
    ]

    run(points, 1, expected=[(-1, 1)])
    run(points, 2, expected=[(-1, 1), (1, 1)])
    run(points, 3, expected=[(-1, 1), (1, 1), (1, -1)])
    run(points, 4, expected=[(-1, 1), (1, 1), (1, -1), (-1, -1)])
    run(points, 5, expected=[(-1, 1), (1, 1), (1, -1), (-1, -1), (2, 2)])
    run(points, 6, expected=[(-1, 1), (1, 1), (1, -1), (-1, -1), (2, 2), (3, 2)])
    run(points, 7, expected=[(-1, 1), (1, 1), (1, -1), (-1, -1), (2, 2), (3, 2), (2, 3)])
    run(points, 8, expected=[(-1, 1), (1, 1), (1, -1), (-1, -1), (2, 2), (3, 2), (2, 3)])

    run(points, 7, center=(1, 0),
        expected=[(1, 1), (1, -1), (2, 2), (-1, 1), (-1, -1), (3, 2), (2, 3)])

    run(points, 7, center=(2, 2),
        expected=[(2, 2), (3, 2), (2, 3), (1, 1), (-1, 1), (1, -1), (-1, -1)])

    print('\n')


if __name__ == '__main__':
    run_all()
