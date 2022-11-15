class Solution(object):

    def __init__(self):
        self.count = 0

    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1 and k % nums[0] == 0:
            return 1

        def dfs(index):
            if index == len(nums) \
                    or (index == len(nums)-1 and k % nums[index] != 0)\
                    or nums[index] < k:
                return
            self.count += 1
            for index in range(len(nums)):
                dfs(index+1)

        for i in range(len(nums)):
            dfs(i)
            print(self.count)
        return self.count


if __name__ == "__main__":
    s = Solution()
    s.subarrayLCM([3,6,2,7,1], 6)
