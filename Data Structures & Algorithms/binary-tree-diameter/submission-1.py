# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Suggested solution
# Time: O(n)
# Space: O(h)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # returns height and updates result
        def dfs(curr):
            if not curr:
                return 0

            left, right = dfs(curr.left), dfs(curr.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res