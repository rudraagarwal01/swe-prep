class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # a list of length amount + 1, where every single element is initialized to the value amount + 1
        dp = [amount + 1] * (amount + 1)


        # zero total would require zero coins
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1


