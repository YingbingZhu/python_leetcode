from collections import Counter


class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        print(price)
        diff = []
        for i in range(1, len(price)):
            diff.append(price[i] - price[i-1])
        print(diff)


if __name__ == "__main__":
    price = [13,5,1,8,21,2]
    k = 3
    Solution().maximumTastiness(price, k)