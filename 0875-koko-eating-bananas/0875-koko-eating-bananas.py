class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # least hours to finish one pile
        left = 1
        # find the time it takes her to eat the pile with the most bananas
        # so if hours are 11 it would take 11 bananas/hr highest time
        right = max(piles)

        while left < right: 
            # (1 + 11) // = 6
            mid = (left + right) // 2
            
            # calculate the total hours it would take to eat at the mid rate
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / mid)
            
            if total_hours > h:
                left = mid + 1
            # if mid speed is correct then try to find speed lower 
            # doing right = mid - 1 could force it to find a speed lower, when mid is the right speed
            else:
                right = mid
        return left

            