from cmath import sqrt


class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        d = {}
        nums.sort()
        for num in nums:
            d[num] = 1
            if sqrt(num) in d:
                d[num] = d.get(num, 1) + d[sqrt(num)]
        print(d)

        return max(d.values()) if max(d.values()) > 1 else -1


if __name__ == "__main__":
    s = Solution()
    nums = [2,2]
    s.longestSquareStreak(nums)