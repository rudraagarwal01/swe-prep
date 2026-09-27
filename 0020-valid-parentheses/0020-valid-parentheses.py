class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:
                if stack:
                    elt = stack.pop()
                else:
                    elt = ''
                if pairs[ch] != elt:
                    return False
            else:
                stack.append(ch)
        
        return not stack

            

                    
            