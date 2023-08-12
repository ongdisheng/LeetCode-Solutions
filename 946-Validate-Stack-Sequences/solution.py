class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        # initialize variables
        stack = []
        i = 0
        n = len(popped)

        for p in pushed:
            stack.append(p)

            while stack and i < n and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return stack == []