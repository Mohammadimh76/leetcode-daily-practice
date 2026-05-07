class Solution:
    def isPalindrome(s: str) -> bool:
        
        s = s.lower() 
        left, right = 0, len(s) - 1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left] != s[right]:
                return "is not a palindrome"
            
            left += 1
            right -= 1
            
        return "is a palindrome"


print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
        