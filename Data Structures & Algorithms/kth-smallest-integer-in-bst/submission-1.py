# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        count = k
        def inorder(root):
            nonlocal count, res
            if not root:
                return 
            inorder(root.left)
            count -= 1
            if count == 0:
                res = root.val
                return
            inorder(root.right)
            return res
        
        inorder(root)
        return res