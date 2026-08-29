class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] prefix = new int[n];
        int[] suffix = new int[n];

        prefix[0] = nums[0];
        suffix[n-1] = nums[n-1];

        for(int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i-1] * nums[i];
            suffix[n - i - 1] = suffix[n - i] * nums[n - i - 1];
        }

        int[] res = new int[n];
        for(int i = 0; i < n; i++)
        {
            int temp = 1;
            temp *= (i-1 >= 0) ? prefix[i-1] : 1;
            temp *= (i + 1 < n) ? suffix[i+1] : 1;

            res[i] = temp;
        }

        return res;
    }
}  
