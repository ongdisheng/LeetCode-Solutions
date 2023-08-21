class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        # initialize variables
        res = []
        carry = 0

        while carry or arr1 or arr2:
            if arr1:
                carry += arr1.pop()
            if arr2:
                carry += arr2.pop()
            
            # update 
            res.append(carry & 1)
            carry = -(carry >> 1)

        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return res[::-1]