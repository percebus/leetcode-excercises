from aloe import step, world
from test.utils import assert_is_in_range
from problems.leetcode import palindrome_number


constraints = {
    'value': {  # -2^31 <= x <= 2^31 -1
        'min': -2 ** 31,
        'max': (2 ** 31) - 1
    }
}

validate = {
    'value': lambda x: assert_is_in_range(x, constraints['value'])
}


def parse(x):
    return eval(x)


@step("an integer number (?P<x>.+)")
def step_impl(self, x):
    number = parse(x)
    validate['value'](number)
    world.number = number


@step("an invalid integer number (?P<x>.+)")
def step_impl(self, x):
    number = parse(x)
    try:
        validate['value'](number)
        world.number = number
    except Exception as exception:
        world.exception = exception


@step("I run is_palindrome")
def step_impl(self):
    world.result = palindrome_number.is_palindrome(world.number)


@step("return True if x is palindrome integer")
def step_impl(self):
    assert world.result is True


@step("return False if x is NOT palindrome integer")
def step_impl(self):
    assert world.result is False


@step("handle the exception")
def step_impl(self):
    assert world.actual is None, f'{world.actual}'
    assert world.exception is not None, f'{world.exception}'
