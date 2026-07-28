class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        zero_count = 0
        left = 0

        for right in range(len(nums)):
            # count the numbers of zeros
            if nums[right] == 0:
                zero_count += 1
            
            # If we have more zeros than k, shrink window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len