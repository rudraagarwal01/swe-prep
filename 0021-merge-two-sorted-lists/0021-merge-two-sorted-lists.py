# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode() # initialize merged list

        tail = merged # tail keeps track of last node in merged list

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 # make next point to node in list1
                list1 = list1.next # interate the list to next node
            else: 
                tail.next = list2 # make next point to node in list2
                list2 = list2.next # iterate the list to next node
            
            tail = tail.next # iterate tail to next node

        # list2 is empty
        if list1:
            tail.next = list1
        # list1 is empty
        elif list2:
            tail.next = list2
        
        # return merged.next because that is where the list starts 
        return merged.next
        


