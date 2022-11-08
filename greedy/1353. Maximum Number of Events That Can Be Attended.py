#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/4
"""
from heapq import heappush, heappop


# You are given an array of events where events[i] = [startDayi, endDayi].
# Every event i starts at startDayi and ends at endDayi.
#
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
#
# Return the maximum number of events you can attend.

# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # sort the event by start time
        events.sort(key=lambda i: i[0])
        print(events)
        i = 0
        n = len(events) - 1
        pq = []
        d = 0
        res = 0
        while i < n or pq:
            if not pq:
                d = events[i][0]
            while i < n and events[i][0] <= d:
                heappush(pq, events[i][1])
                i += 1
            # attend the soonest event
            heappop(pq)
            res += 1
            d += 1
            # remove event that are closed
            while pq and pq[0] < d:
                heappop(pq)
        return res


if __name__ == "__main__":
    s = Solution()







if __name__ == "__main__":
    s = Solution()
    events = [[1, 2], [2, 3], [3, 4]]
    s.maxEvents(events)


