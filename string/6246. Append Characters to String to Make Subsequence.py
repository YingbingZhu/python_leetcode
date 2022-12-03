class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ps = pt = 0
        res = 0
        while pt < len(t) and ps < len(s):
            if t[pt] == s[ps]:
                ps += 1
                pt += 1
            else:
                ps += 1
            print(ps, pt)
        if pt < len(t):
            res += len(t) - pt
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    s.appendCharacters(s = "zac", t = "abcde")