

# pylint: disable=too-few-public-methods
class ForkNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'val={self.val}'
# pylint: enable=too-few-public-methods
