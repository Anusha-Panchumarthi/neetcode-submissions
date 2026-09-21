class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s) 
        if n == 1:
            return 1 

        res = 1
        charSet = set(s)

        for c in charSet:
            # sliding window 
            l = 0 
            temp = 0 
            for r in range(n):
                if s[r] != c:
                    temp += 1
                
                while temp > k:
                    if s[l] != c:
                        temp -= 1
                    
                    l += 1
                
                res = max(r - l + 1, res)

        return res 
