class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for source, destination, weight in edges:
            adj[source].append([destination, weight])

        minHeap = [[0, src]]
        shortest = {}

        while minHeap:
            _weight, _destination = heapq.heappop(minHeap)
            if _destination in shortest:
                continue

            shortest[_destination] = _weight

            for neighboarDest, neighboarWeight in adj[_destination]:
                if neighboarDest not in shortest:
                    heapq.heappush(minHeap, [_weight + neighboarWeight, neighboarDest])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
            