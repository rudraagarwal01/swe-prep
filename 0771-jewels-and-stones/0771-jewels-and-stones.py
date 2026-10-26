class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # set of jewel types for O(1) lookups
        seen = set(jewels)
        count = 0

        for s in stones:
            if s in seen:
                count += 1
        return count