# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Suggested Solution
# Fast Slow Pointers
# Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        
        while current:
            next_node = current.next # save a pointer to next one as to not loose track
            current.next = previous # readjust the next of current to be prev
            previous = current # now that we are done with previous, update it to be the current
            current = next_node # and therefore move the current to be next that we saved before
        
        return previous

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