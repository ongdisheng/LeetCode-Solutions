class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        # initialize memo
        memo = [0] * (n + 1)
        offset = 1

        # formula: 1 + memo[i - offset]
        for i in range(1, n + 1):
            # update offset
            if offset * 2 == i:
                offset = i

            # update memo
            memo[i] = 1 + memo[i - offset]
        
        return memo