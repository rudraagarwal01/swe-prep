class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0

        # add all the numbers in first window
        for i in range(k):
            curr += nums[i]

        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]

            ans = max(ans, curr)

        return ans / k

