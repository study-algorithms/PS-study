# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.validateBST(root, -2**31-1, 2**31+1)

    def validateBST(self, node, min, max):
        if node.left is not None:
            if node.left.val >= node.val:
                return False
            if node.left.val <= min:
                return False
            if not self.validateBST(node.left, min, node.val):
                return False
            
        if node.right is not None:
            if node.right.val <= node.val:
                return False
            if node.right.val >= max:
                return False
            if not self.validateBST(node.right, node.val, max):
                return False
        
        return True
