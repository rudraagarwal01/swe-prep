class Solution:
    def maxArea(self, height: List[int]) -> int:
        # how do i make it so that it multiplies with the shorter number 
        # can use max_area (max()) to store the greatest area

        # hint: one pointer at start and the other at the end
        # move the pointer that is pointing to the smaller number

        area = 0
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            length = right - left
            if height[left] < height[right]:
                area = height[left] * length
                left += 1
            elif height[left] > height[right]:
                area = height[right] * length
                right -= 1
            else:
                area = height[left] * length
                left += 1
                right -= 1

            max_area = max(max_area, area)

        return max_area
            