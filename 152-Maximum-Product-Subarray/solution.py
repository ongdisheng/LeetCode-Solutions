class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variables
        best = nums[0]
        cur_min, cur_max = 1, 1

        for n in nums:
            temp = n * cur_min
            cur_min = min(temp, n * cur_max, n)
            cur_max = max(temp, n * cur_max, n)

            # update best
            best = max(best, cur_max)
        
        return best