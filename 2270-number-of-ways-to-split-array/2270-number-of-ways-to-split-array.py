class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        prefix = [nums[0]]

        # this finds the prefix at each index
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        # cant split at the last index
        for i in range(len(nums) - 1):
            left_section = prefix[i]
            # prefix[-1] is the last element
            right_section = prefix[-1] - prefix[i]

            if left_section >= right_section:
                ans += 1
        return ans
            