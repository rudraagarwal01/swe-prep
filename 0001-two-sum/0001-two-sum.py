# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
# O(N^2)

class Solution:
    def twoSum(self, nums, target):
        seen = {} # dictionary 
        
        # enumerate iterates and basically stores index and number
        # Key is the number(complement)
        # Value is the index
        for i, num in enumerate(nums):
            complement = target - num
            # Search in seen with complement
            # if value exists return its index and curr index
            if complement in seen:
                return [seen[complement], i]
            # if complement not in seen then store curr num in seen for future
            else: 
                seen[num] = i
# O(N)

