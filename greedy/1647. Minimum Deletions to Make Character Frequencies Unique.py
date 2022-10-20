# A string s is called good if there are no two different characters in s that have the same frequency.
#
# Given a string s, return the minimum number of characters you need to delete to make s good.
#
# The frequency of a character in a string is the number of times it appears in the string. For example,
# in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.


class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        seen = set()
        dels = 0
        for k, v in counter.items():
            while v > 0 and v in seen:
                dels += 1
                v -= 1
            seen.add(v)
        return dels
