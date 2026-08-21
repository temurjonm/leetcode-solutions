class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base cases
        if not grid: 
            return 0

        rows, cols = len(grid), len(grid[0])
        number_of_island = 0

        # algorithms
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # traversal
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    number_of_island += 1
                    dfs(r,c)

        return number_of_island