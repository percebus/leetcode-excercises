from aloe import step, world
from problems.leetcode.reverse_string import reverseString


@step("an array of (?P<chars>.+)")
def step_impl(self, chars):
    world.chars = chars.split(',')


@step("I call reverseString")
def step_impl(self):
    world.result = reverseString(world.chars)


@step("the void function returns None")
def step_impl(self):
    assert world.result is None, f'expected:None, got:{world.result}'


@step("the same array is procedurally (?P<reversed>.+) by reference")
def step_impl(self, reversed):
    actual = world.chars
    expected = reversed.split(',')
    assert ','.join(actual) == reversed, f'expected{expected}, got:{actual}'
