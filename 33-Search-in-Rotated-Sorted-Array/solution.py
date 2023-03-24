class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time: O(log n)
        Space: O(1)
        """

        # initialize left and right pointer
        left, right = 0, len(nums) - 1

        # binary search
        while left <= right:

            # find middle index
            mid = (left + right) // 2

            # found target
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[left] <= nums[mid]:

                # search to the right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                
                # search to the left
                else:
                    right = mid - 1

            # right sorted portion
            else:

                # search to the left
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                
                # search to the right
                else:
                    left = mid + 1
        
        return -1