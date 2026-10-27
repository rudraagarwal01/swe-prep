# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # dummy handles the case where left == 1 (head changes)
        # creates a node of val = 0 and next points to head
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # curr is the node at left index
        curr = prev.next

        # each round moves the node after curr to the front of the section
        # loop the length of right - left
        for _ in range(right - left):
            next_node = curr.next           # node we are moving
            curr.next = next_node.next      # unlink next_node from its spot
            next_node.next = prev.next      # point next_node at the current front of the section
            prev.next = next_node           # make next_node the new front

        return dummy.next






