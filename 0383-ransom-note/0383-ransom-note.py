class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = defaultdict(int)
        for ch in magazine:
            counts[ch] += 1
        
        for letter in ransomNote:
            if counts[letter] == 0:
                return False
            counts[letter] -= 1
        return True