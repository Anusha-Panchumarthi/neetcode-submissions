class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for(String s : strs)
        {
            sb.append(String.valueOf(s.length()) + '#' + s);
        }

        String res = sb.toString();
        return res;
    }

    public List<String> decode(String str) {
        int i = 0;
        char[] s = str.toCharArray();

        List<String> res = new ArrayList<>();

        while(i < s.length)
        {
            int len = 0;

            while(s[i] != '#' && Character.isDigit(s[i]))
            {
                len = len*10 + (s[i++] - '0');
            }

            i++; // skipping the #

            res.add(str.substring(i, i + len));
            i = i + len;
        }

        return res;
    }
}
