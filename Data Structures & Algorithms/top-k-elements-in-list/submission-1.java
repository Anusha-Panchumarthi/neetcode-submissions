class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // bucket sort 
        int n = nums.length;
        List<Integer>[] buckets = new List[n + 1];
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i = 0; i <= n; i++)
        {
            buckets[i] = new ArrayList<>();
        }
        for(int i : nums)
        {   
            hm.put(i, hm.getOrDefault(i, 0) + 1);
        }

        for(int key : hm.keySet())
        {
            buckets[hm.get(key)].add(key);
        }

        int[] res = new int[k];

        for(int i = n; i >= 0; i--)
        {
            if(buckets[i].size() == 0)
                continue;

            for(int freq : buckets[i]){
                res[(k--) - 1] = freq;
                if(k == 0)
                    return res;
            }
        }

        return res;
    }
}
