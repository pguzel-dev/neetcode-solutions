# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n)
# Space: O(h)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:                            # Base
                return [True, 0]                    # Return is [allowed, height]

            left = dfs(node.left)
            right = dfs(node.right)

            balanced = (
                left[0] and right[0]               # Is both left & right allowed
                and abs(left[1] - right[1]) <= 1   # Is current node's allowed
            )

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]