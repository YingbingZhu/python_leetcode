class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for v in intervals:
            if v[1] < newInterval[0]:
                res.append(v)
            elif newInterval[1] < v[0]:
                res.append(newInterval)
                newInterval = v
            else:
                newInterval[0] = min(v[0], newInterval[0])
                newInterval[1] = max(v[1], newInterval[1])
        res.append(newInterval)
        return res
                
