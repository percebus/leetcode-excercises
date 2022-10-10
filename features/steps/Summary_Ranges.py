# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.leetcode.easy.summary_ranges import summary_ranges


@step("a sorted unique integer (?P<array>.+)")
def step_impl(self, array):
    world.nums = eval(array)


@step("I call summary_ranges")
def step_impl(self):
    world.actual = summary_ranges(world.nums)


@step("return the (?P<expected>.+) smallest sorted list of ranges that cover all the numbers in the array exactly")
def step_impl(self, expected):
    world.expected = eval(expected)
    assert str(expected) == str(world.actual), f'expected:{expected}, got:{world.actual}'
