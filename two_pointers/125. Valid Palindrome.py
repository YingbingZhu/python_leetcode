class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    Solution().isPalindrome(s)