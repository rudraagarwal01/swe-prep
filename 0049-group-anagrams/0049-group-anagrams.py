class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dict to store different groups of letters
        seen = {}

        # use sorted to store the keys and ensure that the words are grouping with the right key
        for word in strs:
            key = "".join(sorted(word))

            # if the key is in seen then append it to curr key
            if key in seen:
                seen[key].append(word)
            # else create a new key and add the curr word
            else:
                seen[key] = [word]
                
        # return the dict as a list
        return list(seen.values())
