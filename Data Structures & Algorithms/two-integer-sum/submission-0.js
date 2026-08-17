class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const n = nums.length;
        const map = new Map();
        let result = new Array(2);
        
        for (let i = 0; i < n; i++) {
            map.set(nums[i], i);
        }

        for (let [i,j] of map) {
            if(map.has(target - i)) {
                result[0] = j
                result[1] = map.get(target - i);
                return result;
            }
        }

        return result;
    }
}
