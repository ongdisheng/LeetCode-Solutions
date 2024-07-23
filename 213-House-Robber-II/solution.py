class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # edge case
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    
    def helper(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialise pointers
        rob1, rob2 = 0, 0

        for n in nums:
            # choose to include or exclude
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2