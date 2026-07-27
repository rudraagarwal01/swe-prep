# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy

        while curr.next:
            # if mutation is needed it keeps checking the new value after curr
            if curr.next.val == val:
                curr.next = curr.next.next # mutation
            else:
                curr = curr.next # iteration
        
        # dummy is just a random node
        return dummy.next