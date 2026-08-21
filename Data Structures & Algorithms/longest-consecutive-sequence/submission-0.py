class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        res = 0
        for num in nums:
            next_num = num
            temp = 0
            while next_num in seen:
                temp += 1
                next_num += 1
            res = max(temp, res)

        return res 