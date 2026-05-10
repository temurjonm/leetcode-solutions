# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
[2,4,6,8]

- find the mid divide by 2
- reverse 2 portion of list
- merge them 
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def findMiddleList(linkedList):
            slow = fast = linkedList

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverseList(curr):
            prev = None

            while curr:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next

            return prev

        mid = findMiddleList(head)
        second = reverseList(mid.next)
        mid.next = None

        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        return head
