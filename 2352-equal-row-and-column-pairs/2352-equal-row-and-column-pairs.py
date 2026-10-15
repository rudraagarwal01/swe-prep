class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # arrays cannot be stored as keys because they are immutable
        def convert_to_key(arr):
            return tuple(arr)


        row_counts = defaultdict(int)
        for row in grid:
            # store row in map (freq to 1)
            row_counts[convert_to_key(row)] += 1
        
        ans = 0
        # zip(*grid) gives each column as a tuple
        for col in zip(*grid):
            # every matching row forms one valid (row, col) pair with this column
            ans += row_counts[col]

        return ans


