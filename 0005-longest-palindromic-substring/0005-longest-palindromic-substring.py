class Solution:
    def longestPalindrome(self, s: str) -> str:
        # helper function
        def expand(left, right):
            # Expand outward while valid
            # the char are the same for left and right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return palindrome substring
            return s[left + 1:right]
        
        res = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd = expand(i, i)
            # Even-length palindrome
            even = expand(i, i + 1)

            # Pick the longer palindrome
            res = max(res, odd, even, key=len)
        
        return res
