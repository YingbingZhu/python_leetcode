class Solution(object):
    def __init__(self):
        self.res = 0

    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def dfs(index, curr):
            if index == len(nums):
                return
            if curr % 5 == 0:
                self.res += 1
            dfs(index + 1, curr + nums[index])

        for i in range(len(nums)):
            dfs(i, 0)
            print(self.res)
        return self.res


if __name__ == "__main__":
    s = Solution()
    s.subarraysDivByK([4,5,0,-2,-3,1],5)