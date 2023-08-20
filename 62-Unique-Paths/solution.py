class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(m * n)
        Space: O(n)
        """
        # initialize memo
        memo = [1] * n

        for _ in range(m-1):
            new = [1] * n
            for j in range(n-2, -1, -1):
                new[j] = new[j+1] + memo[j]
            memo = new
        
        return memo[0]