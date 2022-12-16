class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        count = 0
        while l <= r:
            if s[l] != s[r]:
                delete_l = s[l+1:r+1]
                delete_r = s[l:r]
                return delete_l == delete_l[::-1] or delete_r == delete_r[::-1]
            l += 1
            r -= 1
        return True

