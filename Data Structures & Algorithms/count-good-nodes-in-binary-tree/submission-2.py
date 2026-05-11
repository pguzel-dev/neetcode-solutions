# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(node, max_seen):
            if not node:
                return

            if node.val >= max_seen:
                self.counter += 1
                max_seen = node.val
            
            dfs(node.left, max_seen)
            dfs(node.right, max_seen)
        
        dfs(root, -float('inf'))
        return self.counter
            
            