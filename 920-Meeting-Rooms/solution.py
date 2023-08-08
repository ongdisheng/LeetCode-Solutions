"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        """
        Time: O(n log n)
        Space: O(1)
        """
        # Write your code here
        # edge case 
        if not intervals:
            return True

        # sort by start time
        intervals.sort(key=lambda i: i.start)
        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            # retrieve start and end time
            start, end = intervals[i].start, intervals[i].end

            # overlapping
            if start < prev_end:
                return False
            
            # update previous end time
            prev_end = max(end, prev_end)
        
        return True