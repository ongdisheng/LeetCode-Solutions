class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """

        # initialize result list, pre and post variable
        result = []
        pre = 1
        post = 1

        # move from left to right
        for i in range(len(nums)):

            # update result list with pre value
            result.append(pre)

            # update pre value
            pre *= nums[i]

        # move from right to left
        for i in range(len(nums)-1, -1, -1):
            
            # update result list with post value
            result[i] *= post

            # update post value
            post *= nums[i]

        return result