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
        old2copy = {None: None}                     # map old nodes to copies

        curr = head                                 # start at head
        while curr:                                 # create copy nodes
            old2copy[curr] = Node(curr.val)         # copy current node
            curr = curr.next                        # move forward

        curr = head                                 # reset pointer
        while curr:                                 # connect pointers
            copy = old2copy[curr]                   # get copied node
            copy.next = old2copy[curr.next]         # copy next link
            copy.random = old2copy[curr.random]     # copy random link
            curr = curr.next                        # move forward

        return old2copy[head]                       # return copied head