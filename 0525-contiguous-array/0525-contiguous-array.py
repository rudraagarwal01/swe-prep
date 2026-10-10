class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}   # running total 0 "happened" before the array starts
        total = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                total += 1
            else:
                total -= 1

            if total in first_seen:
                ans = max(ans, i - first_seen[total])
            else:
                first_seen[total] = i

        return ans