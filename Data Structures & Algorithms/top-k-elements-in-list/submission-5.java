class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // bucket sort 
        int n = nums.length;
        List<Integer>[] buckets = new List[n + 1];
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i : nums)
        {   
            hm.put(i, hm.getOrDefault(i, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : hm.entrySet())
        {
            int key = entry.getKey();
            int freq = entry.getValue();

            if(buckets[freq] == null)
                buckets[freq] = new ArrayList<>();

            buckets[freq].add(key);
        }

        int[] res = new int[k];
        int idx = 0;
        for(int i = n; i >= 0; i--)
        {
            if(buckets[i] == null)
                continue;
            for(int freq : buckets[i]){
                res[idx++] = freq;
                if(k == idx)
                    return res;
            }
        }

        return res;
    }
}
