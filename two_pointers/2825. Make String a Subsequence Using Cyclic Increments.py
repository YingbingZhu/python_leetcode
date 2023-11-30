class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def getNext(ch):
            ord_number = ord(ch) - ord('a')
            if ord_number == 25:
                return 'a'
            return chr(ord_number+ord('a')+1)

        p1 = 0
        p2 = 0
        while p1 < len(str1) and p2 < len(str2):
            if str1[p1] == str2[p2] or getNext(str1[p1]) == str2[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        return p2 == len(str2)