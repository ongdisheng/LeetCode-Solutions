class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variables
        best = nums[0]
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0
            
            # update cur and best
            cur += n
            best = max(best, cur)

        return best