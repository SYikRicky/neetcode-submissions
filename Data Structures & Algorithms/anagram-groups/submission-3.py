class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. sort -> group, O(nlogn)
       # { sorted word : [str] }
        seen = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in seen:
                seen[sorted_word] = [word]
            else:
                seen[sorted_word].append(word)
        return list(seen.values())
        