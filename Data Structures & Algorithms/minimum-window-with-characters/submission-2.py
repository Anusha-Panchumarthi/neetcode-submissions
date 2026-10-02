class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        n = len(s)
        res, l = [0, 0], 0
        reslen = n + 1
        
        s1 = {} 
        for c in t:
            s1[c] = 1 + s1.get(c, 0)

        # headstart 
        while l < n and s[l] not in s1:
            l += 1
        lim = l

        goal = len(s1)
        cur = 0 

        s2 = {} 
    
        for r in range(lim, len(s)):
            # expand window 
            # if we hit goal, shrink window 
            if s[r] in s1:
                s2[s[r]] = 1 + s2.get(s[r], 0)
            
                if s2[s[r]] == s1[s[r]]:
                    cur += 1
            
            while cur == goal:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r]
                if s[l] in s1:
                    s2[s[l]] -= 1
                    if s2[s[l]] < s1[s[l]]:
                        cur -= 1
                    
                l += 1

        return s[res[0] : res[1] + 1] if reslen < n + 1 else ""






