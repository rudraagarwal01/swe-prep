class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        temp = 0

        # iterate through nums
        # add to temp if num is 1
        for num in nums:
            if num == 1:
                temp += 1
            # if temp is greater than max then update max
            else:
                if temp > max:
                    max = temp
                temp = 0
        # update max
        if temp > max:
            max = temp
            
        return max
                
        