class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """

        # initialize empty dict
        result_dict = {}

        # loop through each number in the list
        for i in range(len(nums)):
            
            # found second number add up to target
            if target - nums[i] in result_dict:
                return [result_dict[target - nums[i]], i]
            
            else:
                result_dict[nums[i]] = i