class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islandsCount = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or (r,c) in visited:
                return

            visited.add((r,c))

            for dr,dc in [(0,1),(1,0),(0,-1), (-1,0)]:
                dfs(dr+r, dc+c)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islandsCount += 1

        return islandsCount