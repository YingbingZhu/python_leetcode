#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/15
"""
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        stack = []
        for i in range(min(n, 9), 0, -1):
            stack.append(i)
        print(stack)
        ans = []
        while stack:
            curr = stack.pop()
            ans.append(curr)
            for i in range(9, -1, -1):
                nxt = curr * 10 + i
                if nxt <= n:
                    stack.append(nxt)
        return ans
        # while stack:
        #     curr = stack.pop()
        #     for nxt in range(1, 10):
        #         print(curr + str(nxt))
        #         if int(curr + str(nxt)) < n and curr + str(nxt) not in stack:
        #             stack.append(curr + str(nxt))
        # return stack


if __name__ == "__main__":
    s = Solution()
    s.lexicalOrder(13)
