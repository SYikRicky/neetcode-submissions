class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        console.log(strs.join("|"));
        return strs.join("|");
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        return str.split("|")
    }
}
