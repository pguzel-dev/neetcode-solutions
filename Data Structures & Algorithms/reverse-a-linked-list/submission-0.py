# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Derived/Suggested Solution
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



