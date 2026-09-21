class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        l = 0 
        res = 1 
        tracker = set() 
        tracker.add(s[l])

        for r in range(1, n):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            
            tracker.add(s[r])
            res = max(r - l + 1, res)

        return res