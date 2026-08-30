class Solution {
    public boolean isAnagram(String s, String t) {
        int[] temp = new int[26];
        int n = s.length();

        if(n != t.length())
            return false;

        for(int i = 0; i < n; i++)
        {
            temp[s.charAt(i) - 'a']++;
            temp[t.charAt(i) - 'a']--;
        }

        for(int i : temp)
        {
            if(i != 0)
                return false;
        }

        return true;
    }
}
