class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create dictionary to store most freq
        count = {}
        left = 0
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            
            if char in count:
                # add to key
                count[char] += 1
            else:
                count[char] = 1
            
            max_freq = max(max_freq, count[char])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, (right - left + 1))
        return max_len
        