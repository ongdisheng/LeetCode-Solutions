class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Time: O(n log n)
        Space: O(1)
        """
        # sort by start time
        intervals.sort(key=lambda i: i[0])
        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # non-overlapping
            if start >= prev_end:
                prev_end = end
            
            # overlapping
            else:
                res += 1
                prev_end = min(end, prev_end)
        
        return res