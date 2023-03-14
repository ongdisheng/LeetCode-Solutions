class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(N)
        Space: O(N)
        """

        # initialize empty dict
        result_dict = {}

        # loop through each number in the list
        for num in nums:

            # found duplicate
            if num in result_dict:
                return True
            
            # first time seeing this number
            else:
                result_dict[num] = True
        
        return False