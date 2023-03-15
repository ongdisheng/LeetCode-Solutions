class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """

        # initialize longest variable
        longest = 0

        # convert input list to set
        nums_set = set(nums)

        # loop through each number in the set
        for num in nums_set:

            # no left neighbour
            # start of sequence
            if num - 1 not in nums_set:
                
                # finding right neighbour
                length = 1
                while (num + length) in nums_set:
                    length += 1
                
                # update longest variable
                longest = max(longest, length)

        return longest