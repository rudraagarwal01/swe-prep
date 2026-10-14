class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def get_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        seen = {}
        ans = -1

        for num in nums:
            digit_sum = get_sum(num)
            if digit_sum in seen:
                ans = max(ans, num + seen[digit_sum])
                seen[digit_sum] = max(num, seen[digit_sum])
            else:
                seen[digit_sum] = num
        
        return ans

