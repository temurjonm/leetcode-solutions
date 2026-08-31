class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 - empty
        # 1 - fresh 
        # 2 - rotten
        '''
            [[1,1,0]
             [0,1,1],
             [0,1,2]
             ]

             queue = deque((2,2), (2,1),(1,2) )
        '''

        # add rotten to queue
        # start from rotten and check the neighboars if fresh => rotten add rotten to queue

        fresh = 0
        total = 0
        queue = deque()

        rows, cols = len(grid), len(grid[0])
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                (r, c) = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            total += 1

        return total if fresh == 0 else -1