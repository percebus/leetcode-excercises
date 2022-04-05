import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from lib.nodes.lists import nodes_to_list, list_to_nodes


# SRC: https://leetcode.com/problems/merge-k-sorted-lists/
#
# You are given an array of k linked-lists lists,
# each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
def mergeKLists(lists: list):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    _lists = map(nodes_to_list, lists)
    flattened = [
        item
        for array in _lists
        for item in array]
    flattened.sort()
    return list_to_nodes(flattened)


def test(lists: list, expected: list = None):
    collections = list(map(list_to_nodes, lists))
    result = mergeKLists(collections)
    actual = str(nodes_to_list(result))
    _expected = str(expected)
    assert actual == _expected, f'expected:{expected}, got:{actual}'
    print('✅', end='')


def test_all():
    # Example 1:
    # Input: lists = [
    #   [1,4,5],
    #   [1,3,4],
    #   [2,6]
    # ]
    #
    # Output: [1,1,2,3,4,4,5,6]
    # Explanation: merging them into one sorted list:
    # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    test(
        [[1, 4, 5], [1, 3, 4], [2, 6]],
        expected=[1, 1, 2, 3, 4, 4, 5, 6])

    # Example 2:
    #
    # Input: lists = []
    # Output: []
    test([], expected=[])

    # Example 3:
    #
    # Input: lists = [[]]
    # Output: []
    test([[]], expected=[])

    print('\n')


if __name__ == '__main__':
    test_all()
