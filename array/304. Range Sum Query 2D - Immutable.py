#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/13
"""


# Given a 2D matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
# and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix.
# int sumRegion(int row1, int col1, int row2, int col2)
# Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
# and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.colSum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.preSum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            pre = 0
            for j in range(len(matrix)):
                pre += matrix[j][i]
                self.colSum[j][i] = pre
        for i in range(len(matrix)):
            pre = 0
            for j in range(len(matrix[0])):
                print(i, j)
                pre += self.colSum[i][j]
                self.preSum[i][j] = pre
        print(matrix)
        print(self.colSum)
        print(self.preSum)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        left = 0 if col1 == 0 else self.preSum[row2][col1 - 1]
        top = 0 if row1 == 0 else self.preSum[row1 - 1][col2]
        top_left = 0 if (row1 == 0 or col1 == 0) else self.preSum[row1 - 1][col1 - 1]

        return self.preSum[row2][col2] - left - top + top_left


if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
