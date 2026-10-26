class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter subtraction keeps only letters where the note needs MORE than the magazine has
        # if nothing is left over, the magazine covers the whole note
        return not (Counter(ransomNote) - Counter(magazine))



        # counts = defaultdict(int)
        # for ch in magazine:
        #     counts[ch] += 1
        
        # for letter in ransomNote:
        #     if counts[letter] == 0:
        #         return False
        #     counts[letter] -= 1
        # return True