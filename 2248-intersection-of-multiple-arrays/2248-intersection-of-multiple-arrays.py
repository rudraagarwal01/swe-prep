from collections import defaultdict

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)

        # for each array in nums (2D)
        for arr in nums:
            # for each i in each array
            for i in arr:
                # add frequency of each number
                counts[i] += 1
        
        n = len(nums)
        ans = []
        # checks if freqency is equal to number of arrays
        for key in counts:
            # if equal then add key
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)

