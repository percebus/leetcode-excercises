

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



# class ForkNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # TODO
# def find_common_ancestors(binary_tree: ForkNode, nums: tuple) -> int:
#     x, y = nums
#
#     def recurse(node):
#         if node is None:
#             return
#
#         if node.val == x:
#             a = node
#
#         if node.val == y:
#             b = node
#
#         recurse(node.left)
#         recurse(node.right)
