class Solution {
    public int climbStairs(int n) {
        int[] mem = new int[n];

        if(n == 1){
            return 1;
        }
    
        mem[0] = 1;
        mem[1] = 2;
        int i = 2;

        while(i < n){
            mem[i] = mem[i-1] + mem[i-2];
            i++;
        }

        return mem[n-1];
    }
}
