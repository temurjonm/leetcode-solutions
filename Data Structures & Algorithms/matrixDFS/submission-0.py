class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def helper(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c]== 1 or (r,c) in visited:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1
                
            visited.add((r,c))

            count = 0

            for dr,dc in [(0,1),(1,0),(0,-1), (-1,0)]:
                count += helper(dr+r, dc+c)
            visited.remove((r,c))
            return count

        return helper(0,0)