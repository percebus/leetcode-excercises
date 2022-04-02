

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
