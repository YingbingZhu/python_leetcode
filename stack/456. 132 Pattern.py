class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # minimum element till i
        min_arr = [nums[0]] * n
        for i in range(1, n):
            min_arr[i] = min(min_arr[i - 1], nums[i])

        stack = []
        for j in range(n - 1, -1, -1):
            # find potential 2
            while stack and stack[-1] <= min_arr[j]:
                stack.pop()
            # find 3 , greater than 2
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False
