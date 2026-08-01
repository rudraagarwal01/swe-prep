class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both strings and compare them
        if sorted(s) == sorted(t): 
            return True
        return False
# O(n log n)





