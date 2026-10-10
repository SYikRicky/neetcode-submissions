# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            return head.next

        prev, after = head, head
        for i in range(n - 1):
            prev = prev.next
            print(f"prev: {prev.val}")

        for i in range(n + 1):
            if after.next:
                after = after.next
            else:
                break
            print(f"after: {after.val}")
        prev.next = after
        return head