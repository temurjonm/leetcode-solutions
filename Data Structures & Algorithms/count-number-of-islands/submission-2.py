class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # handle base cases
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        number_of_islands = 0

        # explore island and find if more islands
        def explore(r,c):
            # handle outbound 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return 
            # mark visited
            grid[r][c] = '0'
            # explore neighbors 
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c + 1)
            explore(r, c - 1)
        # iterate over grid and find islands 
            # handle cases if land and not visted
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    number_of_islands += 1
                    explore(r, c)

        return number_of_islands
        



