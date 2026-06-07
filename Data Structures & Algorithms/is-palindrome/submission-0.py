class Solution:
    def isPalindrome(self, s: str) -> bool:
        t= ''.join(char.lower() for char in s[::-1] if char.isalnum())
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        if clean_s ==t:
            print(t)
            return True
        else:
            print(t)
            return False
        
