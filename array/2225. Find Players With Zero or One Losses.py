#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/28
"""


# You are given an integer array matches where matches[i] = [winneri, loseri]
# indicates that the player winneri defeated player loseri in a match.
#
# Return a list answer of size 2 where:
#
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
#
# Note:
#
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.


class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        win = []
        lose = []
        lose_count = {}
        for winner, loser in matches:
            lose_count[winner] = lose_count.get(winner, 0)
            lose_count[loser] = lose_count.get(loser, 0) + 1

        for key, value in lose_count.items():
            if value == 0:
                win.append(key)
            elif value == 1:
                lose.append(key)

        print([sorted(win), sorted(lose)])
        return [sorted(win), sorted(lose)]




if __name__ == "__main__":
    s = Solution()
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    s.findWinners(matches)
