class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_count = 1
        curr_count = 1

        sort = sorted(nums)
        n = len(sort)

        for i in range(1, n):
            # check for duplicate
            if sort[i] == sort[i - 1]:
                continue
            if sort[i] == sort[i - 1] + 1:
                curr_count += 1
            else:
                curr_count = 1

            max_count = max(max_count, curr_count)
        
        return max_count 
                