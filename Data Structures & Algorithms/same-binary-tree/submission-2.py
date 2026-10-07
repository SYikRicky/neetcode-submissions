# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return None
            val = [root.val]
            if root.left:
                val += [root.left.val, *dfs(root.left)]
            else:
                val += [None]
            if root.right:
                val += [root.right.val, *dfs(root.right)]
            else:
                val += [None]
            return val

        return dfs(p) == dfs(q)