#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/13
"""
# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s.
# Otherwise, return false.

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
# They can be all found as substrings at indices 0, 1, 3 and 2 respectively.


class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        needed = 2 ** k # 1 << k
        # seen = set()
        # for i in range(k, len(s)):
        #     sub = s[i-k:i]
        #     if sub not in seen:
        #         seen.add(sub)
        #         needed -= 1
        #         if needed == 0:
        #             return True
        # return False
        # rolling hash
        all_one = needed - 1 # 111
        hash_val = 0
        got = [False] * needed
        for i in range(len(s)):
            hash_val = ((hash_val << 1) & all_one) | int(s[i])
            if i >= k - 1 and got[hash_val] is False:
                got[hash_val] = True
                needed -= 1
                if needed == 0:
                    return True
        return False


if __name__ == "__main__":
    s = "00110110"
    k = 3
    Solution().hasAllCodes(s, k)


