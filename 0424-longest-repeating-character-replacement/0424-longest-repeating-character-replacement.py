class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            # 1. Expand the window by including s[right]
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # 2. If replacements needed exceed k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # 3. Update the maximum valid window length
            max_len = max(max_len, right - left + 1)

        return max_len