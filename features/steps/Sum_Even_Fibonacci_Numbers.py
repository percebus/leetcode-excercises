from monkeypatch import step, world
from problems.euler.even_fibonacci_numbers import sum_evens


@step("a (?P<limit>.+) number")
def step_impl(self, limit):
    world.limit = int(limit)


@step("I call sum_evens")
def step_impl(self):
    world.result = sum_evens(world.limit)


@step("I get the (?P<total>.+) sum of all even numbers inside the Fibonacci series, up until that limit")
def step_impl(self, total):
    expected = int(total)
    assert world.result == expected, f'expected:{expected}, got:{world.result}'
