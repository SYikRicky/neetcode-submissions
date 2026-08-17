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
    public void reorderList(ListNode head) {
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        } 

        ListNode node_right = slow.next;
        slow.next = null;
        ListNode prev_right = null;
        while (node_right != null) {
            ListNode temp = node_right.next;
            node_right.next = prev_right;
            prev_right = node_right;
            node_right = temp;
        }

        while (head != null && prev_right != null) {
            ListNode nxt_left = head.next;
            ListNode nxt_right = prev_right.next;
            head.next = prev_right;
            head = nxt_left;
            prev_right.next = head;
            prev_right = nxt_right; 
        }
    }
}
