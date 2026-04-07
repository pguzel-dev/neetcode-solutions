# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# A better merging method, 2 at a time
class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        dummy = ListNode(0)
        new = dummy

        while c1 and c2:
            if c1.val < c2.val:
                new.next = c1
                c1 = c1.next
            else:
                new.next = c2
                c2 = c2.next
            new = new.next

        if c1:
            new.next = c1
        if c2:
            new.next = c2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                
                # to prevent accesing non existing variables if the number is odd 
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                merged.append(self.mergeTwoLists(l1, l2))

            lists = merged

        return lists[0]