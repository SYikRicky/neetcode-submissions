from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # lecabee | abc
        #   l r
        # l, r not in 
        # r in abc -> counter["c"] += 1 -> l += 1, r+=1, check counter
        # l, r in abc -> counter["a"] += 1 -> r += 1
        # len(counter) > len(-> 
        if s1 == s2:
            return True

        if len(s1) == 1:
            return True if s1 in s2 else False
            
        s1_counter = Counter(s1)
        l, r = 0, 0

        chk_counter = Counter()
        while r < len(s2):
            if r - l > len(s1):
                chk_counter.clear()
                l = r
                continue

            if s2[l] not in s1 and s2[r] not in s1:
                l += 1
            elif s2[r] in s1:
                chk_counter[s2[r]] += 1
                if s2[l] not in s1:
                    l += 1
            elif s2[r] not in s1:
                while l != r:
                    if chk_counter == s1_counter:
                        return True 
                    chk_counter[s2[l]] -= 1
                    l += 1
            r += 1
            print(chk_counter)
            if chk_counter == s1_counter:
                return True 
        
        while l != r:
            if chk_counter == s1_counter:
                return True 
            chk_counter[s2[l]] -= 1
            l += 1

        return False