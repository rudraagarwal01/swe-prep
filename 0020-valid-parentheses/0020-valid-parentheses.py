class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # create a dict to match each type of bracket
        # key is close, value is open
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If the char is a closing bracket
            # only checks the keys
            if char in pairs:
                # check if stack exists
                if stack:
                    element = stack.pop()
                else:
                    element = ''
                # if the top element is not equal to the value in pairs
                # pairs[char] is value
                if pairs[char] != element:
                    return False
            # char is opening bracket to add it to stack 
            else:
                stack.append(char)
        return not stack

    
    

            
        


                