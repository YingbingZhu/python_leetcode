class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        print(ord(columnNumber)-ord('A')+1)
        return columnNumber-ord('A')




if __name__ =="__main__":
    s = Solution()
    s.convertToTitle(columnNumber='A')