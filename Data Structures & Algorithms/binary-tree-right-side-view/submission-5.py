# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])

        while q:
            qLen = len(q)
            curLevel = []
            node = None #maintains values of current level
            while qLen:
                cur = q.popleft()
                # curLevel.append(cur.val)
                node = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                qLen -= 1
            # if curLevel:
            if node:
                res.append(node.val) # we're interested only in the last element as we process from left to right
        return res