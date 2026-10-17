class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        travelled: dict[int, int] = {} # val, idx
        for i in range(len(nums)):
            find = target - nums[i]
            if find in travelled:
                return [travelled[find], i]
            travelled[nums[i]] = i