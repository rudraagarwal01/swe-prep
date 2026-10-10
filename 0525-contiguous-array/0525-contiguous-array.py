class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Maps a running total to the FIRST index where that total appeared.
        # Starting with {0: -1} means "before the array starts (index -1),
        # the total was 0". This handles subarrays that begin at index 0.
        # {index: count}
        first_seen = {0: -1}

        # Running total: +1 for every 1, -1 for every 0
        total = 0

        # Length of the longest balanced subarray found so far
        ans = 0

        for i in range(len(nums)):
            # Update the running total based on the current number
            if nums[i] == 1:
                total += 1
            else:
                total -= 1

            if total in first_seen:
                # We've seen this total before, so the stretch between that
                # earlier index and now adds up to 0 (equal 0s and 1s).
                # Its length is the current index minus the earlier index.
                ans = max(ans, i - first_seen[total])
            else:
                # First time seeing this total, so remember where it happened.
                # We never overwrite it, because an earlier start gives a
                # longer subarray.
                first_seen[total] = i

        # Longest balanced subarray (0 if none exists)
        return ans