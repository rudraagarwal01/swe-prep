class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lowest amount of time to eat a pile is one hour
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
            # if total hours is <= given h then that might be correct speed or too slow
            # continue to check the slower rate by updating the right index
            else:
                right = mid
        return left
