class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the arrays 
        merged = nums1 + nums2 
        # Sort the merged arrays
        merged.sort()
        # divide the array by two to find the median of the array
        n = len(merged)
        mid = n // 2
        # if even number of elements then return the average of the two middle elements 
        if n % 2 == 1: 
            return float(merged[mid])

        return float(merged[mid-1] + merged[mid]) / 2