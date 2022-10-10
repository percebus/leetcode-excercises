# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.euler.multiples_of_3_or_5.percebus import sum_multiples


@step("a (?P<limit>.+) number")
def step_impl(self, limit):
    world.limit = int(limit)


# @step("bananas (?P<multiples>.+)")
@step("a few (?P<multiples>.+) to divide by")
def step_impl(self, multiples):
    _multiples = map(int, multiples.split(', '))
    world.multiples = list(_multiples)


@step("I call sum_multiples")
def step_impl(self):
    world.result = sum_multiples(world.limit, world.multiples)


@step("I get the expected (?P<result>.+)")
def step_impl(self, result):
    expected = int(result)
    assert world.result == expected, f'expected:{expected}, got:{world.result}'
