### Search in a sorted matrix (each row sorted) last element in the row < first element in the next row
### If you just flatten the matrix O(m*n) but we want a more efficient way: O(log(m*n))) --> binary serach
### Virtually flatten, do the same thing as before in the binary serach but convert mid to row and column to index the matrix instead of the 1D array
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1

        while l<=r:
            mid = (l+r)//2
            rw = mid//n
            col = mid%n

            if matrix[rw][col] > target:
                r = mid - 1
            elif matrix[rw][col] < target:
                l = mid + 1
            else:
                return True
        return False
