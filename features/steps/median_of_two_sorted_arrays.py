from aloe import step, world
from apps.leetcode import median_of_two_sorted_arrays


@step("arrays (?P<array1>.+) and (?P<array2>.+)")
def step_impl(self, array1, array2):
    world.nums1 = eval(array1)
    world.nums2 = eval(array2)


@step("I call find_median")
def step_impl(self):
    world.actual = median_of_two_sorted_arrays.find_median(world.nums1, world.nums2)


@step("I get the (?P<expected>.+) result")
def step_impl(self, expected):
    assert float(expected) == world.actual, "expected:{expected}, got:{actual}".format(expected=expected, actual=world.actual)
