# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Alternative, worse solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        return previous

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: reverse
        head = self.reverseList(head)

        # Step 2: remove nth from start
        if n == 1:
            head = head.next
        else:
            current = head
            for _ in range(n - 2):
                current = current.next
            
            current.next = current.next.next

        # Step 3: reverse back
        return self.reverseList(head)