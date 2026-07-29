class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lowest rate of eating a pile of bananas
        left = 1
        # maximum amount of time to eat the largest pile of bananas
        right = max(piles)

        while left < right:
            # find the time in the middle to see if that would work
            mid = (left + right) // 2

            # calculate the total hours it takes to eat the bananas at middle rate
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / mid)

            # if total hours is > given h then we need to increase the speed to greater than the middle
            if total_hours > h:
                left = mid + 1
            # Speed 'mid' works! It might be our answer, or we might be eating
            # faster than needed. Keep 'mid' as candidate and check slower speeds.
            else:
                right = mid
        return left
