class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_l, first_r = 0, 0
        second_l, second_r = 0, len(nums) - 1
        while second_l <= second_r:
            if nums[second_l] < nums[second_l - 1]:
                break
            second_l += 1
        first_r = second_l - 1
        print(f"{first_l} {first_r} {second_l} {second_r}")

        while first_l <= first_r:
            m = first_l + (first_r - first_l) // 2
            if nums[m] < target:
                first_l = m + 1
            elif nums[m] < target:
                first_r = m - 1
            elif nums[m] == target:
                return m
            else:
                break
        
        while second_l <= second_r:
            m = second_l + (second_r - second_l) // 2
            if nums[m] < target:
                second_l = m + 1
            elif nums[m] < target:
                second_r = m - 1
            elif nums[m] == target:
                return m
            else:
                break

        return -1