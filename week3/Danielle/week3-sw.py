class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lo, hi):
            if not node:
                return True
            if not lo < node.val < hi:
                return False
            left = dfs(node.left, lo, node.val)   
            right = dfs(node.right, node.val, hi) 

            return left and right
        return dfs(root, float('-inf'), float('inf'))
