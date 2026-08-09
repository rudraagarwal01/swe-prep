# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # edge case for enpty list
#         if not nums:
#             return 0

#         # total num of consecutive numbers
#         max_count = 1

#         # use to find all counts
#         curr_count = 1

#         sort = sorted(nums)
#         n = len(sort)

#         for i in range(1, n):
#             # Ignore duplicates
#             if sort[i] == sort[i - 1]:
#                 continue
#             if sort[i] == sort[i - 1] + 1:
#                 curr_count += 1
#             else:
#                 curr_count = 1
            
#             max_count = max(max_count, curr_count)
        
#         return max_count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to remove duplicates
        # this does NOT sort the nums
        unique = set(nums)
        max_count = 0
        
        for num in unique:
            # ensure that current num is the start of the sequence
            # let's say are looking at 3 if there is 2 in the set it'll continue 
            if num - 1 in unique: 
                continue
            
            curr_count = 1

            # keeps checking for consecutive
            while num + curr_count in unique:
                curr_count += 1

            max_count = max(max_count, curr_count)

        return max_count

# faster complexity
# O(n)




