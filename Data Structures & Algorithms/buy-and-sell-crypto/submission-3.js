class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        // 10 3 5 6 7 2 4
        //    l       r
        // res = 4 -> 5 -> 6
        
        // 567 > 3, x < 3 => x < 3 < 5 6 7

        let l = 0;
        let r = 1;
        let res = 0;
        while (r < prices.length) {
            if (prices[l] < prices[r]) {
                res = Math.max(res, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return res;
    }
}
