class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Idea: Quickselect
        Time: O(n) average; O(n^2) worst
        Space: O(n)
        """

        # get the index of target element in sorted array
        k = len(nums) - k

        # quickselect
        def quickSelect(left, right):

            # get pivot element
            pivot = nums[right]

            # set the start index of p
            p = left

            # iterate from left to right (excluding)
            for i in range(left, right):

                # swap nums[i] with nums[p]
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            # swap nums[p] with nums[right] (pivot)
            nums[p], nums[right] = nums[right], nums[p]
            
            if p < k:
                return quickSelect(p+1, right)
            elif p > k:
                return quickSelect(left, p-1)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums)-1)