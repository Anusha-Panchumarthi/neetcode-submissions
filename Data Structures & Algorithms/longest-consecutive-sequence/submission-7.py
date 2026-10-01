class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        cur = 0 
    
        temp = set(nums)

        for num in temp:
            if num - 1 not in temp:
                cur = num 
                streak = 1

                while cur + 1 in temp:
                    streak += 1
                    cur += 1

                res = max(res, streak)
        return res 