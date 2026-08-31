from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        def calcKey(s):
            temp = [0 for _ in range(26)]

            for c in s:
                temp[ord(c) - ord('a')] += 1
            
            return "#".join(map(str, temp))

        for s in strs:
            key = calcKey(s)
            hm[key].append(s)
        
        return list(hm.values())
