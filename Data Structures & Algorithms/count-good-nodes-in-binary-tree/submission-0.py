# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,prevMax):
            # if node.val > prevMax:
            #     return 1
            # else:
            #     return 0
            if not node:
                return 0
            left = dfs(node.left,max(node.val,prevMax))
            right = dfs(node.right,max(node.val,prevMax))

            return left + right + (1 if node.val>=prevMax else 0)
        
        return dfs(root,root.val)