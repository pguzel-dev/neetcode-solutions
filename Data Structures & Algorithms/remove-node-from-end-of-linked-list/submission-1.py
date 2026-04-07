# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Initial solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # Move fast n+1 steps ahead
        # (+1 since we end at the end of the list, not last node)
        for _ in range(n + 1):
            if not fast:
                return head.next  # remove head
            fast = fast.next

        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove nth node
        slow.next = slow.next.next

        return head