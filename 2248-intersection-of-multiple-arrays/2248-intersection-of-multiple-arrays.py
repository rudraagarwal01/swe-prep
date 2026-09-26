from collections import defaultdict

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)

        for arr in nums:
            for i in arr:
                # add frequency of each number
                counts[i] += 1
        
        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)

