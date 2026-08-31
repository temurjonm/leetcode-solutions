class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid),len(grid[0])
        queue = deque()
        fresh = 0
        total = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            total += 1
            for _ in range(len(queue)):
                (r,c) = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
        return total if fresh == 0 else -1
