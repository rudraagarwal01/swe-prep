# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Can also use a queue to avoid recursion
        # empty tree
        if not root:
            return 0
        # recursively find the depth of the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # root plus the longer subtree 
        return 1 + max(left, right)

