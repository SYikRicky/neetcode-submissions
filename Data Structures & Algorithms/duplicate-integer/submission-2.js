class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // 1. empty? if yes, return false.
        // 2. hash map O(n) / brute force O(n^2)
        if (nums.length === 0) return false;
        let checkDuplicate = new Map();
        
        for (let i in nums) {
            if (checkDuplicate.has(nums[i])) {
                return true
            }
            checkDuplicate.set(nums[i]);
        }
        return false;
    }
}
