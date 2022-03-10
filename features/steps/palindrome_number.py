from aloe import step, world
from test.utils import assert_is_in_range
from apps.leetcode import palindrome_number


constraints = {
    'value': {  # -2^31 <= x <= 2^31 -1
        'min': -2 ** 31,
        'max': (2 ** 31) - 1
    }
}

validate = {
    'value': lambda x: assert_is_in_range(x, constraints['value'])
}


@step("an integer number (?P<x>.+)")
def step_impl(self, x):
    number = int(x)
    validate['value'](number)
    world.number = number


@step("I run is_palindrome")
def step_impl(self):
    world.result = palindrome_number.is_palindrome(world.number)


@step("return True if x is palindrome integer")
def step_impl(self):
    assert world.result is True


@step("return False if x is NOT palindrome integer")
def step_impl(self):
    assert world.result is False
