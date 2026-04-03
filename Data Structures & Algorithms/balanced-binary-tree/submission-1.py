# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = True
    def dfs(self,root):
            if not root:
                return 0
            left = self.dfs(root.left)
            right =self.dfs(root.right)
            return 1+max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if abs(self.dfs(root.left)-self.dfs(root.right)) > 1:
            return False
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        return left and right

            