# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoList(list1, list2):
            if not list1: return list2
            if not list2: return list1

            while list1 and list2:
                if list1.val < list2.val:
                    list1.next = mergeTwoList(list1.next, list2)
                    return list1
                else:
                    list2.next = mergeTwoList(list1, list2.next)
                    return list2
        
        if not lists: return None

        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergeList.append(mergeTwoList(l1, l2))
            lists = mergeList
        return lists[0]
