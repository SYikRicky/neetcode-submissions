from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        res = 0
        temp_nums = deque(nums)
        count = 0

        while temp_nums:
            next_num = temp_nums[0]
            temp = 0
            while next_num in seen:
                temp += 1
                if temp_nums:
                    temp_nums.popleft()
                next_num += 1
            res = max(temp, res)

        return res 