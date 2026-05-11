"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Suggested
# Time: O(n)
# Space: O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2copy = {None: None}

        curr = head
        while curr:
            old2copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = old2copy[curr]
            copy.next = old2copy[curr.next]
            copy.random = old2copy[curr.random]
            curr = curr.next

        return old2copy[head]