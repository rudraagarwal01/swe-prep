class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        curr = 0
        min_prefix = 0

        for num in nums:
            curr += num
            # stores the all time lowest number (usually negative)
            min_prefix = min(min_prefix, curr)

        # return 1 if all positives in nums
        # return 1 - negative number to ensure you get prefix > 1
        return max(1, 1 - min_prefix)