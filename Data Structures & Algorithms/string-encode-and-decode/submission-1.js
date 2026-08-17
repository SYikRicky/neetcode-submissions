class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encodedWord = "";
        for (let i of strs) {
            encodedWord += i.length + "#" + i
        }
        console.log(encodedWord);
        return encodedWord;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 0;
        let res = [];
        while (i < str.length) {
            let j = i;
            while (str[j] !== "#") {
                j++;
            }
            let length = parseInt(str.substring(i,j));
            i = j + 1;
            j = i + length;
            res.push(str.substring(i,j));
            i = j;
        }
        return res;
    }
}
