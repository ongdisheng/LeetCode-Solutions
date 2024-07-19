class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time: O(n * m)
        Space: O(n * m)
        """
        # edge case 
        if not grid: 
            return 0

        # initialize variables
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            # initialize queue
            queue = collections.deque()
            queue.append((r, c))
            visit.add((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dx, dy in directions:
                    r = row + dx
                    c = col + dy
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        visit.add((r, c))
                        queue.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                # encounter island
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    res += 1
            
        return res