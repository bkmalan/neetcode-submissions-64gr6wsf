# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root):
            if not root:
                return []
            left = inorder(root.left)
            right = inorder(root.right)
            return left + [root.val] + right
        
        res = inorder(root)
        return res[k - 1]