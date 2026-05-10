'''
    [[1,3],[1,5],[6,7]]
            i

    [1,3]


'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastInterval = result[-1]

            if lastInterval[1] >= start:
                lastInterval[1] = max(lastInterval[1], end)
            else:
                result.append([start, end])

        return result