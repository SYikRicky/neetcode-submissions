# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack: list[tuple[TreeNode, int, int]] = [(root, float("-inf"), float("inf"))]
        while stack:
            data: tuple[TreeNode, int, int] = stack.pop()
            low_bound, up_bound, node = data[1], data[2], data[0]

            if not (low_bound < node.val < up_bound):
                return False

            if node.left:
                stack.append((node.left, low_bound, node.val))

            if node.right:
                stack.append((node.right, node.val, up_bound))

        return True