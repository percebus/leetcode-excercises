# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.leetcode.easy.valid_parentheses import is_valid


@step("a (?P<string>.+) containing the characters '\(', '\)', '\{', '\}', '\[' and '\]'")
def step_impl(self, string):
    world.string = string


@step("I run is_valid")
def step_impl(self):
    result = is_valid(world.string)
    world.result = bool(result)


@step("determine that the input string is valid")
def step_impl(self):
    assert world.result is True


@step("determine that the input string is NOT valid")
def step_impl(self):
    assert world.result is False
