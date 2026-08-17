class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0;
        let r = 1;
        let n = prices.length;
        let res = 0;
        while (r < n) {
            console.log(`l:${l} r:${r}`);
            if (prices[l] > prices[r] && r <= n) {
                l = r;
            } else if (prices[l] < prices[r]) {
                console.log(`res: ${res}`);
                res = Math.max(prices[r] - prices[l], res);
            }
            r++;
        }
        return res;
    }
}
