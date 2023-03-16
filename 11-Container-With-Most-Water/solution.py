class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """

        # initialize res variable
        res = 0

        # initialize left and right pointer
        left, right = 0, len(height) - 1

        # solve using two pointer
        while left < right:

            # find current area
            area = (right - left) * (min(height[left], height[right]))

            # update res
            res = max(res, area)

            # update left and right pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return res