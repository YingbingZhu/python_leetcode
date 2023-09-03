class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        cnts = [0] * len(nums)
        for i, v in enumerate(nums):
            if v % modulo == k:
                cnts[i] = 1

        # prefix_sum
        ps = [0]
        for num in cnts:
            ps.append(ps[-1] + num)

        counter = defaultdict(int)
        counter[0] = 1
        res = 0
        for i in range(1, len(nums) + 1):
            #
            res += counter[(ps[i] - k) % modulo]
            # range[0, modulo-1]
            counter[ps[i] % modulo] += 1
        return res

        # def isInteresting(nums):
        #     return sum(nums) % modulo == k

        # res = 0
        # for l in range(len(nums)):
        #     for r in range(l, len(nums)):
        #         r = l
        #         while isInteresting(cnts[l:r+1]):
        #         if isInteresting(cnts[l:r+1]):
        #             res += 1

        # return res