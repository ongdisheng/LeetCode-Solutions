class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variables
        count = 0
        index_sum, value_sum = 0, 0

        for i, value in enumerate(flips):
            value_sum += value
            index_sum += i+1
            count += (value_sum == index_sum)
        
        return count