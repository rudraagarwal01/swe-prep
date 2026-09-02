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

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Both are null -> identical
        if not root and not subRoot:
            return True
        
        # One is null or values differ -> not identical
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        # Recurse strictly on corresponding left and right subtrees
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)