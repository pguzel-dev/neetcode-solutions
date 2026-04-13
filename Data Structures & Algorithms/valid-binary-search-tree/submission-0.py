# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, current, low, high):
        if not current:
            return True
            
        if not (low < current.val < high):
            return False
            
        return (
            self.helper(current.left, low, current.val) and
            self.helper(current.right, current.val, high)
        )
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))