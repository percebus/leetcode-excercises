# FIXME nose monkeypatch
import collections
import collections.abc
collections.Callable = collections.abc.Callable


from aloe import step, world
from problems.leetcode.medium.add_two_numbers import addTwoNumbers, list_to_nodes, nodes_to_list


def to_list(string):
    return [
        int(num)
        for num in string.split('→')
    ]


def parse(string):
    nums = to_list(string)
    return list_to_nodes(nums)


@step("two non-empty linked lists (?P<nodes1>.+) and (?P<nodes2>.+) representing two non-negative integers")
def step_impl(self, nodes1, nodes2):
    world.nodes1 = parse(nodes1)
    world.nodes2 = parse(nodes2)


@step("I call addTwoNumbers")
def step_impl(self):
    world.result = addTwoNumbers(world.nodes1, world.nodes2)


@step("I get the sum as a (?P<result>.+) linked list")
def step_impl(self, result):
    expected_numbers = to_list(result)
    expected = ''.join(str(num) for num in expected_numbers)
    actual_numbers = nodes_to_list(world.result)
    actual = ''.join(str(num) for num in actual_numbers)
    assert actual == expected, f'expected:{expected}, got:{actual}'
