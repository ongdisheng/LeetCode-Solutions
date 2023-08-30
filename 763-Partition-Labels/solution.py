class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        # initialize variables
        start = end = 0
        last = { c: i for i, c in enumerate(s) }
        res = []

        for i, c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                res.append(end - start + 1)
                start = i + 1

        return res
