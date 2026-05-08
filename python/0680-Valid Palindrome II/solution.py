class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() 
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1 
                right -= 1
            elif s[left] != s[right]:
                return self.Solution.isPalindrome(s, left + 1, right) or self.Solution.isPalindrome(s, left, right -1)
        
        return True

    def isPalindrome(s: str, left: int, right: int) -> bool:
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


        