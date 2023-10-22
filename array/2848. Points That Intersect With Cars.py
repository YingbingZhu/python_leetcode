class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        cnt = 0
        max_r = -1
        for l, r in nums:
            if r > max_r:
                max_l = max(l, max_r)
                cnt += r - max_l
                # new interval
                if l > max_r:
                    cnt += 1
                max_r = max(max_r, r)
        return cnt

