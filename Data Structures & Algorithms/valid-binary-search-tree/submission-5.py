# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def checkSubtree(node:Optional[TreeNode],minValue,maxValue) -> bool:
            if not node:
                return True
            if node.val <= minValue or node.val >= maxValue:
                return False
            left  = checkSubtree(node.left,minValue,node.val)
            right  = checkSubtree(node.right,node.val,maxValue)

            return left and right
        # Instead of passing nodes or values, we're giving a range for the value to fit
        left = checkSubtree(root.left,float('-inf'),root.val)
        right = checkSubtree(root.right,root.val,float('inf'))

        return left and right
