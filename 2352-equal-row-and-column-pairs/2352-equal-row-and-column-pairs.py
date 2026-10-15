class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counts = defaultdict(int)

        for row in grid:
            row_counts[tuple(row)] += 1
        
        ans = 0
        for col in zip(*grid):
            ans += row_counts[col]
        return ans



