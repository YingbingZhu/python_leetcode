# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
#
# You need to implement the function pickIndex(),
# which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it.
# The probability of picking an index i is w[i] / sum(w).
#
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%),
# and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        totalSum = sum(w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i]/totalSum
        # prefix Sum
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        N = random.uniform(0, 1)

        return bisect.bisect_left(self.w,N)




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

