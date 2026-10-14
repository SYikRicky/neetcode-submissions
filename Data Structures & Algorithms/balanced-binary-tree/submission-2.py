# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        def dfs(curr: TreeNode | None) -> int:
            if not curr:
                return 0
            
            return 1 + max(dfs(curr.left), dfs(curr.right))

        left_height = dfs(root.left)
        right_height = dfs(root.right)
        
        return abs(left_height - right_height) <= 1