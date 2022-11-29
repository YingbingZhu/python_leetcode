#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/28
"""


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = 0
        seen = set()
        for email in emails:
            domain = email.split('@')[1]
            name = email.split('@')[0].split('+')[0].replace('.', '')

            seen.add(domain+name)
        return len(seen)

