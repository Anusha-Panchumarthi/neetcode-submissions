class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while(l < r)
        {
            int tgt = nums[l] + nums[r];

            if(tgt == target){
                System.out.println(nums[l] + nums[r]);
                return new int[] {l+1, r+1};
            }
                

            if(tgt < target)
                l++;
            else
                r--;
        }

        return new int[] {-1, -1};
    }
}
