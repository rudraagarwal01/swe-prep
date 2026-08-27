# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # use two pointers 
        slow = head
        fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None # split list into two halves

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # merge the two halves
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2


        