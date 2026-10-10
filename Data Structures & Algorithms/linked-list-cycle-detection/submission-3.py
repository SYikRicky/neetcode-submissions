# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        stack = [head]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                if head.next:
                    head = head.next
                    stack.append(head)
            else:
                return True
        return False