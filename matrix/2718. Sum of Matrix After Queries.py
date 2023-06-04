class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        queries.reverse()
        res = 0
        # seen number
        mpr = set()
        mpc = set()
        # painted row and col
        rsum = 0
        csum = 0

        for q in queries:
            if q[0] == 0:
                if q[1] not in mpr:
                    rsum += 1
                    mpr.add(q[1])
                    res += q[2] * (n - csum)
            else:
                if q[1] not in mpc:
                    csum += 1
                    mpc.add(q[1])
                    res += q[2] * (n - rsum)
        return res

