class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # start with the result array filled with 1s
        
        n = len(nums)
        ans = [1] * n

        # store all numbers in ans before the current num
        prefix = 1
        for i in range(n):
            # store the prefix
            ans[i] = prefix
            # multiply it but the current number and store it in the next iteration 
            prefix *= nums[i]

        # At this point, for nums = [1, 2, 3, 4]:
        # result is now [1, 1, 2, 6] (the product of all numbers to the left of each index)

        suffix = 1
        # go backwards
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix 
            suffix *= nums[i]
        
        return ans

            

