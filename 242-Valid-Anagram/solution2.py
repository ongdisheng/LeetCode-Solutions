class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n log n)
        Space: O(n) or O(1) 
        """
        return sorted(s) == sorted(t)