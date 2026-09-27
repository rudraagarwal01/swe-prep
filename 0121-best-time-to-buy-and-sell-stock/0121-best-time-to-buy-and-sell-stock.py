class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Cannot do sort because the indices are basically days 
        # and we cannot sell on a day before it is bought

        # Use sliding window to find the difference each time
        max_profit = 0
        n = len(prices)
        left = 0
        right = 1

        while right < n:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit



            


