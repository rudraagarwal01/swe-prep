class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # set automatically removes duplicates
        k = set(nums)
        output = []

        # in range from 1 to the end of list
        for i in range(1, len(nums) + 1):
            # iterates 1 -> end and adds the numbers to the output that are not found
            if i not in k:
                output.append(i)
        return output