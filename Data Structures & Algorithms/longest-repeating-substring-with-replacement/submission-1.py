class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        cur = s[0]

        res, maxf = 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(count[s[r]], maxf)

            window_size = r - l + 1

            while window_size - maxf > k:
                count[s[l]] -= 1
                l += 1
                window_size -= 1
            
            res = max(window_size, res)
        
        return res
