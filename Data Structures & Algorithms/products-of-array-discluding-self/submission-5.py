class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = 1, 1
        res = [1] * n  

        for i in range(n):
            res[i] *= pre
            pre *= nums[i] 

            res[n-i-1] *= suf
            suf *= nums[n-i-1]
        
        return res

