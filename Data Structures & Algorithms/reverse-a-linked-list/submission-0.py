# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        head = stack.pop()
        cur = head
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return head