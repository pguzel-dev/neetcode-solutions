# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(node) -> int | bool:
            if not node:                        # Base case
                return 0

            left = maxDepth(node.left)          # Get both sides depth
            right = maxDepth(node.right)

            if left is False or right is False: # Must carry false up
                return False

            if abs(left - right) > 1:           # Max diff can only be 1
                return False

            return 1 + max(left, right)         # Carry depth up

        return False if maxDepth(root) is False else True