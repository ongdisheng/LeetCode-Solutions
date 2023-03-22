class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """

        # initialize close to open map and stack
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []

        # loop through input string
        for char in s:

            # current char is open bracket
            if char not in close_to_open:

                # push to stack
                stack.append(char)
            
            # current char is close bracket
            # invalid: stack is empty or mismatch open close bracket
            elif len(stack) == 0 or stack.pop() != close_to_open[char]:
                return False
        
        return len(stack) == 0