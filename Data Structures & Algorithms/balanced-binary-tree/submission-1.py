# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(root):
            if not root:
                return 0

            nonlocal isBalanced
            left, right = 0, 0

            if root.left:
                left = 1 + dfs(root.left)
            if root.right:
                right = 1 + dfs(root.right)
            if abs(left - right) > 1:
                isBalanced = False

            return max(left, right)

        dfs(root)
        return isBalanced