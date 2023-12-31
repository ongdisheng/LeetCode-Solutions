class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time: O(n * m)
        Space: O(n * m)
        """
        # initialize memo
        memo = []
        for _ in range(len(text1) + 1):
            memo.append([0] * (len(text2) + 1))

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                # match
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                
                # non-match
                else:
                    memo[i][j] = max(memo[i+1][j], memo[i][j+1])
        
        return memo[0][0]