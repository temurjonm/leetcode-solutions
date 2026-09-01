class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = deque([(0, 0, 1)])

        grid[0][0] = 1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1),  (1, 0),   (1, 1)
        ]

        while queue:
            for _ in range(len(queue)):
                row, col, path = queue.popleft()

                if row == rows-1 and col == cols - 1:
                    return path

                for dr, dc in directions:
                    nr, nc = dr+row, dc+col

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc, path+1))


        return -1
