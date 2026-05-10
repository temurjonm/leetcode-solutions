'''
    [1,2,2,3,3,3], k = 2
    {1:1, 2:2, 3:3}
                i    
    max heap 
    topk = [
        2,
        3
    ]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [num for freq, num in heap]






