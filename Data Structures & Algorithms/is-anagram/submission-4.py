class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = set()
        for char in s:
            seen.add(char)
        for char in t:
            if char not in seen:
                return False
        return True