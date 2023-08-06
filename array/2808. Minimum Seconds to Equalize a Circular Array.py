from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        # store indices of each number
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        res = n
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        for l in indices.values():
            l.append(l[0] + n)
            res = min(res, max(y - x for x, y in pairwise(l)) // 2)

        return res