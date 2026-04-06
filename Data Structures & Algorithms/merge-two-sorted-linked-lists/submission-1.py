# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# GPT optimization
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        dummy = ListNode(0)
        new = dummy

        while c1 and c2:
            if c1.val < c2.val:
                new.next = c1
                new = c1
                c1 = c1.next
            else:
                new.next = c2
                new = c2
                c2 = c2.next

        if c1:
            new.next = c1
        if c2:
            new.next = c2

        return dummy.next