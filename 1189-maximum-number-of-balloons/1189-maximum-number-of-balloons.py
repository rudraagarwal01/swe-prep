# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         count = {}

#         for ch in text:
#             if ch in "ballon":
#                 count[ch] += 1
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # this counts the number of times each char in balloon that shows up
        b = text.count('b')
        a = text.count('a')
        l = text.count('l')
        o = text.count('o')
        n = text.count('n')

        # return the min of one of these char will tell how many times we can make balloon
        return min(b, a, l // 2, o // 2, n)
            

        
