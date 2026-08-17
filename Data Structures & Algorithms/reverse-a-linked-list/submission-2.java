/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        // prev 0 1 2 3
        // 0 -> prev, 0(prev) 1(head)
        // 1 -> 0 -> null, 1(prev) 2(head)
        // 2 -> 1 -> 0 -> null, 2(prev) 3(head)
        // 3 -> 2 -> 1 -> 0 -> null, 3(prev) null(head)
        ListNode prev = null;
        while (head != null) {
            ListNode nxt = head.next;
            head.next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }
}
