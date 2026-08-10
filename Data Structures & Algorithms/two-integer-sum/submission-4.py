class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hash_map = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in hash_map:
                return [hash_map[find], i]
            hash_map[nums[i]] = i