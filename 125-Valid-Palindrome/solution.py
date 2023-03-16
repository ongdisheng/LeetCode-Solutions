class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(1)
        """

        # initialize left and right counter
        left, right = 0, len(s) - 1

        # compare left and right
        while left < right:

            # skip non-alphanumeric char
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while left < right and not self.isAlphanumeric(s[right]):
                right -= 1
            
            # non-palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            # update left and right counter
            left += 1
            right -=1
        
        return True

    
    def isAlphanumeric(self, char):
        """
        Check if given character is alphanumeric 
        """
        return (
            ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9")
        )
