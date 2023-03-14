class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(s)
        Space: O(s + t)
        """

        # s and t are of different length
        if len(s) != len(t):
            return False
        
        # initialise counter dict
        counter_s = {}
        counter_t = {}

        # loop through each character in s and t
        for i in range(len(s)):

            # update counter dict
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        
        return counter_s == counter_t