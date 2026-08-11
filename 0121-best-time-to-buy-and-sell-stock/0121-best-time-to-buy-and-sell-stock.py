class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Cannot do sort because the indices are basically days 
        # and we cannot sell on a day before it is bought

        # Use sliding window to find the difference each time
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            # if profit 
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # if right finds a lower price then move the left pointer there
                left = right
            right += 1

        return max_profit


            


