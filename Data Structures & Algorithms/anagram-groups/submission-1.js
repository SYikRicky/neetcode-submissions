class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hash = new Map();
        for (let i of strs) {
            let sortedStrs = i.split("").sort().join("");
            let modifyValue = hash.has(sortedStrs) ? hash.get(sortedStrs).concat(i) : [i];
            hash.set(sortedStrs, modifyValue);
        }
        return Array.from(hash.values());
    }
}
