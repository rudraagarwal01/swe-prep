# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # save next (2) (3) (4) (5) (None)
            curr.next = prev        # reverse pointer (1 -> None) (2 -> 1) (3 -> 2) (4 -> 3) (5 -> 4)
            prev = curr             # move prev forward (prev = 1) (prev = 2) (prev = 3) (prev = 4) (prev = 5)
            curr = next_node        # move curr forward (curr = 2) (curr = 3) (curr = 4) (curr = 5) (curr = None)

        return prev

       

        
            
            

            
       

