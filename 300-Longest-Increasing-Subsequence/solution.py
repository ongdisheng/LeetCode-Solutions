class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time: O(n ^ 2)
        Space: O(n)
        """
        # initialize memo
        memo = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])

        return max(memo)