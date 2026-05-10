'''
[[1,3],[1,5],[6,7]]

'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            lastInterval = merged[-1]

            if start <= lastInterval[1]:
                lastInterval[1] = max(lastInterval[1], end)
            else:
                merged.append([start, end])

        return merged