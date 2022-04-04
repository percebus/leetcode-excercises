from aloe import step, world
from problems.meta.coding.puzzles.warmup.sum_abc import get_sum


@step("three integers (?P<A>.+), (?P<B>.+), and (?P<C>.+)")
def step_impl(self, A, B, C):
    world.A = int(A)
    world.B = int(B)
    world.C = int(C)


@step("I call getSum")
def step_impl(self):
    world.result = get_sum(world.A, world.B, world.C)


@step("it determines their (?P<result>.+)")
def step_impl(self, result):
    expected = int(result)
    assert expected == world.result, f'expected:{expected}, got:{world.result}'
