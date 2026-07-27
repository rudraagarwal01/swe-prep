# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # FILO
        stack = []
        curr = head

        # Add all the values onto stack
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        
        # stack (FILO) puts the nodes in backwards
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True


        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # curr = slow
        # prev = None

        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr 
        #     curr = next_node
        # left = head
        # right = prev

        # while right:  # We only need to check until the right half runs out
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next
            
        # return True




