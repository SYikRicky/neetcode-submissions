class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = nums[0]
        f = nums[nums[s]]
        while True:
            if s == f:
                return s
            s = nums[s]
            f = nums[nums[s]]