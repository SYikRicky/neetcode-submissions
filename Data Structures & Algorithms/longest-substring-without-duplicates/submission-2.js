class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // pwwkew
        //  l r
        // [p]
        if (s.length === 1) return 1;
        let currentLetter = new Set();
        let l = 0;
        let res = 0;
        for (let r = 0; r < s.length; r++) {
            console.log(`${l} - ${r}`)
            while(currentLetter.has(s[r])) {
                currentLetter.delete(s[l]);
                l++;
            }
            currentLetter.add(s[r]);
            res = Math.max(res, r - l + 1); 
        }
        return res;
    }
}
