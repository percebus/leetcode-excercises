from aloe import step, world
from apps.leetcode import median_of_two_sorted_arrays


# 0 <= m <= 1000
def validate_list(array, expected):
    length = len(array)
    assert length == expected, f'len({array}): expected:{expected}, got:{length}'
    minimum = 0
    maximum = 1000
    assert (minimum <= length)           , f'({minimum} <= m <= {maximum}): {length}'
    assert (           length <= maximum), f'({minimum} <= m <= {maximum}): {length}'


# 1 <= m + n <= 2000
def validate_lists(array1, array2):
    m = len(array1)
    n = len(array2)
    length = m + n
    minimum = 1
    maximum = 2000
    assert (minimum <= length)           , f'({minimum} <= m + n <= {maximum}): {length}'
    assert (           length <= maximum), f'({minimum} <= m + n <= {maximum}): {length}'


@step("two sorted arrays (?P<array1>.+) and (?P<array2>.+)")
def step_impl(self, array1, array2):
    world.nums1 = eval(array1)
    world.nums2 = eval(array2)


@step("of size (?P<m>.+) and (?P<n>.+) respectively")
def step_impl(self, m, n):
    world.m = int(m)
    world.n = int(n)
    validate_list(world.nums1, world.m)
    validate_list(world.nums2, world.n)
    validate_lists(world.nums1, world.nums2)


@step("I call find_median")
def step_impl(self):
    world.actual = median_of_two_sorted_arrays.find_median(world.nums1, world.nums2)


@step("return the (?P<median>.+) of the two sorted arrays (?P<merged>.+)")
def step_impl(self, median, merged):
    world.merged = eval(merged)
    assert float(median) == world.actual, f'expected:{median}, got:{world.actual}'
