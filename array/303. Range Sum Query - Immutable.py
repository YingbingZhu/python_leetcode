class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.acc = []
        cur = 0
        for num in nums:
            cur += num
            self.acc.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right] - self.acc[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)