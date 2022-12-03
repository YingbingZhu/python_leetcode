class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) / 2
        prev = []
        suff = []
        pre = suf = 0
        for i in range(1, n+1):
            pre += i
            prev.append(pre)
        for i in range(1, n+1):
            suf += (n +1- i)
            suff.append(suf)
        print(prev)
        print(suff)
        for i in range(n):
            if prev[i] == suff[::-1][i]:
                print(i+1)
                return i+1
        return -1


if __name__ == "__main__":
    s = Solution()
    s.pivotInteger(4)