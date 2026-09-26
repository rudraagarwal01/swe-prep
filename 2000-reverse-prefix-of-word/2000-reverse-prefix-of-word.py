class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        word = list(word)
        
        right = -1 
        for i in range(len(word)):
            if word[i] == ch:
                right = i
                break
    
            
        if right == -1: 
            return "".join(word)

        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        return "".join(word)
