class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        cnt = 0
        # 1 1 1 1 6
        for i, v in counter.items():
            cnt += v * (v - 1) // 2
        return cnt