class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time: O(s + t)
        Space: O(s + t)
        """

        # edge case
        if t == "":
            return ""
        
        # initialize count_t and window dict
        count_t, window = {}, {}

        # build count_t dict
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        # initialize have and need var
        # initialize res and res_len var
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity") 

        # initialize left pointer
        left = 0

        # sliding window
        for right in range(len(s)):
            
            # update window dict
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            # update have
            if char in count_t and count_t[char] == window[char]:
                have += 1
            
            # move left pointer
            while have == need:
                
                # update res
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # pop from left of window
                window[s[left]] -= 1

                # update have
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                
                left += 1
        
        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""