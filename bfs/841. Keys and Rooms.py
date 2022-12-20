#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/20
"""
from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = set([0])
        queue = deque(rooms[0])
        while queue:
            for _ in range(len(queue)):
                key = queue.popleft()
                seen.add(key)
                for room in rooms[key]:
                    if room not in seen:
                        seen.add(room)
                        queue += rooms[room]
        return len(seen) == len(rooms)


if __name__ == "__main__":
    Solution().canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]])
