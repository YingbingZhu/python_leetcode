class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        max_freq = 0
        start = 0
        n = len(s)
        freq = {}
        for end in range(n):
            freq[s[end]] = freq.get(s[end], 0) + 1
            #  max_freq would not decrease
            max_freq = max(max_freq, freq[s[end]])
            # not a valid substring
            if (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            # the substring length would not decrease
            res = end - start + 1
            print(freq)
        return res

if __name__ == "__main__":
    s = "ABAA"
    k = 0
    Solution().characterReplacement(s, k)
