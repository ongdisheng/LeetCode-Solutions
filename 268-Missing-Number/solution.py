class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        return sum(range(len(nums) + 1)) - sum(nums)