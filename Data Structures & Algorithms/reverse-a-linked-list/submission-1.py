# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursive Solution
# Time: O(n)
# Memory: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head:
            return None
        
        # Assume current node might become the new head
        newHead = head
        
        # If there's a next node, keep going deeper
        if head.next:
            # Recursively reverse the rest of the list
            newHead = self.reverseList(head.next)
            
            # At this point:
            # head -> next_node
            # We want: next_node -> head (reverse the link)
            head.next.next = head
        
        # Break the original forward link
        head.next = None
        
        # Always return the new head (from the bottom of recursion)
        return newHead