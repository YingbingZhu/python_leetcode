# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
# when viewed from a distance.
# Given the locations and heights of all the buildings,
# return the skyline formed by these buildings collectively.
#
# The geometric information of each building is given in the array buildings
# where buildings[i] = [lefti, righti, heighti]:
#
# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded
# on an absolutely flat surface at height 0.
#
# The skyline should be represented as a list of "key points" sorted by their x-coordinate
# in the form [[x1,y1],[x2,y2],...].
# Each key point is the left endpoint of some horizontal segment in the skyline
# except the last point in the list,
# which always has a y-coordinate 0 and is used to mark the skyline's termination
# where the rightmost building ends.
# Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
#
# Note: There must be no consecutive horizontal lines of equal height in the output skyline.
# For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
# the three lines of height 5 should be merged into one in the final output as such:
# [...,[2 3],[4 5],[12 7],...]

import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = [(l, -h, r) for l, r, h in buildings]
        events += [(r, 0, None) for _, r, _ in buildings]
        events.sort()

        max_heap = [(0, float('inf'))]
        res = [[0, 0]]
        for l, h, r in events:

            if h != 0:
                heapq.heappush(max_heap, (h, r))

            # find higher height whose r > l
            while max_heap[0][1] <= l:
                heapq.heappop(max_heap)

            if res[-1][1] != -max_heap[0][0]:
                res.append([l, -max_heap[0][0]])
        return res[1:]

