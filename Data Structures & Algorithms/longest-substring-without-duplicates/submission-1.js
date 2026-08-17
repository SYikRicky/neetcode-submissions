class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // zxyzxyz
        //  l  r
        if (s.length === 1) return 1;
        let currentLetter = new Set();
        let l = 0;
        let res = 0;
        for (let r = 0; r < s.length; r++) {
            console.log(`${l} - ${r}`)
            if(currentLetter.has(s[r])) {
                res = Math.max(res, r - l);
                currentLetter.clear();
                l = r;
            } 
            currentLetter.add(s[r]);
        }
        return res;
    }
}
