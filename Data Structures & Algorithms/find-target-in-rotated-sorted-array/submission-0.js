class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        // 3456|12
        // l m   r
        // 1. if target < nums[m] (target may exist in both array)
        //   1.1 if target <= nums[l] , l = m + 1
        //   1.2 if target > num[l], r = m - 1
        // 2. if target > nums[m] (eliminate element in the left of m)
        //   2.1 
        
        let l = 0;
        let r = nums.length - 1;
        while (l <= r) {
            let m = Math.floor(l + (r - l) / 2);
            if (nums[m] === target) return m;
            
            if (nums[l] <= nums[m]) {
                if (target > nums[m]) {
                    l = m + 1;
                } else if (target < nums[l]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else {
                if (target < nums[m]) {
                    r = m - 1;
                } else if (target > nums[r]) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }
        return -1;
    }
}
