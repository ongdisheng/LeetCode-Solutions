class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Time: O(n ^ 2)
        Space: O(1)
        """
        # initialize left and right pointer
        left, right = 0, len(matrix) - 1

        # modify from outermost to innermost
        while left < right:
            
            # initialize top and bottom pointer
            top, bottom = left, right

            for i in range(right - left):

                # save top left to temp variable
                top_left = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left to top right using saved temp variable
                matrix[top + i][right] = top_left
            
            left += 1
            right -= 1