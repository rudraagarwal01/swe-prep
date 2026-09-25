class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # output array
        res = []

        for num in nums:
            res.append(num * num)
        return sorted(res)