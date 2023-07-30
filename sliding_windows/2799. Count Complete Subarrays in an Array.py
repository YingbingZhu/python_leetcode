class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        required = len(set(nums))
        left = 0
        cnt = 0
        freq = {}

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            #  find the left, [2, 2, 2, 3] > [2, 3] : sub array are 3, cur left = 3
            while len(freq.keys()) == required:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            cnt += left
        return cnt

