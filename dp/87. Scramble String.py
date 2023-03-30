class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = {}
        def func(s1, s2):
            if (s1, s2) in m:
                return m[(s1, s2)]
            if not sorted(s1) == sorted(s2):
                return False
            if len(s1) == 1:
                return True
            
            for i in range(1, len(s1)):
                # swap and non-swap
                if func(s1[:i], s2[-i:]) and func(s1[i:], s2[:-i]) or func(s1[:i], s2[:i]) and func(s1[i:], s2[i:]):
                    return True
            m[(s1, s2)] = False
            return False
        return func(s1, s2)
        