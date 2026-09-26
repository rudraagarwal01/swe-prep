class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()

        # option A: three largest numbers (rightmost three after sorting)
        option_a = nums[-1] * nums[-2] * nums[-3]

        # option B: two smallest (most negative) numbers + the single largest
        option_b = nums[0] * nums[1] * nums[-1]

        return max(option_a, option_b)