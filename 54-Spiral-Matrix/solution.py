class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time: O(m * n)
        Space: O(1)
        """
        # initialize variables
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # retrieve values in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # retrieve values in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # edge case
            if not (left < right and top < bottom):
                break

            # retrieve values in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # retrieve values in left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res