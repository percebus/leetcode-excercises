from aloe import before, step, world
from test.utils import assert_is_in_range
from problems.leetcode import median_of_two_sorted_arrays


constraints = {
    'm'  : {'min': 0, 'max': 1000},  # 0 <=   m   <= 1000
    'm+n': {'min': 1, 'max': 2000},  # 1 <= m + n <= 2000
}


def validate_list(array, expected):
    length = len(array)
    assert length == expected, f'len({array}): expected:{expected}, got:{length}'
    validate['m'](length)


def validate_lists(array1, array2):
    m = len(array1)
    n = len(array2)
    compound = m + n
    validate['m+n'](compound)


def parse(array):
    return eval(array)  # FIXME


validate = {
    'm': lambda m: assert_is_in_range(m, constraints['m']),
    'm+n': lambda x: assert_is_in_range(x, constraints['m+n']),
    'list': validate_list,
    'lists': validate_lists
}


@before.each_example
def before_example(scenario, outline, steps):
    world.nums1 = None
    world.nums2 = None
    world.m = None
    world.n= None
    world.merged = None
    world.actual = None


@step("two sorted arrays (?P<array1>.+) and (?P<array2>.+)")
def step_impl(self, array1, array2):
    world.nums1 = parse(array1)
    world.nums2 = parse(array2)
    validate['lists'](world.nums1, world.nums2)


@step("two empty arrays (?P<array1>.+) and (?P<array2>.+)")
def step_impl(self, array1, array2):
    world.nums1 = parse(array1)
    world.nums2 = parse(array2)
    try:
        validate['lists'](world.nums1, world.nums2)
    except Exception as exception:
        world.exception = exception


@step("of size (?P<m>.+) and (?P<n>.+) respectively")
def step_impl(self, m, n):
    world.m = int(m)
    world.n = int(n)
    validate['list'](world.nums1, world.m)
    validate['list'](world.nums2, world.n)


@step("I call find_median")
def step_impl(self):
    world.actual = median_of_two_sorted_arrays.find_median(world.nums1, world.nums2)


@step("return the (?P<median>.+) of the two sorted arrays (?P<merged>.+)")
def step_impl(self, median, merged):
    world.merged = parse(merged)
    assert float(median) == world.actual, f'expected:{median}, got:{world.actual}'


@step("handle the exception")
def step_impl(self):
    assert world.actual is None, f'{world.actual}'
    assert world.exception is not None, f'{world.exception}'
