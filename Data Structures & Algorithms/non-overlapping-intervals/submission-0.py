class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        non_overlap = float('-inf')
        count = 0

        for start, end in intervals:
            if start >= non_overlap:
                non_overlap = end
            else:
                count += 1
        return count