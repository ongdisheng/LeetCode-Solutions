class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        # initialize result variable
        res = 0

        for i in range(32):
            # retrieve bit from right to left
            bit = (n >> i) & 1

            # set bit from left to right
            res = res | (bit << (31 - i))
        
        return res