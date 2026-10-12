# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        
        has_carry = False
        while l1 and l2:
            if has_carry:
                val_sum = l1.val + l2.val + 1
                has_carry = False
            else:
                val_sum = l1.val + l2.val

            if val_sum > 10:
                val_sum -= 10
                has_carry = True

            node.next = ListNode(val_sum)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        if has_carry:
            if l1:
                node.next = NodeList(l1.val + 1)
                node = node.next
                l1 = l1.next
            elif l2:
                node.next = NodeList(l2.val + 1)
                node = node.next
                l2 = l2.next
            else:
                node.next = ListNode(1)

        if l1:
            node.next = l1

        if l2:
            node.next = l2

        return dummy.next
