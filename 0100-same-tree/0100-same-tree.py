# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use deque for Trees
        
        # create deque with both p and q (tuple)
        queue = deque([(p, q)]) 

        while queue:
            # pop the first node (root) in each tree
            node1, node2 = queue.popleft()

            # if both empty then continue 
            if not node1 and not node2:
                continue 
            
            # if either one is empty or they are not equal then return false
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # add their children to conintue comparison
            # compare as tuples!!
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    
        return True


        
    
    


        


            
            


    