from aloe import step, world

from apps.leetcode.summary_ranges import summary_ranges


@step("a sorted unique integer (?P<array>.+)")
def step_impl(self, array):
    world.nums = eval(array)


@step("I call summary_ranges")
def step_impl(self):
    world.actual = summary_ranges(world.nums)


@step("return the (?P<expected>.+) smallest sorted list of ranges that cover all the numbers in the array exactly")
def step_impl(self, expected):
    world.expected = eval(expected)
    assert str(expected) == str(world.actual), "expected:{expected}, got:{actual}".format(expected=expected, actual=world.actual)
