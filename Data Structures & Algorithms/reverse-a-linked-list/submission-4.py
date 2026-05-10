# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
