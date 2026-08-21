class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # base cases check if grid not empt
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        # dfs over grid, check if gird = 1, count lands
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            current_area = 1
            for dr, dc in directions:
                current_area += dfs(dr+r, dc+c)

            return current_area

        # iterate over rows/cols keep max 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                   max_area = max(max_area, dfs(r,c)) 

        return max_area