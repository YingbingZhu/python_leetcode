class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur = 0
        cnt = {}
        for num in nums:
            cur = (cur + num) % k
            if cur in cnt:
                cnt[cur] += 1
            else:
                cnt[cur] = 1
        ans = 0
        for k, v in cnt.items():
            ans += v * (v - 1) // 2
        return ans + cnt[0] if 0 in cnt else ans
        