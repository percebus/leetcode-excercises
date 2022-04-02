

# pylint: disable=redefined-builtin
# pylint: disable=too-few-public-methods
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# pylint: enable=too-few-public-methods
# pylint: enable=redefined-builtin


def nodes_to_list(node: ListNode) -> list:
    _node = node
    array = []
    while _node is not None:
        array.append(_node.val)
        _node = _node.next

    return array


def list_to_nodes(nums: list) -> ListNode:
    prev_node = None
    length = len(nums)
    for idx in range(0, length):
        item = nums[length - idx - 1]
        node = ListNode(item, prev_node)
        prev_node = node

    return prev_node
