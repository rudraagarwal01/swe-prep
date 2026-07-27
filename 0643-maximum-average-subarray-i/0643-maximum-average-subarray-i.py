class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = 0
        total = 0

        # first window from the first index to the kth
        for i in range(k):
            total += nums[i]
            
        max_avg = total / k
            
        for i in range(k, n):
            total += nums[i] # adds to extended window on right side 
            total -= nums[i - k] #removes the first one (shortens the window)
        
            avg = total / k 
            max_avg = max(max_avg, avg) # compares and stores the larger one
        
        return max_avg