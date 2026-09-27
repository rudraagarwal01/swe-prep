class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

#         # sort both strings and compare them
#         if sorted(s) == sorted(t):
#             return True
#         return False
# # O(n log n)







