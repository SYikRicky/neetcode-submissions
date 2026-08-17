class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();
        const sortedArray = new Array(...strs)
        sortedArray.forEach((word) => {
            let sortedWord = word.split('').sort().join('');
            if (!map.has(sortedWord)) {
                map.set(sortedWord,[word]);
            } else {
                let modifiedMapValue = Array.from(map.get(sortedWord));
                modifiedMapValue.push(word);
                map.set(sortedWord, modifiedMapValue);
            }
        })
        return [...map.values()];
    }
}
