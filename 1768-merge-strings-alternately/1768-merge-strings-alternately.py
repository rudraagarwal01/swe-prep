class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create output string
        # go through both strings and add a letter from each string until both strings are done
        result = ""
        i = 0

        # runs until there are still chars in one of the words
        while i < len(word1) or i < len(word2):
            # add each one alternatively
            if i < len(word1):
                result += word1[i] # adds char from correct index (word1)
            if i < len(word2):
                result += word2[i] # adds char from correct index (word2)
            # iterates
            i += 1

        return result