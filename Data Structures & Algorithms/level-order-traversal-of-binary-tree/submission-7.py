# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        results = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                current = queue.popleft()
                level.append(current.val)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            results.append(level)
        return results




        
