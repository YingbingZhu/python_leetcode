class UnionFind:
    def __init__(self):
        self.parents = [i for i in range(26)]

    def find(self, a):
        if a != self.parents[a]:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if pa < pb:
            self.parents[pb] = pa
        else:
            self.parents[pa] = pb


class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        uf = UnionFind()
        res = ""
        for i in range(len(s1)):
            a = ord(s1[i]) - ord('a')
            b = ord(s2[i]) - ord('a')
            uf.union(a, b)

        for i in range(len(baseStr)):
            ch = uf.find(ord(baseStr[i]) - ord('a')) + 97
            res += chr(ch)
        return res
