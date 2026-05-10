'''
[[1,3],[1,5],[6,7]] => [[1,5],[6,7]]


[[1,2],[2,3]]
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]] #[1,3]

        for interval in intervals[1:]: # [1,5]
            start, end = interval
            lastInterval = result[-1] # [3]

            if lastInterval[1] >= start: # 3 > 1
                lastInterval[1] = max(lastInterval[1], end) # 5
            else:
                result.append([start, end])

        return result