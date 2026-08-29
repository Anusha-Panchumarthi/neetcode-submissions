class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hash = new HashSet<>(nums.length);
        for(int i : nums)
        {
            hash.add(i);
        }

        List<Integer> cands = new ArrayList<>();
        int res = 0;
        for(int i : nums)
        {
            if(!hash.contains(i-1)){
                int temp = i, len = 0;
                while(hash.contains(temp))
                {
                    temp++;
                    len++;
                }
                res = Math.max(len, res);
            } 
        }

        return res;
    }
}
