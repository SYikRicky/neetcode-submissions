class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let l = 1;
        let r = Math.max(...piles);
        let res = r
        while (l <= r) {
            const k = l + Math.floor((r - l) / 2);
    
            let timeRequired = 0;
            for (let i of piles) {
                timeRequired += Math.ceil(i / k);
            }
            if (timeRequired <= h) {
                if (k < res) res = k;
                r = k - 1;
            } else if (timeRequired > h) {
                l = k + 1;
            }
        }
        return res;
    }
}
