class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(n)
        """
        # initialize variables
        stack = []
        visit = set()
        last = {}
        
        # update last occurrence 
        for i in range(len(s)):
            last[s[i]] = i

        for i, ch in enumerate(s):
            # avoid duplicate
            if ch in visit:
                continue
            
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                rm = stack.pop()
                visit.remove(rm)
            
            visit.add(ch)
            stack.append(ch)
        
        return ''.join(stack)