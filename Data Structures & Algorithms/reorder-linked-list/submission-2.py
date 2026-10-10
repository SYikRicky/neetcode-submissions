# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # invert
        prev, second_list = None, slow
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # merge
        node = ListNode()
        while prev and prev != head:
            node.next = head
            head = head.next
            node = node.next

            node.next = prev
            prev = prev.next
            node = node.next

        # excess node in 2nd half
        if prev:
            node.next = prev
