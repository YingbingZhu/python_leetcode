class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = i = 0
        res = []
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i+1]:
                res.append(self.getRange(nums[start], nums[i]))
                start = i + 1
            i += 1
        res.append(self.getRange(nums[start], nums[i]))
        return res


    def getRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)


            