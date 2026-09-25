class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = ans = curr = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1

            while curr > 1:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            
            ans = max(ans, right - left)
            
        return ans