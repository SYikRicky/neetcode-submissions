class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    // [[element,freq]]
    topKFrequent(nums, k) {
        const count = new Map();
        const freq = Array.from({ length: nums.length + 1 }, () => []);
        for (const n of nums) {
            count.set(n, (count.get(n) || 0) + 1);
        }
        console.log(count);
        for (const n of count) {
            freq[n[1]].push(n[0]);
        }
        console.log(freq)
        const res = [];
        for (let i = freq.length - 1; i > 0; i--) {
            console.log(`i = ${i}`)
            for (const n of freq[i]) {
                res.push(n);
                console.log(`When i = ${i}, res = ${res}`)
                if (res.length === k) {
                    return res;
                }
            }
        }
        return res;
    }
}
