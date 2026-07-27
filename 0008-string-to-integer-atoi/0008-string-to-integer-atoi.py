class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            # helps place in the right place 
            num = num * 10 + int(s[i])
            i += 1

        num *= sign    
        return max(-2**31, min(2**31 - 1, num))