class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)  # strings are immutable, need a list for in-place swaps
        left, right = 0, len(s) - 1

        while left < right:
            # skip left pointer forward if it's not sitting on a letter
            if not s[left].isalpha():
                left += 1
                continue

            # skip right pointer backward if it's not sitting on a letter
            if not s[right].isalpha():
                right -= 1
                continue

            # both are letters — swap them, then move both pointers inward
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)