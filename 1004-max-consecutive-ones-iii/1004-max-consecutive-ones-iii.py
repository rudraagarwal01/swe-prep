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
            # move left pointer to find the zeros
            # once we can convert the 0's to 1 then stop and that is your window
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len