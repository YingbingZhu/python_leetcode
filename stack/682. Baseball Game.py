#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/27
"""


# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.


class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        stack = []
        for o in operations:
            print(stack)
            if o == '+':
                stack.append(stack[-1] + stack[-2])
            elif o == 'C':
                stack.pop()
            elif o == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(o))
        print(stack)
        return sum(stack)


if __name__ == '__main__':
    operations = ["5","-2","4","C","D","9","+","+"]
    Solution().calPoints(operations)
