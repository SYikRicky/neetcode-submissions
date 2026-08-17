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
            if (map.has(nums[i])) {
                let modifiedArray = map.get(nums[i]);
                modifiedArray.push(i);
                map.set(nums[i], modifiedArray);
            } else {
                map.set(nums[i], [i]);
            }
        }

        console.log(map);
        
        for (let [firstNum, index] of map) {
            console.log(`checking ${firstNum} and finding ${target - firstNum}`)
            if (target - firstNum === firstNum) {
                result[0] = index[0];
                result[1] = index[1];
                break;
            }
            if (map.has(target - firstNum)) {
                result[0] = index[0];
                result[1] = map.get(target - firstNum)[0]
                break;
            }
        }

        return result; 
        
    }
}
