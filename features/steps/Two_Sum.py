from aloe import step, world
from test.utils import assert_is_in_range
from problems.leetcode.easy.two_sum import two_sum


constraints = {
    'length': {'min':    2, 'max': 104},  #    2 <= nums.length <= 104
    'target': {'min': -109, 'max': 109},  # -109 <= target      <= 109
    'value' : {'min': -109, 'max': 109}   # -109 <= nums[i]     <= 109
}

validate = {
    'value' : lambda      x: assert_is_in_range(           x, constraints['value']),
    'length': lambda length: assert_is_in_range(      length, constraints['length']),
    'target': lambda target: assert_is_in_range(world.target, constraints['target']),
}


@step("an (?P<array>.+) of integers nums")
def step_impl(self, array):
    world.nums = eval(array)
    length = len(world.nums)
    validate['length'](length)
    map(validate['value'], array)


@step("an integer (?P<target>.+) number")
def step_impl(self, target):
    world.target = int(target)
    validate['target'](world.target)


@step("I call two_sum")
def step_impl(self):
    world.actual = two_sum(world.nums, world.target)


@step("return (?P<indices>.+) of the (?P<two_numbers>.+)")
def step_impl(self, indices, two_numbers):
    world.indices = eval(indices)
    world.two_numbers = eval(two_numbers)
    idx1, idx2 = world.indices
    num1, num2 = world.two_numbers
    world.num1 = world.nums[idx1]
    world.num2 = world.nums[idx2]
    assert world.num1 == num1, f'expected:{num1}, got:{world.num1}'
    assert world.num2 == num2, f'expected:{num2}, got:{world.num2}'


@step("they add up to (?P<target>.+)")
def step_impl(self, target):
    result = world.num1 + world.num2
    assert result == int(target), f'expected:{target}, got:{result}'
