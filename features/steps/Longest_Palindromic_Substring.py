# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world

from problems.leetcode.medium.longest_palindromic_substring import longestPalindrome


@step("a (?P<string>.+) s")
def step_impl(self, string):
    world.string = string


@step("I call longestPalindrome")
def step_impl(self):
    world.result = longestPalindrome(world.string)


@step("it returns the longest (?P<palindrome>.+) in the string")
def step_impl(self, palindrome):
    expected = palindrome
    assert world.result == expected, f'expected:{expected}, got:{world.result}'
