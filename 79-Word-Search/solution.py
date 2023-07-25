class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time: O(m * n * 4 ^ len(word))
        Space: O(len(word)) due to recursive stack
        """
        # initialize variables
        rows, cols = len(board), len(board[0])

        # visited path
        path = set()

        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            
            # invalid case
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or 
                (r, c) in path):
                return False
            
            # found character in current cell 
            path.add((r, c))

            # recursive case
            res = (dfs(r - 1, c, i + 1) or 
                   dfs(r + 1, c, i + 1) or
                   dfs(r, c - 1, i + 1) or 
                   dfs(r, c + 1, i + 1))
            
            # remove current coordinate from visited path
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False