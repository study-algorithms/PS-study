# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        stack = [(root, 1)]
        
        while stack:
            data = stack.pop()
            curr = data[0]
            currDepth = data[1]

            if currDepth < depth-1:
                if curr.left:
                    stack.append((curr.left, currDepth+1))
                if curr.right:
                    stack.append((curr.right, currDepth+1))
            elif currDepth == depth-1:
                tempLeft, tempRight = None, None
                if curr.left:
                    tempLeft = curr.left
                if curr.right:
                    tempRight = curr.right
                curr.left = TreeNode(val, tempLeft, None)
                curr.right = TreeNode(val, None, tempRight)
        
        return root
                
