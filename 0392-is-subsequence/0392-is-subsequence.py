class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for char in t:
            # i cannot be bigger than s (string) and checking if char is in both strings
            if i < len(s) and char == s[i]: 
                i += 1
            
        # if i is equal to length of s then it will return true
        return i == len(s)