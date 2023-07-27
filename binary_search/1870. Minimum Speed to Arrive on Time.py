class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        left = 1
        right = 10 ** 7
        min_speed = -1
        while left <= right:
            mid = (left + right) // 2
            if self.computeTime(mid, dist, hour):
                right = mid - 1
                min_speed = mid
            else:
                left  = mid + 1
        return min_speed



    def computeTime(self, speed, dist, hour):
        res = 0
        for i in range(len(dist)):
            if i!= len(dist)-1:
                # * 1.0 to make it double, otherwise got int
                res += math.ceil(dist[i] * 1.0/ speed)
            else:
                res += dist[i] * 1.0 / speed
            if res > hour:
                return False
        return res <= hour
        