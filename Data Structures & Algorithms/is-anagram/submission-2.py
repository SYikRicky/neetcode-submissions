class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        for char in s:
            seen.add(char)
        for char in s:
            if char in seen:
                return True
        return False
