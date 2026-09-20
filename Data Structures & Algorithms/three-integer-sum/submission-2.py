class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                # if current value is same as previous 
                continue

            l, r = i+1, n-1
            while l < r:
                tgt = nums[l] + nums[r]
                if tgt == -1*nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif tgt < -1*nums[i]:
                    l += 1
                else:
                    r -= 1
            
        return res
            
