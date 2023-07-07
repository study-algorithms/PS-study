package project2.week1.Hyungjun;

import java.util.HashMap;
import java.util.HashSet;

class Solution2 {
    public int[] solution(String[] gems) {
        int[] answer = new int[2];
        HashSet<String> gemSet = new HashSet<>();
        for (String g : gems) {
            gemSet.add(g);
        }
        int start=0, end=0;
        int len = Integer.MAX_VALUE;
        HashMap<String, Integer> gemToNum = new HashMap<>();

        while (true) {
            if (gemToNum.size() == gemSet.size()) {
                Integer startNum = gemToNum.get(gems[start]);
                if (startNum == 1) {
                    gemToNum.remove(gems[start]);
                } else {
                    gemToNum.put(gems[start], startNum-1);
                }
                start += 1;
            } else if (end >= gems.length){
                break;
            } else {
                gemToNum.put(gems[end], gemToNum.getOrDefault(gems[end], 0)+1);
                end += 1;
            }
            if (gemToNum.size() == gemSet.size()) {
                if (end-start < len){
                    len = end - start;
                    answer[0] = start + 1;
                    answer[1] = end;
                }
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        Solution2 solution = new Solution2();
        String[] input = {"DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"};
        int[] answer = solution.solution(input);
        System.out.printf("%d, %d",answer[0], answer[1]);
    }
}
