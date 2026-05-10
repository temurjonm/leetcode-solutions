class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        
        for source, destination, weight in edges:
            adj[source].append([destination, weight])

        minHeap = [[0, src]]
        shortest = {i: -1 for i in range(n)}  # Set all distances to -1 initially

        while minHeap:
            _weight, _destination = heapq.heappop(minHeap)

            # If destination has already been processed, skip it
            if shortest[_destination] != -1:
                continue

            # Record the shortest distance to this destination
            shortest[_destination] = _weight

            # Process each neighbor of the destination
            for neighboarDest, neighboarWeight in adj[_destination]:
                if shortest[neighboarDest] == -1:
                    # Push the new distance and neighbor into the min-heap
                    heapq.heappush(minHeap, [_weight + neighboarWeight, neighboarDest])


        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
                
        return shortest