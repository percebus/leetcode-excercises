from aloe import step, world
from problems.leetcode.list_node import list_to_nodes, nodes_to_list
from problems.leetcode.hard.merge_k_sorted_lists import mergeKLists


def remove_brackets(string):
    _string = string
    _string = _string.replace('{', '')
    _string = _string.replace('}', '')
    return _string


def parse_chain(string):
    if string == '{}':
        return []

    _string = remove_brackets(string)
    return [int(num) for num in _string.split('→')]


def parse_nodes(string):
    if string == '':
        return None

    nums = parse_chain(string)
    return list_to_nodes(nums)


def parse_array(string):
    if string == '[]':
        return []

    _string = string
    _string = _string.replace('[ ', '')
    _string = _string.replace(' ]', '')
    strings = _string.split(', ')
    return list(map(parse_nodes, strings))


@step("an (?P<array>.+) of k linked-lists lists")
def step_impl(self, array):
    world.nodes = parse_array(array)


@step("I call mergeKLists")
def step_impl(self):
    world.result = mergeKLists(world.nodes)


@step("it returns all the linked-lists merged into one sorted linked-list as (?P<result>.+)")
def step_impl(self, result):
    expected = parse_chain(result)
    _expected = '→'.join([str(num) for num in expected])

    actual = nodes_to_list(world.result)
    _actual = '→'.join([str(num) for num in actual])

    assert _actual == _expected, f'expected:{expected}, got:{actual}'
