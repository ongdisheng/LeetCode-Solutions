class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Time: O(log n)
        Space: O(1)
        """

        # initialize res
        res = nums[0]

        # initialize left and right pointer
        left, right = 0, len(nums) - 1

        # binary search
        while left <= right:

            # located in sorted portion
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            # find mid
            mid = (left + right) // 2
            res = min(res, nums[mid])

            # located in left sorted portion
            # search to the right
            if nums[mid] >= nums[left]:
                left = mid + 1
            
            # located in right sorted portion
            # search to the left
            else:
                right = mid - 1
        
        return res