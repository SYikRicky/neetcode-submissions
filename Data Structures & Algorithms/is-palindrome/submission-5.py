import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        mod_s = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(mod_s) - 1
        while l < r:
            if mod_s[l] != mod_s[r]:
                return False
            l += 1
            r -= 1
        # abccba
        #  l  r
        # l+=1, r-=1
        # l > r
        return True