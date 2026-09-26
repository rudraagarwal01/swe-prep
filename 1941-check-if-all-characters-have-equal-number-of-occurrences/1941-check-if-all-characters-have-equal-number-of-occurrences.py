from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        freq = counts.values()
        # if all freq are the same then it will be one element in set
        # if there are freq or 1, 2 then two elements and this condition will fail
        return len(set(freq)) == 1  

