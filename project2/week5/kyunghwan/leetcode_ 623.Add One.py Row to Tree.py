# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def add(node, depth, now_depth):
            if not node:
                return 
            
            if depth == 1:
                return TreeNode(val, left=node)
            
            elif now_depth == depth-1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
                return node

            else:
                add(node.left, depth, now_depth+1)
                add(node.right, depth, now_depth+1)
            return node

        return add(root, depth, 1)

a = solution()
print(a.addOneRow(root = [4,2,6,3,1,5], val = 1, depth = 2))
#[4,1,1,2,null,null,6,3,1,5]
