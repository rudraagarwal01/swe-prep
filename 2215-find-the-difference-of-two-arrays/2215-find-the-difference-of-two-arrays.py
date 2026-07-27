class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # sets remove duplicates automatically 
        set1 = set(nums1) 
        set2 = set(nums2)

        # allows to remove the elements that are in both 
        return [list(set1 - set2), list(set2 - set1)]