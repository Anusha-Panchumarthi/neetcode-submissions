class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        res = [] 
        i = 0 
        while i < len(s):
            while s[i].isdigit() and s[i] != "$":
                num += s[i]
                i += 1

            i += 1
            word = ""
            for j in range(i, i + int(num)):
                word += s[j] 
            res.append(word)
            i += int(num)
            num = ""

        return res 

            


