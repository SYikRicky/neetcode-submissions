class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        // 51234
        // l m r
        // 34512
        // l m r
        
        let l = 0;
        let r = nums.length - 1;
        let res = 1000;
        while (l <= r) {
            let m = Math.floor((l + r) / 2);
            console.log(`nums[m]: ${nums[m]}, m: ${m}`);
            res = Math.min(res, nums[m]);
            if (nums[l] <= nums[m]) {
                l = m + 1
            } else {
                r = m - 1;
            }
        }
        return res;
    }
}
