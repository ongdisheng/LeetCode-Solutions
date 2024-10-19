from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Time: O(m * n)
        Space: O(1)
        """
        # initialize variables
        rows, cols = len(mat), len(mat[0])
        dir_dict = defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                dir_dict[r+c].append(mat[r][c])
        
        res = []
        for key, value in enumerate(dir_dict.values()):
            # bottom up
            if key % 2 == 0:
                res += value[::-1]
            
            # top down
            else:
                res += value
        
        return res