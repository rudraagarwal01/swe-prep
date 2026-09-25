class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)  # strings are immutable, convert to list for in-place swaps
        n = len(s)
        left = 0

        for right in range(n + 1):  # +1 so we catch the last word too
            # word boundary: either a space, or the end of the string
            if right == n or s[right] == " ":
                # reverse s[left..right-1] in place
                lo, hi = left, right - 1
                while lo < hi:
                    s[lo], s[hi] = s[hi], s[lo]
                    lo += 1
                    hi -= 1
                left = right + 1  # move left past the space, to start of next word

        return "".join(s)