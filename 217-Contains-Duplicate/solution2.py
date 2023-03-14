class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(N)
        Space: O(N)
        """
        return len(set(nums)) != len(nums)