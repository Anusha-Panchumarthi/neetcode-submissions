class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hash = new HashSet<>(nums.length);
        for(int i : nums)
        {
            hash.add(i);
        }

        int res = 0;
        for(int i : hash)
        {
            if(!hash.contains(i-1)){
                int len = 0;
                while(hash.contains(i + len))
                {
                    len++;
                }
                res = Math.max(len, res);
            } 
        }

        return res;
    }
}
