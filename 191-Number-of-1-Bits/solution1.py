class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        # initialize result variable
        res = 0

        while n:
            # verify if rightmost bit is `1`
            res += n % 2

            # shift to right by 1 bit
            n = n >> 1

        return res