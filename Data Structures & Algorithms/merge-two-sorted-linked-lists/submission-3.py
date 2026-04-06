# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Initial Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        new = ListNode(0)
        pointer = new

        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    pointer.next = c1
                    c1 = c1.next
                else:
                    pointer.next = c2
                    c2 = c2.next
            elif c1:
                pointer.next = c1
                c1 = c1.next
            elif c2:
                pointer.next = c2
                c2 = c2.next
            pointer = pointer.next

        return new.next