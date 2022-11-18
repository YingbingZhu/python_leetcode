#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/18
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or strs == [""]:
            return ""
        prefix = []
        for i in zip(*strs):
            if len(set(i)) > 1:
                return "".join(prefix)
            prefix.append(i[0])
        return "".join(prefix)


if __name__ =="__main__":
    s = Solution()
    strs = ["flower", "flow", "flight"]
    s.longestCommonPrefix(strs)