package project2.week1.Hyungjun;

import java.util.Objects;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {
    public boolean isValidBST(TreeNode root) {
        
        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean helper(TreeNode node, long minVal, long maxVal) {
        if (Objects.isNull(node)) {
            return true;
        }
        if (node.val <= minVal || node.val >= maxVal) {
            return false;
        }
        return helper(node.left, minVal, node.val) && helper(node.right, node.val, maxVal);
    }
    public static void main(String[] args) {
        TreeNode root = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        Solution solution = new Solution();
        if (solution.isValidBST(root) == true) {
            System.out.println("success");
        }
    }
}