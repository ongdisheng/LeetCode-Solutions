class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(26 * n) = O(n)
        Space: O(26) = O(1)
        """
        
        # define count dict and res var
        count = {}
        res = 0

        # initialize left pointer
        left = 0

        # sliding window
        for right in range(len(s)):

            # increment count 
            count[s[right]] = 1 + count.get(s[right], 0)

            # current window requires more than k times replacement
            while (right - left + 1) - max(count.values()) > k:
                
                # update count dict
                count[s[left]] -= 1

                # move left pointer 
                left += 1

            # update res
            res = max(res, right - left + 1)

        return res