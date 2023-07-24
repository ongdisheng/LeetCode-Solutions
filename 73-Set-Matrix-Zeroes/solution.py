class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Time: O(m * n)
        Space: O(1)
        """
        # initialize variables
        rows, columns = len(matrix), len(matrix[0])
        row_zero = False

        # determine which row and column should be set to 0
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        
        # set previously determined rows and columns to 0 
        # (except row 0 and column 0)
        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # special case
        # handle column 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # special case
        # handle row 0
        if row_zero:
            for c in range(columns):
                matrix[0][c] = 0