class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        sort = sorted(nums)
        
        for i in range(len(sort)):
            # Fix 1: Check against the previous element
            if i > 0 and sort[i] == sort[i - 1]:
                continue
            
            p1 = i + 1
            p2 = len(sort) - 1

            while p1 < p2:
                total = sort[i] + sort[p1] + sort[p2]
                
                if total < 0:
                    p1 += 1
                elif total > 0:
                    p2 -= 1
                else:
                    # Fix 2: Typo fixed and brackets added
                    res.append([sort[i], sort[p1], sort[p2]])
                    
                    # Fix 3: Indented these so they only trigger on a match
                    p1 += 1
                    p2 -= 1

                    while p1 < p2 and sort[p1] == sort[p1 - 1]:
                        p1 += 1
                        
        return res