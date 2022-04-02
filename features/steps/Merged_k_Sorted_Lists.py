from aloe import step, world
from problems.leetcode.list_node import list_to_nodes, nodes_to_list
from problems.leetcode.hard.merge_k_sorted_lists import mergeKLists


def parse(string):
    nums = [
        int(num)
        for num in string.split('→')]
    return list_to_nodes(nums)


@step("an (?P<array>.+) of k linked-lists lists")
def step_impl(self, array):
    strings = array.split(', ')
    world.nodes = map(parse, strings)


@step("I call mergeKLists")
def step_impl(self):
    world.result = mergeKLists(world.nodes)


@step("it returns all the linked-lists merged into one sorted linked-list as (?P<result>.+)")
def step_impl(self, result):
    _expected = result
    expected = [
        int(num)
        for num in result.split('→')]

    actual = nodes_to_list(world.result)
    _actual = '→'.join([str(num) for num in actual])
    assert _actual == _expected, f'expected:{expected}, got:{actual}'
