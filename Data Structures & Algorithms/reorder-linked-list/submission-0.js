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
     * @return {void}
     */
    reorderList(head) {
        // 248(s) null | 6 10 null(f)
       
        let slowPtr = head;
        let fastPtr = head.next;
        while (fastPtr && fastPtr.next) {
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;
        }

        let secondList = slowPtr.next;
        let prev = null;
        slowPtr.next = null; 
        while (secondList) {
            let nxt = secondList.next;
            secondList.next = prev;
            prev = secondList;
            secondList = nxt;
        }

        secondList = prev;
        let firstList = head;
        while (firstList && secondList) {
            let firstNxt = firstList.next;
            let secondNxt = secondList.next;
            firstList.next = secondList;
            secondList.next = firstNxt;
            firstList = firstNxt;
            secondList = secondNxt;
        }
    }
}
