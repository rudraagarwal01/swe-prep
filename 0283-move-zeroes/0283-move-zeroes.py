class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Two pointer approach
        # left and right are both indices
        # 'left' is our Write pointer
        left = 0
    
        # 'right' is our Read pointer, iterating through the array
        for right in range(len(nums)):
            # When we find a non-zero element...
            if nums[right] != 0:
                # Swap it with the element at the 'left' pointer
                nums[left], nums[right] = nums[right], nums[left]
            
                # Move the 'left' pointer forward
                left += 1

        return nums