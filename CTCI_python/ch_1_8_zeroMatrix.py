import numpy as np
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        zeros_row = np.zeros((rows,1))
        zeros_col = np.zeros((cols,1))
        all_z_rows = [0]*cols
        
        for i in range (rows):
            for j in range (cols):
                if matrix[i][j]==0:
                    zeros_row[i]+=1
                    zeros_col[j]+=1
        for i in range (cols):
            for j in range (rows):
                if zeros_row[j] !=0:
                    matrix[j]= all_z_rows
                if zeros_col[i]!=0:
                    matrix[j][i]=0
            