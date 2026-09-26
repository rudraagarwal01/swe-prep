class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # create a dict to match each type of bracket
        # key is close, value is open
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in pairs:
                if stack:
                    elt = stack.pop()
                else:
                    elt = ''
                
                if elt != pairs[ch]:
                    return False
            
            else:
                stack.append(ch)
        
        return not stack