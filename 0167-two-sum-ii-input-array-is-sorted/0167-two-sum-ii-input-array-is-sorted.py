class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create two pointers one starting at the front and one at the end
        p1 = 0
        p2 = len(numbers) - 1

        # ensure that pointers don't cross
        # can't have two same values either
        while p1 < p2:
            # add the values at curr pointers
            total = numbers[p1] + numbers[p2]
            # move left pointer if total < target
            if total < target:
                p1 += 1
            # move right pointer if total > target
            elif total > target:
                p2 -= 1 
            # return indices with +1 because it is using 1-indexed output 
            else:
                return [p1 + 1, p2 + 1]
