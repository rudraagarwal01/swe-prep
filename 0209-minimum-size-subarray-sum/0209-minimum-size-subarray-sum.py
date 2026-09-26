class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # min stores length
        min_len = len(nums) + 1
        left = 0
        curr = 0

        for right in range(len(nums)):
            # adds the numbers from the right
            curr += nums[right]

            while curr >= target:
                length = right - left + 1
                min_len = min(min_len, length)
                # removes the numbers from the left until curr drops below target
                curr -= nums[left]
                left += 1

        return min_len if min_len != len(nums) + 1 else 0
        