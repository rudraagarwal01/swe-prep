class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dict to store the freq
        # char -> freq
        count = {}
        left = 0
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            # 1. Expand the window by including s[right]
            # This basically gets the letter of the most frequency
            char = s[right]

            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            max_freq = max(max_freq, count[char])

            # 2. If replacements needed exceed k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                # remove from count
                count[s[left]] -= 1
                # shrink window
                left += 1

            # 3. Update the maximum valid window length
            max_len = max(max_len, right - left + 1)

        return max_len