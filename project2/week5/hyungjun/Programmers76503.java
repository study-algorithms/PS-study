package project2.week5.hyungjun;

import java.util.ArrayList;
import java.util.List;

/**
 * Programmers76503
 */

public class Programmers76503 {
    static class Node {
        int id;
        int val;
        List<Node> linkedNodes = new ArrayList<>();

        Node(int id, int val) {
            this.id = id;
            this.val = val;
        }
    }

    long answer = 0;

    public long solution(int[] a, int[][] edges) {
        List<Node> nodes = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            nodes.add(new Node(i, a[i]));
        }
        for (int i = 0; i < edges.length; i++) {
            Node node1 = nodes.get(edges[i][0]);
            Node node2 = nodes.get(edges[i][1]);
            node1.linkedNodes.add(node2);
            node2.linkedNodes.add(node1);
        }
        int[] visited = new int[a.length];
        visited[0] = 1;
        dfs(visited, nodes, 0);

        if (nodes.get(0).val != 0) {
            return -1;
        }
        return answer;
    }

    public long dfs(int[] visited, List<Node> nodes, int id) {
        Node node = nodes.get(id);
        for (Node linkedNode : node.linkedNodes) {
            if (visited[linkedNode.id] == 1) {
                continue;
            }
            visited[linkedNode.id] = 1;
            node.val += dfs(visited, nodes, linkedNode.id);
        }
        answer += Math.abs(node.val);
        return node.val;
    }

    public static void main(String[] args) {
        Programmers76503 p = new Programmers76503();

        p.solution(new int[] { -5, 0, 2, 1, 2 }, new int[][] { { 0, 1 }, { 3, 4 }, { 2, 3 }, { 0, 3 } });
    }
}
// TC 6,7,8 -> Runtime Error
// 11, 17 -> Fail