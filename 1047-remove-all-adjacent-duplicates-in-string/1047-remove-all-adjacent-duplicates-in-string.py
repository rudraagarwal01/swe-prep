class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # holds the characters that survive so far

        for ch in s:
            # if the top matches the current char, they cancel each other out
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)