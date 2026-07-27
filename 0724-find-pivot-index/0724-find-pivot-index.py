class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums) # gives the total sum of the array

        for i in range(len(nums)):
            # this basically compares the right and left side 
            # does not count the index itself 
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        
        return -1
            
           
