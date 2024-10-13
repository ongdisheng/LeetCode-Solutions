class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time: O(n * m)
        Space: O(n)
        """
        # initialize memo
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0

        # dp
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    memo[a] = min(memo[a], 1 + memo[a-c])
        
        return memo[amount] if memo[amount] != amount + 1 else -1