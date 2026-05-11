# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def maxDepth(curr) -> int:
            if not curr: return 0
            
            left, right = maxDepth(curr.left), maxDepth(curr.right)
            if left is False or right is False:
                return False
            if abs(left - right) > 1:
                return False

            depth = 1 + max(left, right)

            return depth
        
        return False if maxDepth(root) is False else True