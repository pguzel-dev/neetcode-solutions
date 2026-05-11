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
        carry = 0

        while c1 or c2:
            if not c1:                      # l1 ended first
                prev.next = c2              # attach remaining l2 to l1
                c1 = c2                     # continue using attached nodes
                c2 = None                   # avoid double-counting l2

            total = c1.val + carry          # start with current l1 value

            if c2:                          # add l2 value if available
                total += c2.val
                c2 = c2.next

            c1.val = total % 10             # store digit
            carry = total // 10             # update carry

            prev = c1                       # remember last node
            c1 = c1.next                    # move forward

        if carry:                           # final carry
            prev.next = ListNode(carry)

        return l1