class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            squarePts = (x ** 2) + (y**2) 
            heap.append((squarePts, x, y))

        heapq.heapify(heap)
        result = []
        for _ in range(k):
            _, x,y = heapq.heappop(heap)
            result.append((x,y))
        
        return result