class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = len(nums) + 1
        left = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                length = right - left + 1
                min_len = min(min_len, length)
                curr -= nums[left]
                left += 1
            
        if min_len != len(nums) + 1:
            return min_len
        else: 
            return 0
        