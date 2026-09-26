class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # iterate backwards
        for i in range(len(digits) -1, -1, -1):
            # adds one to last index
            # then second last ...
            digits[i] += 1

            # if there is no carry over
            if digits[i] < 10:
                return digits 
            else: 
                digits[i] = 0
            
        return [1] + digits