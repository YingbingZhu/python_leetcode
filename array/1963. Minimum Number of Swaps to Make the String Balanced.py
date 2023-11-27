#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/8
"""
# You are given a 0-indexed string s of even length n.
# The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
#
# A string is called balanced if and only if:
#
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.
#
# Return the minimum number of swaps to make s balanced.


class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack = []
        for c in s:
            if c == "]":
                stack.append(c)
            else:
                if stack and stack[-1] == "]":
                    count += 1
                    stack.pop()
                stack.append(c)

        print(len(stack) // 4 + len(stack) % 4)

        # length of stack is number of not-paired brackets
        return len(stack) // 4 + len(stack) % 4
    

        # Solution 2
        # ]]][[[]]  [-1, -2, -3, -2, -1, 0, -1, -2]
        # each swap, at most decrese imbalance by 2
        # take leftmost ] and rightmost [
        # [1, ....]
        bal = 0
        ans = 0
        for symbol in s:
            if symbol == "[":
                bal += 1
            else:
                bal -= 1
            ans = min(ans, bal)
        return (-ans+1)//2



if __name__ == "__main__":
    s = Solution()
    s.minSwaps(s="][][")