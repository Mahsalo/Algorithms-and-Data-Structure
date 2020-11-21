import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ## Move each row to the other end of the array, first row to last row 
        rows = len(matrix)
        cols = len(matrix[0])        
        c=np.ceil(rows/2)
        for i in range(int(c)):
            frst_row = matrix[i]
            sc_row = matrix[rows-1-i]
            matrix[i] = sc_row
            matrix[rows-1-i] = frst_row
        ## Find the transpose of the matrix
        tmp = matrix
        tmp=np.array(tmp)
        for i in range(rows):
            tmp_col = np.reshape(tmp[:,i],(1,rows))
            l=list(tmp_col)
            matrix[i]= l[0]
       
            