class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    
    
    hasDuplicate(nums) {
        let map = new Set();
        for (let i of nums) {
            if (map.has(i)) return true;
            map.add(i);
        }
        return false;
    }
}
