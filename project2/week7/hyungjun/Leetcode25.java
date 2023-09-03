import java.util.Stack;

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
    public ListNode reverseKGroup(ListNode head, int k) {
        //* 0->1->2->3->4->5->6
        //* |           |   
        //* begin       end
        //* 0->3->2->1->4->5->6
        //*          |  |
        //*      begin end

        if (head == null || head.next == null || k ==1 ) { return head; }
        ListNode dummyHead = new ListNode(-1, head);
        ListNode begin = dummyHead;

        int i = 0;
        while (head != null) {
            i++;
            if (i % k == 0) {
                begin = reverse(begin, head.next);
                head = begin.next;
            } else {
                head = head.next;
            }
        }
        return dummyHead.next;
    }

    public ListNode reverse(ListNode begin, ListNode end) {
        ListNode curr = begin.next;
        ListNode next, first;
        ListNode prev = begin;

        first = curr;
        while (curr != end) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        begin.next = prev;
        first.next = curr;
        return first;
    }
}
class Solution2 {
    public ListNode reverseKGroup(ListNode head, int k) {
        int count=0;
        List<ListNode> listNodeList = new ArrayList<>();
        Stack<ListNode> st = new Stack<>();
        while (head != null) {
            if (count == k ){
                while(!st.empty()) {
                    listNodeList.add(st.pop());
                }
                count = 0;
            }
            count += 1;
            st.push(head);
            head = head.next;
        }
        if (st.size() < k) {
            Stack<ListNode> revSt = new Stack<>();
            while (!st.empty()) { revSt.push(st.pop()); }
            while (!revSt.empty()) { listNodeList.add(revSt.pop()); }
        } else {
            while (!st.empty()) { listNodeList.add(st.pop()); }
        }

        for(int i = 0; i < listNodeList.size()-1; i++) {
            listNodeList.get(i).next = listNodeList.get(i+1);
        }
        listNodeList.get(listNodeList.size()-1).next = null;
        return listNodeList.get(0);
    }
}
