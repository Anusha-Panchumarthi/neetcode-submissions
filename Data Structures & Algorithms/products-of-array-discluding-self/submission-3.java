class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, 1);

        int pref = 1, suf = 1;
        for(int i = 0; i < n; i++)
        {
            res[i] *= pref;
            pref *= nums[i];

            int idx = n - i - 1;
            res[idx] *= suf;
            suf *= nums[idx];
        }

        return res;
    }
}  
