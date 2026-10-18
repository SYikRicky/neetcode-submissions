class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s_2 = 0 
        while True:
            if s_2 == s:
                return s
            s_2 = nums[s_2]
            s = nums[s]