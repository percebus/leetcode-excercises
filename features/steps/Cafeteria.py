# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.meta.coding.puzzles.level1.cafeteria import getMaxAdditionalDinersCount


@step("a number (?P<N>.+) of seats")
def step_impl(self, N):
    world.N = int(N)


@step("social distancing (?P<K>.+)")
def step_impl(self, K):
    world.K = int(K)


@step("current diners (?P<S>.+), of size (?P<M>.+)")
def step_impl(self, S, M):
    world.S = [
        int(num)
        for num in S.split(', ')
    ]

    world.M = int(M)


@step("I call getMaxAdditionalDinersCount")
def step_impl(self):
    world.result = getMaxAdditionalDinersCount(world.N, world.K, world.M, world.S)


@step("I get the potential maximum number of additional diner (?P<new_clients>.+)")
def step_impl(self, new_clients):
    expected = int(new_clients)
    assert world.result == expected, f'expected:{expected}, got:{world.result}'
