from aloe import step, world

from apps.leetcode import palindrome_number


@step("an integer number (?P<x>.+)")
def step_impl(self, x):
    world.number = x


@step("I run is_palindrome\(x\)")
def step_impl(self):
    world.result = palindrome_number.is_palindrome(world.number)


@step("return True if x is palindrome integer")
def step_impl(self):
    assert world.result is True


@step("return False if x is NOT palindrome integer")
def step_impl(self):
    assert world.result is False
