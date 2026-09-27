class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
# Trace: s = "leetcode", wordDict = ["leet","code"] (n=8)
# dp[0] = True
# i=1..3: no j gives a valid word ("l","le","lee" aren't in the dict) → all False
# i=4: j=0, dp[0]=True, s[0:4]="leet" ∈ word_set → dp[4]=True
# i=5,6,7: check various j, nothing matches (no valid word ends here) → False
# i=8: j=4, dp[4]=True, s[4:8]="code" ∈ word_set → dp[8]=True
                if dp[j] and s[j:i] in word:
                    dp[i] = True
                    break
        return dp[n]