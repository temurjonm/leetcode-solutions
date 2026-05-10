'''
[[1,2],[2,4],[1,4]] => 1 sorted => [[1,2],[1,4],[2,4]]
2 > 1
    count = 1
else:


[[1,2],[2,4]] => 0
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        prevEnd = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end, prevEnd)

        return count