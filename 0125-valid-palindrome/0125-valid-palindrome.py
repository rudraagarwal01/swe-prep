class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        # compare each value and iterate pointer
        left = 0
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        right = len(clean_s) - 1

        while left < right:
            if clean_s[left] == clean_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True