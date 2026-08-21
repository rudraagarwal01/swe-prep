class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # target is found
            if nums[mid] == target:
                return mid
            
            # left half is sorted
            if nums[left] <= nums[mid]:
                # target is on the left side 
                if nums[left] <= target < nums[mid]:
                    # elimate right side
                    right = mid - 1
                else:
                    left = mid + 1

            # right side is sorted 
            else:
                # target is on the right side
                if nums[mid] < target <= nums[right]:
                    # elimate left side
                    left = mid + 1
                else: 
                    right = mid - 1
        return -1
        











