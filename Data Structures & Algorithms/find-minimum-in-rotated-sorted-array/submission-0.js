class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        // 345612
        //    l r
        
        let l = 0;
        let r = nums.length - 1;
        let res = 1000;
        while (l <= r) {
            let m = Math.floor((l + r) / 2);
            console.log(nums[m]);
            console.log(m)
            res = Math.min(res, nums[m]);
            if (nums[l] < nums[r]) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return res;
    }
}
