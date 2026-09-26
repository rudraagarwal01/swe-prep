from collections import defaultdict
class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)

        for arr in nums:
            for i in arr:
                counts[i] += 1
        

        ans = []
        n = len(nums)

        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)