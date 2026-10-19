"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        sort = sorted(intervals, key=lambda inter: inter.start)
        for i in range(n):
            currs = sort[i].start
            curre = sort[i].end
            for j in range(i + 1, n):
                if sort[j].start < curre:
                    return False
        return True