from collections import Counter


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        counter = Counter(arr)
        counter = sorted(counter.items(), key=lambda x: x[1])
        res = len(counter)
        for i in range(len(counter)):
            v = counter[i][1]
            if k - v < 0:
                break
            else:
                k -= v
                res -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findLeastNumOfUniqueInts([5, 5, 4], 1))
