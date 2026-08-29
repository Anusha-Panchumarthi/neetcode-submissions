class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();
        for(String s : strs)
        {
            char[] temp = new char[26];
            for(char c : s.toCharArray())
            {
                temp[c - 'a']++;
            }

            String key = new String(temp);
            List<String> arr = hm.getOrDefault(key, new ArrayList<>());
            arr.add(s);
            hm.put(key, arr);
        }

        List<List<String>> res = new ArrayList<>();
        for(String key : hm.keySet())
        {
            res.add(hm.get(key));
        }

        return res;
    }
}
