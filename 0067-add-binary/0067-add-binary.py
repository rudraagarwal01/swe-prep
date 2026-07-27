class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            bit1 = int(a[i]) if i >= 0 else 0   # checks for negative 
            bit2 = int(b[j]) if j >= 0 else 0   # checks for negative 

            total = bit1 + bit2 + carry     # prints 0, 1, 2, or 3
            result.append(str(total % 2))   # allows us to get the current binary number
            carry = total // 2              

            i -= 1
            j -= 1
        
        return "".join(result[::-1])