class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # doesn't store duplicates
        seen = set()
        alpha = 26

        for s in sentence:
            if s not in seen:
                seen.add(s)
        
        if len(seen) == alpha:
            return True
        else: 
            return False
