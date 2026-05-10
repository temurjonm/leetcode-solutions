class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        result = []

        for x, y in points:
            sqtr_point = ((x - 0) ** 2) + (y-0)**2
            heapq.heappush(heap, (-sqtr_point, [x,y]))

            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            _, point = heapq.heappop(heap)
            result.append(point)

        return result
