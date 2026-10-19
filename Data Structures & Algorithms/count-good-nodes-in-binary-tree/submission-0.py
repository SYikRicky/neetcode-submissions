# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res: int = 0
        stack: list[tuple[TreeNode, int]] = [(root, root.val)]

        while stack:
            data: tuple[TreeNode, int] = stack.pop()
            node: TreeNode = data[0]
            curr_max: int = data[1]

            if node.left:
                if node.left.val >= curr_max:
                    res += 1
                    stack.append((node.left, node.left.val))
                else:
                    stack.append((node.left, curr_max))

            if node.right:
                if node.right.val >= curr_max:
                    res += 1
                    stack.append((node.right, node.right.val))
                else:
                    stack.append((node.right, curr_max))

        return res + 1