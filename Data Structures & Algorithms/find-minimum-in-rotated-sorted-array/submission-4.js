class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        // binary search
        // 123456
        // l    r
        // 3456|012
        // l  m lmr
        // - nums[l] < nums[r], if yes, return res = min(nums[l], res)

        let l = 0;
        let r = nums.length - 1;
        let res = nums[0];
        while (l <= r) {
            if (nums[l] < nums[r]) {
                res = Math.min(res, nums[l]);
                break;
            }
            let m = Math.floor(l + (r - l) / 2);
            console.log(`m: ${m}, nums[m]: ${nums[m]}`);
            res = Math.min(res, nums[m]);
            if (nums[m] >= nums[l]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return res;
    }
}
