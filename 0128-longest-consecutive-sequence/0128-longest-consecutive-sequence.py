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
        # 
        unique = set(nums)
        longest = 0
        
        for num in unique:
            # check if there is a number before curr num in set 
            if num - 1 in unique: 
                continue
            
            length = 1
            
            # keeps checking for consecutive
            while num + length in unique:
                length += 1

            longest = max(longest, length)

        return longest

# faster complexity
# O(n)




