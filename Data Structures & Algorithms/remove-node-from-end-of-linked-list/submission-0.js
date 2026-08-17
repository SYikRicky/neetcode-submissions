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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        if (n === 1) return null;
        
        let prev = null;
        let count = 1;
        while (head) {
            let nxt = head.next;
            head.next = prev;
            prev = head;
            head = nxt;
        }
        head = prev;
        let actionNode = head;
        console.log(head);
        prev = null;
        while (count !== n) {
            count++;
            prev = head;
            actionNode = actionNode.next;
        }

        let nxt = actionNode.next;
        prev.next = nxt;
        
        console.log(head);
        prev = null;
        while (head) {
            let nxt = head.next;
            head.next = prev;
            prev = head;
            head = nxt;
        }

        return prev;
    }
}
