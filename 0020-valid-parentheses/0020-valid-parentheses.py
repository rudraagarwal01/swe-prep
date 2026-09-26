class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:
            
                if not stack:
                    return False
                elt = stack.pop()
                if pairs[ch] != elt:
                    return False
            else:
                stack.append(ch)
        
        return not stack

