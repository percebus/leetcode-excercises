from aloe import step, world
from problems.meta.practice.reverse_to_make_equal import are_they_similar


def process(string:str) -> list:
    return [
        int(num)
        for num in string.split(',')
    ]


@step("two arrays (?P<A>.+) and (?P<B>.+)")
def step_impl(self, A, B):
    world.array_a = process(A)
    world.array_b = process(B)


@step("I run are_they_similar")
def step_impl(self):
    world.result = are_they_similar(world.array_a, world.array_b)


@step("are_they_similar returns True")
def step_impl(self):
    assert world.result is True, f'expected:True, got:{world.result}'


@step("are_they_similar returns False")
def step_impl(self):
    assert world.result is False, f'expected:False, got:{world.result}'
