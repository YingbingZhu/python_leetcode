from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1 = Counter(word1)
        c2 = Counter(word2)
        if sorted((c1.values())) == sorted(c2.values()) and set(c1.keys()) == set(c2.keys()):
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    word1 = "a"
    word2 = "aa"
    s.closeStrings(word1, word2)