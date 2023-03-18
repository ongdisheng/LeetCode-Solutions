class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(n)
        """

        # initialize variables
        char_set = set()
        left = 0
        res = 0

        # expand sliding window
        for right in range(len(s)):

            # found duplicate
            while s[right] in char_set:

                # update char set and left counter
                char_set.remove(s[left])
                left += 1
            
            # add char at right index and update res variable
            char_set.add(s[right])
            res = max(res, right - left + 1)
        
        return res