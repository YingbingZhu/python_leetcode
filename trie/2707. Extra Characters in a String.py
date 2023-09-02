class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        # build Tree
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

        # dp
        n = len(s)
        dp = [float('inf')] * (n + 1)

        # empty string
        dp[-1] = 0

        for l in reversed(range(n)):
            dp[l] = dp[l + 1] + 1
            node = root
            for r in range(l, n):
                if s[r] not in node.children:
                    break
                node = node.children[s[r]]
                if node.is_word == True:
                    dp[l] = min(dp[l], dp[r + 1])

        return dp[0]

