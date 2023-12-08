class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def distance(p1, p2):
            return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))
        
        ans = 0
        for i in range(1, len(points)):
            ans += distance(points[i], points[i-1])
        
        return ans
        