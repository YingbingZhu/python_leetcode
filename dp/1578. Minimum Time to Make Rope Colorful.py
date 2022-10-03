# Alice has n balloons arranged on a rope.
# You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
#
# Alice wants the rope to be colorful.
# She does not want two consecutive balloons to be of the same color,
# so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful.
# You are given a 0-indexed integer array neededTime
# where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
#
# Return the minimum time Bob needs to make the rope colorful.
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total = 0
        curr_max = 0
        for i in range(len(colors)):
            # each group first = 0
            if i > 0 and colors[i] != colors[i-1]:
                curr_max = 0
            total += min(neededTime[i], curr_max)
            curr_max = max(curr_max, neededTime[i])
        return total
