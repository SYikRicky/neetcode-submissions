# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack: list[TreeNode | None] = [(root, False)]
        res: list[int] = []
        
        while stack:
            data: tuple[TreeNode | None] = stack.pop()
            node: TreeNode = data[0]
            visited: bool = data[1]
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res