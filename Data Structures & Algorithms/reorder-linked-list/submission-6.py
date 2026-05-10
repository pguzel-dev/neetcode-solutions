# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Derived Solution
# Fast Slow Pointers
# Reverse Linked List
# Time: O(n)
# Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_n = head
        prev_n = None

        while curr_n:
            next_node = curr_n.next   # save where to go next
            curr_n.next = prev_n      # reverse the arrow
            prev_n = curr_n           # move previous forward
            curr_n = next_node        # move current forward

        return prev_n

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse second half
        second = self.reverseList(slow.next)
        slow.next = None  # cut the list into two halves
        
        # 3. Merge two halves
        first = head
        while second:
            # Step 1: save next nodes
            first_next = first.next
            second_next = second.next

            # Step 2: connect first → second
            first.next = second

            # Step 3: connect second → next of first
            second.next = first_next

            # Step 4: move pointers forward
            first = first_next
            second = second_next