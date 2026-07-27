# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # create set to automatically remove duplicates
        # # this could also work for unsorted list
        # seen = set()
        # dummy = ListNode(next=head)
        # curr = dummy

        # while curr.next:
        #     if curr.next.val in seen:
        #         curr.next = curr.next.next
        #     else:
        #         seen.add(curr.next.val)
        #         curr = curr.next

        # return dummy.next

        # this is optimal solution for sorted list
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head