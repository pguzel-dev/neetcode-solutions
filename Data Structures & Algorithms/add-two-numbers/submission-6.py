# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n + m)
# Space: O(max(n, m))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        prev = None
        remainder = 0

        while c1 or c2:
            if not c1:
                prev.next = c2  # ignore, they are non empty
                c1 = c2
                c2 = None       # prevents us from double counting             

            total = c1.val + remainder
            
            if c2:
                total += c2.val
                c2 = c2.next

            c1.val = total % 10
            remainder = total // 10

            prev = c1
            c1 = c1.next

        if remainder != 0:                           # final carry
            prev.next = ListNode(remainder)

        return l1


