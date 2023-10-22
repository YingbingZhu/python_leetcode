class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        self.word1 = word1
        self.word2 = word2
        return self.helper(len(word1), len(word2))


    @lru_cache
    def helper(self, i, j):
        if i == 0:
            return j
        elif j == 0:
            return i
        elif self.word1[i-1] == self.word2[j-1]:
            return self.helper(i-1, j-1)
        else:
            return 1 + min(self.helper(i, j-1), self.helper(i-1, j), self.helper(i-1, j-1))
        