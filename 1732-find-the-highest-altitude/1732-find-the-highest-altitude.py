class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = 0

        for g in gain:
            # keep adding to the current altitude (negative number would decrease this)
            curr_alt += g
            # compares with the max alt each time and updates max alt 
            max_alt = max(max_alt, curr_alt)
        
        return max_alt
