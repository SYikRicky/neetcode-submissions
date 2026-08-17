/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        // (tail) 0-1-2-3 (head)
        // prev = null, curr
        // null<-0, head = 1, prev = 0
        let prev = null;
        while (head !== null) {
            let nxtnode = head.next;
            head.next = prev;
            prev = head
            head = nxtnode;
        }
        return prev
    }
}
