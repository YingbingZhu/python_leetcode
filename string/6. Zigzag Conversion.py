class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
        direction = 1
        res = [''] * numRows
        index = 0

        for ch in s:
            res[index] += ch
            if index == numRows - 1:
                direction = -1
            elif index == 0:
                direction = 1
            
            index += direction
        return ''.join(res)
            
