class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time: O(n * m)
        Space: O(n * m)
        """
        # initialize variables
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        # depth first search
        def dfs(r, c, visit, prev_height):
            # base case
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or 
                prev_height > heights[r][c]):
                return
            
            visit.add((r, c))
            # recursive case
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])

        # upper and bottom row
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        # left and right column
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res