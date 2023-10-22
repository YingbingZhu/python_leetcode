class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2, c1, c2 = 0, 0, 0, 0
        for num in nums:
            # potential number
            if cnt1 == 0 and num != c2:
                c1 = num
                cnt1 = 1
            elif cnt2 == 0 and num != c1:
                c2 = num
                cnt2 = 1

            elif num == c1:
                cnt1 += 1

            elif num == c2:
                cnt2 += 1

            else:
                # find a number different from c1 and c2
                cnt1 -= 1
                cnt2 -= 1

        return [c for c in {c1, c2} if nums.count(c) > len(nums) // 3]

