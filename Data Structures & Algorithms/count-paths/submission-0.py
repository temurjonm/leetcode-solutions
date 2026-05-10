class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)] 

        rows, cols = len(grid), len(grid[0])

        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] = grid[r][c-1] + grid[r-1][c]
        
        return grid[-1][-1]
