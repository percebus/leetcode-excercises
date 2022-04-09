import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
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


def find_branch(node: ForkNode, value):
    def recurse(node, result):
        if node is None:
            return

        result.append(node)
        if node.val == value:
            return result

        nodes = recurse(node.left, result.copy())
        if nodes is not None:
            return nodes

        return recurse(node.right, result.copy())

    return recurse(node, [])
# pylint: enable=inconsistent-return-statements


# TODO
def find_common_ancestors(binary_tree: ForkNode, nums: tuple) -> int:
    x, y = nums
    x_branch = find_branch(binary_tree, x)
    y_branch = find_branch(binary_tree, y)

    result = []
    length = len(y_branch)
    for idx, x_node in enumerate(x_branch):
        if idx >= length - 1:
            break

        y_node = y_branch[idx]
        if x_node.val == y_node.val:
            result.append(x_node)
        else:
            break

    return result


def run_all():
    # node5 = ForkNode(val=5)

    #   9
    #  / \
    # 2   6
    node2 = ForkNode(val=2)
    node6 = ForkNode(val=6)
    node9 = ForkNode(val=9, left=node2, right=node6)

    # 7
    #  \
    #   4
    node4 = ForkNode(val=4)
    node7 = ForkNode(val=7, right=node4)

    #   3
    #  / \
    # 9   7
    node3 = ForkNode(val=3, left=node9, right=node7)

    search = 4
    node = find_branch(node3, search)
    print(f'searched:{search}, found:{node}')

    ancestors = find_common_ancestors(node3, [6, 9])
    print(ancestors)

    ancestors = find_common_ancestors(node3, [2, 6])
    print(ancestors)


if __name__ == '__main__':
    run_all()
