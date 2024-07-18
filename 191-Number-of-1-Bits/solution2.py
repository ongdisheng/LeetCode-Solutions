class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        # initialize result variable
        res = 0

        while n:
            # AND operator
            n = n & (n - 1)

            # increment result
            res += 1

        return res