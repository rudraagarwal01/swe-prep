class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # dont need to track indices
        seen = set()

        for ch in s:
            if ch in seen:
                return ch
            else:
                seen.add(ch)

