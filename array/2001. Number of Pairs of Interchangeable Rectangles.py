class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        d = {}
        for w, h in rectangles:
            val = float(w) / float(h)
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
        res = 0
        for v in d.values():
            if v >= 2:
                res += v * (v - 1) / 2
        return res

