from pprint import pprint
from lib.nodes.fork import ForkNode


#     3
#    / \
#   9   7
#  / \   \
# 2   6   4


# Given two paths from root to each node in that tree, find the LCA
# 3 -> |9| -> 2
# 3 -> |9| -> 6
#
# |3| -> 7
# |3| -> 9 -> 6


# Given two nodes, find 2 paths from root to each node
# 2, 6
#   2: 3 -> 9 -> 2
#   6: 3 -> 9 -> 6


# Given a binary tree and two nodes in that tree, find the lowest common ancestor of those nodes.
# 2,6 ~ 9
# 7,6 ~ 3


# pylint: disable=inconsistent-return-statements
def find_node(node: ForkNode, value):
    def recurse(node):
        if node is None:
            return

        if node.val == value:
            return node

        _node = recurse(node.left)
        if _node is not None:
            return _node

        return recurse(node.right)

    return recurse(node)
# pylint: enable=inconsistent-return-statements


def parse_node(node: ForkNode):
    def recurse(node, result):
        if node is None:
            return result

        result.append(node.val)
        return [
            recurse(node.left, result.copy()),
            recurse(node.right, result.copy())
        ]

    return recurse(node, [])


# TODO
def find_common_ancestors(binary_tree: ForkNode, nums: tuple) -> int:
    x = nums[0]
    find_node(binary_tree, x)


def run_all():
    # node5 = ForkNode(val=5)

    node2 = ForkNode(val=2)
    node6 = ForkNode(val=6)
    node9 = ForkNode(val=9, left=node2, right=node6)

    node4 = ForkNode(val=4)
    node7 = ForkNode(val=7, right=node4)

    node3 = ForkNode(val=3, left=node9, right=node7)

    search = 6
    node = find_node(node3, search)
    print(f'searched:{search}, found:{node}')

    nodes = parse_node(node3)
    pprint(nodes)


if __name__ == '__main__':
    run_all()
