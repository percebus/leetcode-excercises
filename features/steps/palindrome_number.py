from aloe import step, world

from apps.leetcode import palindrome_number


# Constraints
#  * -2^31 <= x <= 2^31 -1
def validate(x):
    minimum = -2 ** 31
    maximum = (2 ** 31) - 1
    assert (minimum <= x)           , f'(-2^31 <= x <= 2^31 -1): {minimum} > {x}'
    assert (           x <= maximum), f'(-2^31 <= x <= 2^31 -1): {x} > {maximum}'


@step("an integer number (?P<x>.+)")
def step_impl(self, x):
    number = int(x)
    validate(number)
    world.number = number


@step("I run is_palindrome\(x\)")
def step_impl(self):
    world.result = palindrome_number.is_palindrome(world.number)


@step("return True if x is palindrome integer")
def step_impl(self):
    assert world.result is True


@step("return False if x is NOT palindrome integer")
def step_impl(self):
    assert world.result is False
