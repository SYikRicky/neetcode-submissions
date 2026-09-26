from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1_counter = Counter(s1)
        while r < len(s2):
            chk_counter = Counter(s2[l : r + 1])
            if s1_counter == chk_counter:
                return True
            else:
                r += 1
                l += 1
        
        return False