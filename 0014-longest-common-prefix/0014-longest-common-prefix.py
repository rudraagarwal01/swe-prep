class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        prefix = strs[0]

        for word in strs[1:]: #loop through the rest of the list minus first word
            while not word.startswith(prefix): #runs until there is a match
                prefix = prefix[:-1] #cutting down letters from the first word 
                if not prefix: 
                    return ""
                    
        return prefix
