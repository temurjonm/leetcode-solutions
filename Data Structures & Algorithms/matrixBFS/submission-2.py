class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        def validate(r,c):
            return not (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1)

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    nr, nc = dr + r, dc+c
                    
                    if validate(nr, nc):
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            length += 1
        return -1