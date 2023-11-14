class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        min_index = [float('inf')] * 26
        max_index = [float('-inf')] * 26

        # get min and max index of each character
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            min_index[index] = min(i, min_index[index])
            max_index[index] = max(i, max_index[index])

        ans = 0
        # iterate over all alphabets
        for i in range(26):
            if min_index[i] != float('inf') and max_index[i] != float('-inf'):
                ans += len(set(s[min_index[i] + 1:max_index[i]]))

        return ans

        return ans


