
package project2.week5.hyungjun;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Leetcode138
 */
public class Leetcode138 {

    public Node copyRandomList(Node head) {
        List<Node> nodeList = new ArrayList<>();
        HashMap<Integer, Integer> addrToId = new HashMap<>();
        int i = 0;
        while (head != null) {
            nodeList.add(head);
            int addr = System.identityHashCode(head);
            addrToId.put(addr, i);
            head = head.next;
            i++;
        }

        List<Node> copiedNodeList = new ArrayList<>();

        for (i = 0; i < nodeList.size(); i++) {
            Node node = nodeList.get(i);
            copiedNodeList.add(new Node(node.val));
        }
        for (i = 0; i < nodeList.size(); i++) {
            Node random = nodeList.get(i).random;
            if (random != null) {
                int id = addrToId.get(System.identityHashCode(random));
                copiedNodeList.get(i).random = copiedNodeList.get(id);
            }
            if (i < nodeList.size() - 1) {
                copiedNodeList.get(i).next = copiedNodeList.get(i + 1);
            }
        }

        return copiedNodeList.get(0);
    }

}

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