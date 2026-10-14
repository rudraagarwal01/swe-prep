class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        seen = defaultdict(int)
        ans = 10**5 + 1

        # x -> card
        # i -> index
        for i, x in enumerate(cards):
            if x in seen:
                # curr index - index of last seen + 1
                ans = min(ans, i - seen[x] + 1)
            # else map card to curr index
            seen[x] = i

        return ans if ans < 10**5 + 1 else -1

     
    