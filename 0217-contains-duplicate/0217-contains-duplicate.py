class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set to ensure that there are no duplicates
        seen = set()

        for num in nums:
            if num in seen:
                return True
            # add current num to set
            seen.add(num)

        return False