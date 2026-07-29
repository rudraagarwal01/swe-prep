# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         min = nums[0]
#         sort = sorted(nums)

#         for num in sort:
#             if num < min:
#                 min = num
#         return min
# O(n) 


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        
