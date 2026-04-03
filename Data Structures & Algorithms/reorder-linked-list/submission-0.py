# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       slow,fast = head,head.next
       while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

       curr = slow.next
       prev = slow.next = None
        # reverse second list
       while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
       list1 = head
       list2 = prev
       print(list1.val)
       while list2:
        tmp = list1.next
        tmp2 = list2.next
        list1.next = list2
        list2.next = tmp
        list1 = tmp
        list2 = tmp2

        
            


        


            
