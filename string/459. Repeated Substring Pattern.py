class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # remove head and tail
        return s in (s+s)[1:-1]
