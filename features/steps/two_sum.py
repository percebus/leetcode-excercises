from aloe import step, world

from apps.leetcode.two_sum import two_sum


@step("an (?P<array>.+) of integers nums")
def step_impl(self, array):
    world.nums = eval(array)


@step("an integer (?P<target>.+)")
def step_impl(self, target):
    world.target = int(target)


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
    assert world.num1 == num1, "expected:{expected}, got:{actual}".format(expected=num1, actual=world.num1)
    assert world.num2 == num2, "expected:{expected}, got:{actual}".format(expected=num2, actual=world.num2)


@step("they add up to (?P<target>.+)")
def step_impl(self, target):
    result = world.num1 + world.num2
    assert result == int(target), "expected:{expected}, got:{actual}".format(expected=target, actual=result)
