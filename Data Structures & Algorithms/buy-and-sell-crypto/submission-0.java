class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = prices[0];
        int movingPointer = 1;

        while (movingPointer < prices.length) {
            maxProfit = Math.max(maxProfit, prices[movingPointer] - minPrice);
            minPrice = Math.min(minPrice, prices[movingPointer]);
            movingPointer++;
        }
        return maxProfit;
    }
}
