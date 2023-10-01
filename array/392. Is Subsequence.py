class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        for i in range(len(t)):
            if sp == len(s):
                return True
            if s[sp] == t[i]:
                sp += 1
        return sp == len(s)
