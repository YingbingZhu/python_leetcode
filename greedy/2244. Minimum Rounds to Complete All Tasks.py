# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task.
# In each round,
# you can complete either 2 or 3 tasks of the same difficulty level.
#
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
from collections import Counter


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        d = Counter(tasks)
        res = 0
        for v in d.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += v // 3
            else:
                res += 1 + v // 3
        print(res)
        return res


if __name__ == '__main__':
    Solution().minimumRounds(tasks=[5,5,5,5])
