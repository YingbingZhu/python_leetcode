class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def check(arr):
            arr.sort()
            delta = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != delta:
                    return False
            return True
        
        ans = []
        m = len(l)
        n = len(nums)

        for i in range(m):
            cur = nums[l[i]:r[i]+1]
            ans.append(check(cur))
        
        return ans