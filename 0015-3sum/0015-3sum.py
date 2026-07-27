class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # create a list to store different triplets
        res = []
        # sort nums to make it easier to ensure no duplicates
        sort = sorted(nums)

        # find the correct starting point (index i)
        for i in range(len(sort)):
            # index is positive and value is a duplicate then continue to prevent duplicate answers
            if i > 0 and sort[i] == sort[i - 1]:
                continue 
            
            # set indices for left and right pointer
            p1 = i + 1
            p2 = len(sort) - 1

            # two sum approach
            while p1 < p2:
                total = sort[i] + sort[p1] + sort[p2]

                if total < 0:
                    p1 += 1
                elif total > 0:
                    p2 -= 1
                # append onto result if total is 0
                # iterate p1/p2 to continue
                else:
                    res.append([sort[i], sort[p1], sort[p2]])
                    p1 += 1
                    p2 -= 1
                
                    # ensures that left pointer is not a duplicate
                    while p1 < p2 and sort[p1] == sort[p1 - 1]:
                        p1 += 1
        return res

        