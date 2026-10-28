# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        is_inserted: bool = False
        def insert(root: TreeNode | None) -> None:
            nonlocal is_inserted, val
            if is_inserted or not root:
                return

            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    is_inserted = True
                insert(root.right)
            elif val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    in_inserted = True
                insert(root.left)

        insert(root) 
        return root