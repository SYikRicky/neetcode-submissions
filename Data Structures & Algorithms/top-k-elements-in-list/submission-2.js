class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // (freq, letter)
        let bucket = new Map();
        // (letter, freq)
        let freq = new Map();
        let res = [];

        for (let i = 0; i < nums.length; i++) {
            freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
        }
        console.log(freq);

        for (let i = 1; i <= nums.length; i++) {
            bucket.set(i, []);
        }
        console.log(bucket);
        // i = [letter, freq]
        for (let i of freq) {
            let modifyArray = [...bucket.get(i[1]), i[0]]
            bucket.set(i[1], modifyArray);
        }
        console.log(bucket);

        for (let i = bucket.size; i > 0; i--) {
            console.log(`${i}: ${bucket.get(i)}`);
            if (bucket.get(i).length !== 0) {
                res.push(bucket.get(i));
            }
            if (res.length >= k) break;
        }

        return res;
    }
}
