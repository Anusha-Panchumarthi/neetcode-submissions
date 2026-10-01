class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*n, [1]*n
        res = [] 

        for i in range(n):
            pre = prefix[i-1] if i > 0 else 1
            prefix[i] = pre * nums[i]
            suf = suffix[n-i] if n-i < n else 1
            suffix[n-i-1] = suf * nums[n-i-1]
        
        for i in range(n):
            # prefix[i-1] * suffix[i+1]
            pre = prefix[i-1] if i > 0 else 1
            suf = suffix[i+1] if i < n-1 else 1
            res.append(pre * suf)
        
        return res

