class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        # must be distinct elements 
        # can't use sliding window
        count = defaultdict(int)
        curr = 0
        ans = 0

        # build first window
        for i in range(k):
            count[nums[i]] += 1
            curr += nums[i]

        if len(count) == k:
            ans = curr

        for i in range(k, len(nums)):
            # add new element
            count[nums[i]] += 1
            curr += nums[i]

            # remove leftmost element of previous window
            left = nums[i - k]
            count[left] -= 1
            curr -= left
            if count[left] == 0:
                del count[left]

            # only a candidate if all k elements are distinct
            if len(count) == k:
                ans = max(ans, curr)

        return ans