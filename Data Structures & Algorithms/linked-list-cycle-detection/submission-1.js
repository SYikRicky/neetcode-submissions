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
     * @return {boolean}
     */
    hasCycle(head) {
        if (!head) return false;
        let fastPtr = head.next;
        let slowPtr = head;
        while (fastPtr && fastPtr.next) {
            if (fastPtr === slowPtr) return true;
            fastPtr = fastPtr.next.next;
            slowPtr = slowPtr.next;
        }
        return false;
    }
}
