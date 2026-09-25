class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        # default every index to -1; this handles the "not enough elements
        # on one side" case automatically, no need for an explicit check later
        avgs = [-1] * n

        # prefix[i] = sum of nums[0..i-1] (offset by one, so prefix[0] = 0
        # represents the "empty" prefix before any elements are added)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(n):
            # only compute an average if there are at least k elements
            # on BOTH sides of i (a full window can be centered here)
            if i - k >= 0 and i + k <= n - 1:
                # sum of nums[i-k .. i+k] using the prefix array:
                # prefix[i+k+1] = sum of nums[0 .. i+k]
                # prefix[i-k]   = sum of nums[0 .. i-k-1]
                # subtracting removes everything before the window,
                # leaving just the window's sum
                window_sum = prefix[i + k + 1] - prefix[i - k]

                # window size is always 2k+1 elements (k on each side, plus i itself)
                avgs[i] = window_sum // (2 * k + 1)

        return avgs