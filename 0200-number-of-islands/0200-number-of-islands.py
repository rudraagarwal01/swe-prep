class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # base case: out of bounds, or not land (water or already visited)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return

            # mark this cell as visited by sinking it
            grid[r][c] = '0'

            # explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1   # new island found
                    dfs(r, c)    # sink the entire island

        return count