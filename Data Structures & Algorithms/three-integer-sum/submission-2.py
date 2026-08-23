class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        i = 0
        while i <= len(nums) - 3:
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                lf_sum = nums[l] + nums[r]
                if lf_sum < target:
                    l += 1
                elif lf_sum > target:
                    r -= 1
                elif lf_sum == target:
                    res.add((nums[i], nums[l], nums[r]))
                    break
            i += 1
        return [list(output) for output in res]