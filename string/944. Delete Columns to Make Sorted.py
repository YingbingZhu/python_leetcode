class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs[0])
        res = 0
        for i in range(n):
            length = len(strs)
            for j in range(1, length):
                if strs[j][i] < strs[j - 1][i]:
                    res += 1
                    break

        return res


if __name__ == '__main__':
    strs = ["abc", "bce", "cae"]
    Solution().minDeletionSize(strs)