class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not grid:
            return grid
        
        original_color = grid[sr][sc]

        if original_color == color:
            return grid

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != original_color:
                return 

            grid[r][c] = color

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        dfs(sr, sc)

        return grid