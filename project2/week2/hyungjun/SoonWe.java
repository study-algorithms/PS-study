package project2.week2.hyungjun;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class SoonWe {
    private Map<Integer, Player> nToP = new HashMap<>();

    public int solution(int n, int[][] results) {
        for (int i = 0; i < n; i++) {
            nToP.put(i + 1, new Player(i + 1));
        }
        for (int[] result : results) {
            nToP.get(result[0]).addWin(result[1]);
            nToP.get(result[1]).addWin(result[0]);
        }
        int answer = 0;

        for (int i = 0; i < n; i++) {
            Set<Integer> visited = dfsToWin(i + 1, new HashSet<>());
            visited.remove(i + 1);
            int len = visited.size();
            visited = dfsToLose(i + 1, new HashSet<>());
            visited.remove(i + 1);
            len += visited.size();
            if (len == n - 1) {
                answer += 1;
            }
        }

        return answer;
    }

    public Set<Integer> dfsToWin(int n, Set<Integer> visited) {
        if (visited.contains(n)) {
            return visited;
        }
        visited.add(n);

        for (Integer next : nToP.get(n).getWin()) {
            visited = dfsToWin(next, visited);
        }
        return visited;
    }

    public Set<Integer> dfsToLose(int n, Set<Integer> visited) {
        if (visited.contains(n)) {
            return visited;
        }
        visited.add(n);

        for (Integer next : nToP.get(n).getLose()) {
            visited = dfsToLose(next, visited);
        }
        return visited;
    }

    class Player {
        private int playerNum;
        private List<Integer> win;
        private List<Integer> lose;

        public Player(int n) {
            playerNum = n;
            win = new ArrayList<>();
            lose = new ArrayList<>();
        }

        public void addWin(int n) {
            win.add(n);
        }

        public void addLose(int n) {
            lose.add(n);
        }

        public List<Integer> getWin() {
            return win;
        }

        public List<Integer> getLose() {
            return lose;
        }
    }

    public static void main(String[] args) {
        SoonWe soonWe = new SoonWe();
        soonWe.solution(5, new int[][] { { 4, 3 }, { 4, 2 }, { 3, 2 }, { 1, 2 }, { 2, 5 } });
    }
}
