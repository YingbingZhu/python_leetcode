class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        height = len(matrix)
        width = len(matrix[0])
        top = 0
        bottom = height - 1
        left = 0
        right = width - 1

        while left < right and top < bottom:
            for col in range(left, right):
                res.append(matrix[top][col])
            for row in range(top, bottom):
                res.append(matrix[row][right])
            for col in range(right, left, - 1):
                res.append(matrix[bottom][col])
            for row in range(bottom, top, - 1):
                res.append(matrix[row][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        # edge case: 
        if len(res) < height * width:
            for row in range(top, bottom+1):
                for col in range(left, right+1):
                    res.append(matrix[row][col])
        
        return res

