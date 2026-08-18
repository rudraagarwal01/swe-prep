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

        # [1, 2, 3, 4, 5] --> [3, 4, 5, 1, 2]

        # first: left = 0, right = 4
        # second: left = 3, right = 4
        while left < right:
            # (4 - 0) / 2 = 2
            # mid = 2
            # mid = 0.5 -> 0
            mid = left + (right - left) // 2

            # 5 > 2 --> true
            if nums[mid] > nums[right]:
                # 2 + 1
                # left = 3
                left = mid + 1
            else:
                right = mid

        return nums[left]
    
# O(log n)
