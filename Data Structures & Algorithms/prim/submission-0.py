class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        adj = {i: [] for i in range(n)}

        for n1, n2, weight in edges:
            adj[n1].append((n2, weight))
            adj[n2].append((n1, weight))

        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while minHeap and len(visited) < n:
            weight, vertex = heapq.heappop(minHeap)

            if vertex in visited:
                continue

            res += weight
            visited.add(vertex) 

            for neighbor, edge_weight in adj[vertex]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (edge_weight, neighbor))

        return res if len(visited) == n else -1