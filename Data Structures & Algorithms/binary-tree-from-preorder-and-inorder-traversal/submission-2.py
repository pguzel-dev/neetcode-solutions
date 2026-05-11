# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Second suggested solution
# Time: O(n)
# Space: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # value -> index in inorder
        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            # no nodes in this range
            if left > right:
                return None

            # preorder gives current root
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            # split inorder into left/right subtrees
            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)