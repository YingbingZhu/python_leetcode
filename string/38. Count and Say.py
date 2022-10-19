# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string,
# split it into the minimal number of substrings such that each substring contains exactly one unique digit.
# Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # base case
        s = '1'
        count = 1
        for _ in range(n-1):
            tmp = []
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(s[i-1])
            tmp.append(str(count))



