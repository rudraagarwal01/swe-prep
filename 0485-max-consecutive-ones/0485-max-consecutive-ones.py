class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        length = 0
  

        for right in range(len(nums)):
            if nums[right] == 1:
                length += 1
            else:
                length = 0
            
            max_len = max(max_len, length)
        
        return max_len