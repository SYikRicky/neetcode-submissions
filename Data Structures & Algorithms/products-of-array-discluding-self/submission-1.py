class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        temp = 1
        for num in nums:
            res.append(temp)
            temp *= num
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
        return res
