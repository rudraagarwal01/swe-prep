class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # arrays cannot be stored as keys because they are immutable

        row_counts = defaultdict(int)
        for row in grid:
            # store row in map (freq to 1)
            row_counts[tuple(row)] += 1
        
        ans = 0
        # zip(*grid) gives each column as a tuple
        for col in zip(*grid):
            # zip(*grid) returns a tuple so use that to 
            ans += row_counts[col]

        return ans



