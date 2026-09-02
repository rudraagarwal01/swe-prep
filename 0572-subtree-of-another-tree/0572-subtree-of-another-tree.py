# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        # Check if the trees rooted at the current node are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, search down the left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are null -> identical
        if not p and not q:
            return True
        
        # One is null or values differ -> not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recurse strictly on corresponding left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)