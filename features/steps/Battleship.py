# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable

from aloe import step, world
from aloe.tools import guess_types
from problems.meta.coding.puzzles.warmup.battleship import getHitProbability


@step("a battleship matrix of 2 by 3")
def step_impl(self):
    world.R = 2
    world.C = 3


@step("a battleship matrix of 2 by 2")
def step_impl(self):
    world.R = 2
    world.C = 2


@step("with the following data:")
def step_impl(self):
    world.grid = [
        [int(num) for num in data['row'].split(' ')]
        for data in guess_types(self.hashes)
    ]


@step("I call getHitProbability")
def step_impl(self):
    world.result = getHitProbability(world.R, world.C, world.grid)


@step("it returns a hit probability of 50%")
def step_impl(self):
    expected = 0.5
    assert world.result == expected, f'expected:{expected}, got:{world.result}'


@step("it returns a hit probability of 100%")
def step_impl(self):
    expected = 1
    assert world.result == expected, f'expected:{expected}, got:{world.result}'


@step("it returns a hit probability of 0%")
def step_impl(self):
    expected = 0
    assert world.result == expected, f'expected:{expected}, got:{world.result}'
