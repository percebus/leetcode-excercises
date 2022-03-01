from aloe import step, world
from apps.leetcode import median_of_two_sorted_arrays


@step("two sorted arrays (?P<array1>.+) and (?P<array2>.+)")
def step_impl(self, array1, array2):
    world.nums1 = eval(array1)
    world.nums2 = eval(array2)


@step("of size (?P<m>.+) and (?P<n>.+) respectively")
def step_impl(self, m, n):
    """
    :type step_instance: lettuce.core.Step
    :type m: str
    :type n: str
    """
    raise NotImplementedError(u'STEP: And of size <m> and <n> respectively')


@step("I call find_median")
def step_impl(self):
    world.actual = median_of_two_sorted_arrays.find_median(world.nums1, world.nums2)


@step("return the (?P<median>.+) of the two sorted arrays (?P<merged>.+)")
def step_impl(self, median, merged):
    world.merged = eval(merged)
    assert float(median) == world.actual, "expected:{expected}, got:{actual}".format(expected=median, actual=world.actual)
