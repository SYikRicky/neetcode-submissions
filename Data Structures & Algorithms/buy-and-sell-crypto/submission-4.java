class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        int left = 0, right = 1;
        while (right < prices.length) {
            System.out.println(left);
            System.out.println(right);
            if (prices[left] > prices[right]) {
                left = right;
                right += 1;
            } else {
                int profit = prices[right] - prices[left]; 
                if (profit > result) {
                    result = profit;
                }
                right += 1;
            }
        }
        return result;
    }
}
