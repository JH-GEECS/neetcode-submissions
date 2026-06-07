"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <= 1:
            return True

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for idx in range(len(intervals)-1):
            if sorted_intervals[idx].end > sorted_intervals[idx+1].start:
                return False

        return True