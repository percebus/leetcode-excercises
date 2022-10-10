# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.meta.coding.puzzles.warmup.all_wrong import get_wrong_answers


@step("a multiple-choice test with (?P<N>.+) questions, numbered 1 to N")
def step_impl(self, N):
    world.N = N


@step("a string with (?P<correct>.+) answers, each labelled A and B")
def step_impl(self, correct):
    world.correct_answers = correct


@step("I call getWrongAnswers\(N, C\)")
def step_impl(self):
    world.result = get_wrong_answers(world.N, world.correct_answers)


@step("I get a string with the (?P<wrong>.+) answers")
def step_impl(self, wrong):
    expected = wrong
    actual = world.result
    assert actual == expected, f'exected{expected}, got:{actual}'
