class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time: O(n log n)
        Space: O(n)
        """
        # sort by start time
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            # retrieve prev end time
            prev_end = res[-1][1]

            # overlapping
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            
            # non-overlapping
            else:
                res.append([start, end])
        
        return res