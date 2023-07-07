from typing import *
# Very good code I think, it is not mine I think

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left and root.left.val >= root.val:
            return False

        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBSTRange(root.left, [-2**31, root.val-1]) and self.isValidBSTRange(root.right, [root.val+1, 2**31])

    def isValidBSTRange(self, root, range) -> bool:
        left, right = range[0], range[1]
        if not root:
            return True

        if root.val < left or root.val > right or left > right:
            return False

        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
            
        return self.isValidBSTRange(root.left, [left, root.val-1]) and self.isValidBSTRange(root.right, [root.val+1, right])