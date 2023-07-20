package project2.week2.hyungjun;

import java.util.HashMap;
import java.util.Map;

public class LongestConsecutiveSequence2 {

    public int longestConsecutive(int[] nums) {

        Map<Integer, Integer> numToIndex = new HashMap<>();
        UnionFind unionFind = new UnionFind(nums.length);
        for (int i = 0; i < nums.length; i++) {
            if (numToIndex.containsKey(nums[i])) {
                continue;
            }
            if (numToIndex.containsKey(nums[i] - 1)) {
                unionFind.union(i, numToIndex.get(nums[i] - 1));

            }
            if (numToIndex.containsKey(nums[i] + 1)) {
                unionFind.union(i, numToIndex.get(nums[i] + 1));
            }

            numToIndex.put(nums[i], i);
        }
        return unionFind.getLargestComponentSize();
    }

    class UnionFind {
        private int[] parent;
        private int[] size;

        public UnionFind(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int find(int x) {
            if (parent[x] == x) {
                return x;
            }
            return parent[x] = find(parent[x]);
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                parent[rootX] = rootY;
                size[rootY] += size[rootX];
            }
        }

        public int getLargestComponentSize() {
            int maxSize = 0;
            for (int i = 0; i < parent.length; i++) {
                if (parent[i] == i && size[i] > maxSize) {
                    maxSize = size[i];
                }
            }
            return maxSize;
        }
    }

}
