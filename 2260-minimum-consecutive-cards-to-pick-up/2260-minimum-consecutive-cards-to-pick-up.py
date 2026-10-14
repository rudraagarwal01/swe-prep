class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        seen = defaultdict(int)
        ans = 10**5 + 1

        for i, x in enumerate(cards):
            if x in seen:
                ans = min(ans, i - seen[x] + 1)
            seen[x] = i

        return ans if ans < 10**5 + 1 else -1

     
    