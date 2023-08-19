class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time: O(n ^ 2)
        Space: O(n)
        """
        # initialize memo
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    memo[i] = memo[i + len(w)]
                if memo[i]:
                    break
        
        return memo[0]