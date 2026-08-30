class Solution {
    public boolean isAnagram(String s, String t) {
        int[] temp = new int[26];

        for(char i : s.toCharArray())
        {
            temp[i - 'a']++;
        }

        for(char i : t.toCharArray())
        {
            if(temp[i-'a'] == 0)
                return false;
            temp[i - 'a']--;
        }

        return Arrays.stream(temp).sum() == 0 ? true : false;
    }
}
