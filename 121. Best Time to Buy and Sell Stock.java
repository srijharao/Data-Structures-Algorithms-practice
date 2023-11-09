class Solution {
    public int maxProfit(int[] prices) {
        //pick lowest day to buy
        //highest day to sell
        int minSoFar = Integer.MAX_VALUE;
        int maxProfit = 0;

        for(int i =0; i<prices.length; i++){
            minSoFar = Math.min(minSoFar, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minSoFar);
        }
        return maxProfit;
    }
}
