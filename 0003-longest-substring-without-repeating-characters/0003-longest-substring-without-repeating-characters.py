class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # prevents dupicates
        seen = set()
        left = 0
        max_len = 0

        # iterate with right to keep expanding window
        for right in range(len(s)):
            # if right is already in seen then shrink from left
            # shrink until duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # if right is new then add it to set
            seen.add(s[right])
            length = right - left + 1
            max_len = max(length, max_len)
        
        return max_len

        

