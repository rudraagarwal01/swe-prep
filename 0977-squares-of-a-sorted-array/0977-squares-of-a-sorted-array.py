class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # output array
        result = []

        # first square all the nums then sort them
        for num in nums:
            result.append(num * num)
        return sorted(result)