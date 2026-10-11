"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = node = Node(x = 0)
        cp_list = head
        rand: list[Node | None, Node | None] = { None : None}

        while cp_list:
            node.next = Node(cp_list.val)
            node = node.next
            rand[cp_list] = node
            cp_list = cp_list.next
        
        cp_list = head
        node = dummy.next
        while cp_list:
            node.random = rand[cp_list.random]
            cp_list = cp_list.next
            node = node.next
            
        return dummy.next
        