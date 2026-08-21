from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        res = 1
        for num in nums:
            if num-1 in seen:
                continue
            temp = 1
            next_num = num + 1
            while next_num in seen:
                temp += 1
                next_num += 1
            res = max(res, temp)

        return res  