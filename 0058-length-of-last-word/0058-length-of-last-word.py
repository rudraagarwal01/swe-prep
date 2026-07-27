class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        result = 0; 

        for i in range(len(string) -1, -1, -1):
            if string[i] != ' ': 
                result += 1
            else: 
                break

        return result
