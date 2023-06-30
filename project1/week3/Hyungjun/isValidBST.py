# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min_v, max_v):
            if not root:
                return True
            if root.val <= min_v or root.val >= max_v:
                return False
            return helper(root.left, min_v, root.val) and helper(root.right, root.val, max_v)
        MAX = 2**31+1
        return helper(root, -MAX, MAX)
