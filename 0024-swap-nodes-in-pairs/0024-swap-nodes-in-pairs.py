# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # 0 or 1 nodes: nothing to swap
        if not head or not head.next:
            return head

        # the second node becomes the new head after the first swap
        dummy = head.next
        # prev is the tail of the previous (already swapped) pair
        prev = None

        # keep going while there is a full pair to swap
        while head and head.next:
            # connect the previous pair's tail to the new front of this pair
            # (head.next is about to become the front of this pair)
            if prev:
                prev.next = head.next
            # head will be the tail of this pair after the swap
            prev = head

            # save the start of the next pair before we change any links
            next_node = head.next.next
            # second node points back to the first node (the swap)
            head.next.next = head

            # first node (now the tail) points to the next pair
            head.next = next_node
            # move to the start of the next pair
            head = next_node

        # dummy is the original second node, which is the new head
        return dummy