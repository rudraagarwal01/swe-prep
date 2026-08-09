class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case for enpty list
        if not nums:
            return 0

        # total num of consecutive numbers
        max_count = 1

        # use to find all counts
        curr_count = 1

        sort = sorted(nums)
        n = len(sort)

        for i in range(1, n):
            # Ignore duplicates
            if sort[i] == sort[i - 1]:
                continue
            if sort[i] == sort[i - 1] + 1:
                curr_count += 1
            else:
                curr_count = 1
            
            max_count = max(max_count, curr_count)
        
        return max_count




