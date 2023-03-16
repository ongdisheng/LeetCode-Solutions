class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """

        # define res variable
        res = 0

        # define left and right counter
        # left = buy
        # right = sell
        # aim for <<buy low, sell high>>
        left, right = 0, 1

        while right < len(prices):

            # possible profit
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                res = max(res, current_profit)
            
            # <<buy high, sell low>>
            else:
                left = right
            
            # update right counter
            right += 1

        return res