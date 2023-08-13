class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Time: O(n log n)
        Space: O(1)
        """
        # initialize variables
        rank = [26] * 26

        for i in range(len(order)):
            rank[ord(order[i]) - ord('a')] = i
        
        res = [c for c in s]
        res.sort(key=lambda x: rank[ord(x) - ord('a')])
        return ''.join(res)