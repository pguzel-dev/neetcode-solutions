# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        
        while current:
            # Both are to the right
            if p.val > current.val and q.val > current.val:
                current = current.right
            # Both are to the left
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # They go different ways
            else:
                return current