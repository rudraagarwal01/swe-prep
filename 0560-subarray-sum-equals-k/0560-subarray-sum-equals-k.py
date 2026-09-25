class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # can't use sliding window because there are negative numbers
        # not monotonic
        count = defaultdict(int)
        count[0] = 1  # empty prefix
        curr = 0
        ans = 0

        for num in nums:
            curr += num
            # checks if a previous sum has added to curr - k
            ans += count[curr - k]
            count[curr] += 1

        return ans