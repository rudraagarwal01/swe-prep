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

        # Use two pointer approach
        # find the mid index
        while left < right:
            mid = (left + right) // 2

            # compare the num at mid index and the last number in array
            # if mid num is bigger than right num then move the left index to mid + 1
            # we know that all nums to the left of mid can be elimated
            if nums[mid] > nums[right]:
                left = mid + 1
            # if mid num is smaller we know that everything to the right of mid can be elimated
            else:
                right = mid
        return nums[left]
# O(log n)

# Example walk through
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left = 0
#         right = len(nums) - 1

#         # [1, 2, 3, 4, 5] --> [3, 4, 5, 1, 2]

#         # first: left = 0, right = 4
#         # second: left = 3, right = 4
#         while left < right:
#             # (4 - 0) / 2 = 2
#             # mid = 2
#             # mid = 3.5 -> 3
#             mid = (right - left) // 2

#             # 5 > 2 -> true
#             # 1 > 2 -> false
#             if nums[mid] > nums[right]:
#                 # 2 + 1
#                 # left = 3
#                 left = mid + 1
#             # right = 3
#             else:
#                 right = mid
#         # return 1
#         return nums[left]
