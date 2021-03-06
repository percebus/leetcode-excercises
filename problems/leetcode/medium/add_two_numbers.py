import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from lib.nodes.lists import ListNode, list_to_nodes, nodes_to_list


def process(node: ListNode) -> int:
    nums = nodes_to_list(node)
    inverted = nums[::-1]
    string = ''.join(str(num) for num in inverted)
    return int(string)


# SRC: https://leetcode.com/problems/add-two-numbers/
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    num1 = process(l1)
    num2 = process(l2)
    total = num1 + num2
    chars = list(str(total))
    inverted = chars[::-1]
    return list_to_nodes(inverted)


def run(list1, list2, expected=None):
    node1 = list_to_nodes(list1)
    node2 = list_to_nodes(list2)
    result = addTwoNumbers(node1, node2)
    actual = str([int(num) for num in nodes_to_list(result)])
    _expected = str(expected)
    assert actual == _expected, f'expected:"{_expected}", got:"{actual}"'
    print('✅', end='')


def run_all():
    # Example 1:
    #   Input:
    #    * l1 = [2,4,3] # 342
    #    * l2 = [5,6,4] # 465 +
    #                   # ------
    #   Output: [7,0,8] # 807
    #
    #   Explanation: 342 + 465 = 807.
    run([2, 4, 3], [5, 6, 4], expected=[7, 0, 8])

    # Example 2:
    #   Input:
    #    * l1 = [0]
    #    * l2 = [0]
    #
    #   Output: [0]
    run([0], [0], expected=[0])

    # Example 3:
    #   Input:
    #    * l1 = [9,9,9,9,9,9,9]   # 9999999
    #    * l2 = [9,9,9,9]         #    9999 +
    #                             # ---------
    #   Output: [8,9,9,9,0,0,0,1] # 1009998
    run([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], expected=[8, 9, 9, 9, 0, 0, 0, 1])

    print('\n')


if __name__ == '__main__':
    run_all()
