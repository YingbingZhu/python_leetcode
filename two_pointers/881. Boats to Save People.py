#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/23
"""
# You are given an array people where people[i] is the weight of the ith person,
# and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            if people[r] + people[l] > limit:
                count += 1
                r -= 1
            else:
                count += 1
                l += 1
                r -= 1
        return count