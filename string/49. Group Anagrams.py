class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            curr = []
            sortedS = ''.join(sorted(s))
            if sortedS not in d:
                d[sortedS] = [s]
            else:
                d[sortedS].append(s)
        return d.values()