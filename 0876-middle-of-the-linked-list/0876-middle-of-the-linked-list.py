# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # slow will reach middle when fast reaches the end
        # ensure that fast and and fast.next are pointing to something
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        return slow
