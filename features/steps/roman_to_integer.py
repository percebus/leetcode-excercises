from aloe import step, world
from test.utils import assert_is_in_range
from problems.leetcode.roman_to_integer import roman_to_int


constraints = {
    'length': {'min': 1, 'max':   15},  # 1 <= s.length <= 15
    'number': {'min': 1, 'max': 3999},  # It is guaranteed that s is a valid roman numeral in the range [1, 3999].
}

validate = {
#   'string': # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'). # TODO
    'length': lambda numeral: assert_is_in_range(numeral, constraints['length']),
    'number': lambda integer: assert_is_in_range(integer, constraints['number'])
}


@step("a roman (?P<numeral>.+)")
def step_impl(self, numeral):
    world.numeral = numeral
    length = len(world.numeral)
    validate['length'](length)


@step("I run roman_to_int")
def step_impl(self):
    world.number = roman_to_int(world.numeral)
    validate['number'](world.number)


@step("convert it to an (?P<integer>.+)")
def step_impl(self, integer):
    world.expected = int(integer)
    assert world.number == world.expected, f'expected:{integer}, got:{world.number}'
