class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = [0] * len(nums)
        neg = [0] * len(nums)
        pos[0] = 1 if nums[0] > 0 else 0
        neg[0] = 1 if nums[0] < 0 else 0
        ans = pos[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1
                neg[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
            elif nums[i] < 0:
                # if we have neg consecutive
                pos[i] = neg[i-1] + 1 if neg[i-1] > 0 else 0
                #  turn the pos consecutive to neg
                neg[i] = pos[i-1] + 1
            ans = max(ans, pos[i])
        return ans           