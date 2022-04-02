
# SRC: https://leetcode.com/problems/add-two-numbers/
from problems.leetcode.list_node import ListNode


def nodes_to_list(node: ListNode) -> list:
    _node = node
    array = []
    while True:
        num = int(_node.val)
        array.append(num)
        _node = _node.next
        if _node is None:
            return array


def list_to_nodes(nums: list) -> ListNode:
    inverted = nums[::-1]
    prev_node = None
    for item in inverted:
        num = int(item)
        node = ListNode(num, prev_node)
        prev_node = node
    return prev_node


def process(node: ListNode) -> int:
    nums = nodes_to_list(node)
    inverted = nums[::-1]
    string = ''.join(str(num) for num in inverted)
    return int(string)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    num1 = process(l1)
    num2 = process(l2)
    total = num1 + num2
    chars = list(str(total))
    inverted = chars[::-1]
    return list_to_nodes(inverted)


def test(list1, list2, expected=None):
    node1 = list_to_nodes(list1)
    node2 = list_to_nodes(list2)
    result = addTwoNumbers(node1, node2)
    actual = str(nodes_to_list(result))
    _expected = str(expected)
    assert actual == _expected, f'expected:"{_expected}", got:"{actual}"'


def test_all():
    # Example 1:
    #   Input:
    #    * l1 = [2,4,3] # 342
    #    * l2 = [5,6,4] # 465 +
    #                   # ------
    #   Output: [7,0,8] # 807
    #
    #   Explanation: 342 + 465 = 807.
    test([2, 4, 3], [5, 6, 4], expected=[7, 0, 8])

    # Example 2:
    #   Input:
    #    * l1 = [0]
    #    * l2 = [0]
    #
    #   Output: [0]
    test([0], [0], expected=[0])

    # Example 3:
    #   Input:
    #    * l1 = [9,9,9,9,9,9,9]   # 9999999
    #    * l2 = [9,9,9,9]         #    9999 +
    #                             # ---------
    #   Output: [8,9,9,9,0,0,0,1] # 1009998
    test([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], expected=[8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == '__main__':
    test_all()
