class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let n = nums.length;
        let left = 0;
        let right = n - 1;
        
        while (left != right) {
            if (nums[left] < nums[right]) {
                left++;
            } else if (nums[left] > nums[right]) {
                right++;
            } else {
                return true;
            }
        }
        return false;
    }
}
