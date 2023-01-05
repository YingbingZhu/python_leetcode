class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        res = 1
        curStart = points[-1][0]
        for start, end in reversed(points):
            if end < curStart:
                res += 1
                curStart = start
        return res



if __name__ == '__main__':
    points = [[10,16],[2,8],[1,6],[7,12]]
    Solution().findMinArrowShots(points)

