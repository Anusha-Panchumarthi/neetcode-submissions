class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] 
        n = len(temperatures)
        res = [0] * n 

        for i in range(n):
            el = (temperatures[i], i)
            while stk and el[0] > stk[-1][0]:
                cur = stk.pop()
                res[cur[1]] = i - cur[1]
            stk.append(el)
        return res
