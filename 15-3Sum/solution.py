class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n log n) + O(n^2) = O(n^2)
        Space: O(1)
        """

        # initialize empty result list
        res = []

        # sort input nums list
        nums.sort()

        # triplets [nums[i], nums[j], nums[k]]
        # outer loop handles nums[i]
        for i in range(len(nums)):

            # avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # initialize left and right pointer
            left, right = i + 1, len(nums) -1

            # find nums[j] and nums[k] using two pointer
            while left < right:
                
                # get sum of current triplets
                current_sum = nums[i] + nums[left] + nums[right]

                # decrement right
                if current_sum > 0:
                    right -= 1
                
                # increment left
                elif current_sum < 0:
                    left += 1

                # nums[i] + nums[j] + nums[k] = 0
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # avoid duplicate triplets
                    # update left pointer
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return res