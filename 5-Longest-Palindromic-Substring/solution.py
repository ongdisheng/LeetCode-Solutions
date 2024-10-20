class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time: O(n ^ 2)
        Space: O(1)
        """
        # initialize variables
        res = ''
        res_len = 0

        for i in range(len(s)):
            # odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                # update pointers
                left -= 1
                right += 1
            
            # even length
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                # update pointers
                left -= 1
                right += 1

        return res