# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n + m)
# Space: O(max(n, m))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def num_calc(head: Optional[ListNode]) -> int:
            multiplier = 1
            total = 0
            curr = head

            while curr:
                total += curr.val * multiplier
                multiplier *= 10
                curr = curr.next
            
            return total
        
        grand_total = str(num_calc(l1) + num_calc(l2))
        dummy = ListNode(0)
        curr = dummy
        for num in grand_total[::-1]:
            num = int(num)
            next_node = ListNode(num)
            curr.next = next_node
            curr = next_node

        return dummy.next