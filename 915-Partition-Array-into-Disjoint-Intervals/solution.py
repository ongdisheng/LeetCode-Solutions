class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variable
        left_max, right_max = nums[0], nums[0]
        partition_idx = 0

        for i in range(1, len(nums)):
            # update right max
            right_max = max(right_max, nums[i])

            if nums[i] < left_max:
                left_max = right_max
                partition_idx = i
        
        return partition_idx + 1