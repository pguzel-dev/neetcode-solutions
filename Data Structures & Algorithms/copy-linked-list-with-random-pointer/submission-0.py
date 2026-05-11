"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Deep copy of a regular list NOT RANDOM
# Time: O(n)
# Space: O(1)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr_og = head
        curr_new = dummy
        copy_map = {}

        while curr_og:
            new_node = Node(curr_og.val)        # Create new
            curr_new.next = new_node            # Assign as new list's node's next
            curr_new = curr_new.next            # iterate new list
            copy_map[curr_og] = curr_new        # Add to map after iterating
            curr_og = curr_og.next              # iterate og list
            
        curr_og = head
        curr_new = dummy.next
        while curr_og:
            curr_new.random = copy_map[curr_og.random] if curr_og.random else None
            curr_og = curr_og.next              # iterate og list
            curr_new = curr_new.next            # iterate new list

        return dummy.next