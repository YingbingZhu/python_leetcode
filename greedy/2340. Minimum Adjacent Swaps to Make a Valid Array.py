class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        mx = max(nums)
        mi = min(nums)
        mxp = 0
        mip = len(nums) - 1
        # get the rightmost max and leftmost min
        for i in range(len(nums)):
            if nums[i] == mx:
                mxp = max(mxp, i)
            if nums[i] == mi:
                mip = min(mip, i)
        
        if mip > mxp:
            return mip + len(nums) - 2 - mxp 
        return mip + len(nums) - 1 - mxp
        
        


                