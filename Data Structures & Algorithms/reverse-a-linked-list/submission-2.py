# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
   p
    [0,1,2,3]
     c 
       n
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        return prev