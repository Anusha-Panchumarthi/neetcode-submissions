class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        res = 0 

        l, r = 0, len(height) - 1
        left, right = height[l], height[r]

        while l <= r:
            if left <= right: # left is smaller, process left 
                left = max(left, height[l])
                res += (left - height[l])
                l += 1
            else:
                right = max(right, height[r])
                res += (right - height[r])
                r -= 1        
        return res 