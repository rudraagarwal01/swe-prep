class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        # helper function to get the sum of the digits
        def get_sum(num):
            total = 0
            while num:
                # isolates each digit
                total += num % 10
                num //= 10
            return total

        
        seen = {}
        # no pair found yet
        ans = -1

        for num in nums:
            # calls the helper to get the sum of digits
            digit_sum = get_sum(num)

            if digit_sum in seen:
                # add curr number plus other number that matches sum of digits
                ans = max(ans, num + seen[digit_sum])
                # keep only the larger number for future pairs
                seen[digit_sum] = max(seen[digit_sum], num)
            else:
                seen[digit_sum] = num
        
        return ans
        
