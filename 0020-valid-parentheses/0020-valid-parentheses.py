class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s: 
            # char is a closing bracket
            if char in pairs:
                if stack:
                    element = stack.pop()
                else:
                    element = ''
                # comapre closing bracket (value) with closing brackets on the stack
                if pairs[char] != element:
                    return False
            else:
                stack.append(char)
        return not stack