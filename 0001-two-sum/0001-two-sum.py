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
        # Key is the number
        # Value is the index
        for i, num in enumerate(nums):
            complement = target - num
            # Search in the hashmap with the key so the number
            if complement in seen:
                return [seen[complement], i]
            else: 
                seen[num] = i
# O(N)

