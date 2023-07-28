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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        """
        Time: O(n log n)
        Space: O(n)
        """
        # Write your code here
        # retrieve sorted start and end time
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # initialize variables 
        res, count = 0, 0
        idx_s, idx_e = 0, 0

        while idx_s < len(intervals):
            # a meeting starts
            if start[idx_s] < end[idx_e]:
                count += 1
                idx_s += 1
            
            # a meeting ends
            else:
                count -= 1
                idx_e += 1
            
            # update result
            res = max(res, count)
        
        return res