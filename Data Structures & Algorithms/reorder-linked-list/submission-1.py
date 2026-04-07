# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Brute force with double pointers
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # store all nodes in an array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        # reorder using two pointers
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1

            if i == j:
                break

            arr[j].next = arr[i]
            j -= 1

        # mark the new end
        arr[i].next = None