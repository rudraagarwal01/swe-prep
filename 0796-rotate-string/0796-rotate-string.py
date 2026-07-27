class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)
        # if goal is a substring of s + s then it is a valid rotation of s