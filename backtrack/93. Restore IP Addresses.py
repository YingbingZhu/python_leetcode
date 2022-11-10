#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/10
"""
# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
# but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits,
# return all possible valid IP addresses that can be formed by inserting dots into s.
# You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.backtrack(s, 0, "", res)
        return res

    # k is counter
    def backtrack(self, s, k, path, res):
        if k > 4:
            return
        if k == 4 and not s:
            res.append(path[:-1])
            print(res)
        for i in range(1, min(4, len(s)+1)):
            if s[:i] == '0' or (s[0] != '0' and 1 <= int(s[:i]) <= 255):
                self.backtrack(s[i:], k+1, path+s[:i]+".", res)


if __name__ == "__main__":
    s = Solution()
    s.restoreIpAddresses("101023")


