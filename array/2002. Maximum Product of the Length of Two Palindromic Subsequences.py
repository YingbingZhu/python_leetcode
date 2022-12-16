class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        arr = []
        # (1<<n) represents all possible combinations to use or not for each index of the string.
        # (e.g. s = "aba", 100: "a", 011: "ba").
        for mask in range(1, 1 << n):
            subseq = ''
            for i in range(n):
                # if used
                if mask & (1 << i) > 0:
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((mask, len(subseq)))

        arr.sort(key=lambda x:x[1], reverse=True)
        res = 1
        for i in range(len(arr)):
            mask1, len1 = arr[i]
            if len1 ** 2 < res:
                break
            for j in range(i+1, len(arr)):
                mask2, len2 = arr[j]
                # disjoint
                if mask1 & mask2 == 0 and len1 * len2 > res:
                    res = len1 * len2
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    s1 = "le"
    s.maxProduct(s1)