from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        freq = counts.values()
        # if all freq are the same then it will be one element in set
        # if there are freq of 1, 2 then this condition will fail
        # set keeps only unique elements
        return len(set(freq)) == 1  

