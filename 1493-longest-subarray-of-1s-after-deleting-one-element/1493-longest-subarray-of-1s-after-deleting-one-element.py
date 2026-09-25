class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = ans = curr = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1

            # removes all zeros from left except 1 (if there)
            while curr > 1:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            
            # not right - left + 1 because you always need to remove 1
            ans = max(ans, right - left)

        return ans