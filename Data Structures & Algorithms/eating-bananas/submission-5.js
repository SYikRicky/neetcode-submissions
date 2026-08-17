class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        // k <= piles' max
        // time = ceil(#bananas / rate)
        // [1...piles' max] find the value --> BS
        
        let maxValue = Math.max(...piles);
        let res = maxValue;
        
        let l = 1;
        let r = maxValue;
        while (l <= r) {
            let m = Math.floor((l + r) / 2);
            let time = 0;
            for (let i = 0; i < piles.length; i++) {
                time += Math.ceil(piles[i] / m);
            }
            if (time <= h) {
                res = Math.min(res, m);
                r = m - 1;
            } else {
                l = m + 1
            }
        }
        return res;
    }

}
