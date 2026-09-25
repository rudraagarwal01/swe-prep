class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        curr = 0
        min_prefix = 0

        for num in nums:
            curr += num
            min_prefix = min(min_prefix, curr)

        return max(1, 1 - min_prefix)