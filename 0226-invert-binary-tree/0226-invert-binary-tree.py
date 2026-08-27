# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case: empty tree
        if not root:
            return None 

        # put only the root into queue
        queue = deque([root])

        while queue:
            # pulls front node from queue
            node = queue.popleft()
            
            # swap left and right nodes
            node.left, node.right = node.right, node.left

            # check if there is a node then append to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # return full inverted tree
        return root