/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> copyFromOld = new HashMap<>();
        Node curr = head;
        while (curr != null) {
            Node copy = new Node(curr.val);
            copyFromOld.put(curr, copy);
            curr = curr.next;
        }

        curr = head;
        while (curr != null) {
            Node copy = (copyFromOld.get(curr));
            copy.next = copyFromOld.get(curr.next);
            copy.random = copyFromOld.get(curr.random);
            curr = curr.next; 
        }

        return copyFromOld.get(head);
    }
}
