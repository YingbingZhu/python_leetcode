# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
#
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
#
# You are given a string dominoes representing the initial state where:
#
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
#
# https://leetcode.com/problems/push-dominoes/

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        d = 'L' + dominoes + 'R'
        i = 0
        res = ""
        for j in range(1, len(d)):
            if d[j] == '.':
                continue
            distance = j - i - 1
            if i > 0:
                res += d[i]
            if d[i] == d[j]:
                res += d[i] * distance
            elif d[i] == 'L' and d[j] == 'R':
                res += '.' * distance
            else:
                res += 'R' * (distance // 2) + '.' * (distance % 2) + 'L' * (distance // 2)
            i = j
        return res


