# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(h)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr: Optional[TreeNode], min_bound, max_bound) -> bool:
            if not curr:
                return True
            
            if not min_bound < curr.val < max_bound:
                return False

            return (dfs(curr.left, min_bound, curr.val) and dfs(curr.right, curr.val, max_bound))

        return dfs(root, -float('inf'), float('inf'))